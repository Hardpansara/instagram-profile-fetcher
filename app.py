from flask import Flask, request, jsonify
import instaloader
import os
import json
import requests
import csv
from datetime import datetime
from fpdf import FPDF

app = Flask(__name__)

# Initialize Instaloader
loader = instaloader.Instaloader()

# Setup paths
CSV_FILE = "instagram_data_log.csv"
DATA_DIR = "accounts_data"
os.makedirs(DATA_DIR, exist_ok=True)

# Setup CSV
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([ 
            "Timestamp", "Username", "Full Name", "Bio", "Followers",
            "Following", "Posts", "Profile Picture URL"
        ])

def log_to_csv(data):
    with open(CSV_FILE, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def save_to_json(folder_path, data):
    with open(os.path.join(folder_path, "profile_data.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

def download_media(url, save_path):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(save_path, 'wb') as f:
                f.write(response.content)
    except Exception as e:
        print(f"Failed to download media: {e}")

# Generate HTML report
def generate_html_report(folder_path, data):
    html_content = """
    <html>
    <head>
        <title>Instagram Profile Report</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f7f6;
                color: #333;
                margin: 0;
                padding: 0;
            }
            h1 {
                text-align: center;
                color: #2c3e50;
                font-size: 2.5em;
                margin-top: 40px;
            }
            h2 {
                color: #34495e;
                font-size: 1.8em;
                text-decoration: underline;
            }
            .container {
                width: 80%;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                margin-top: 20px;
            }
            .section-title {
                font-size: 20px;
                font-weight: bold;
                color: #2c3e50;
                margin-top: 20px;
                border-bottom: 2px solid #3498db;
                padding-bottom: 5px;
                margin-bottom: 20px;
            }
            .profile-info p {
                font-size: 16px;
                line-height: 1.6;
                margin: 10px 0;
            }
            .key {
                font-weight: bold;
                color: #3498db;
            }
            a {
                color: #3498db;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
            .footer {
                text-align: center;
                font-size: 14px;
                color: #95a5a6;
                margin-top: 30px;
                padding-top: 20px;
                border-top: 2px solid #ecf0f1;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Instagram Profile Report</h1>
            <div class="section-title">Profile Information</div>
            <div class="profile-info">
    """

    # Profile Information Section
    for key in ["Username", "Full Name", "Bio", "Followers", "Following", "Posts", "External URL", "Is Business Account", "Is Verified"]:
        val = data.get(key, 'N/A')
        html_content += f"<p><span class='key'>{key}:</span> {str(val)}</p>"

    # Closing HTML tags
    html_content += """
        <div class="footer">
            <p>Generated by Instagram Profile Fetcher</p>
        </div>
        </div>
    </body>
    </html>
    """
    
    # Save the HTML content to a file
    html_output_path = os.path.join(folder_path, "report.html")
    with open(html_output_path, "w", encoding="utf-8") as html_file:
        html_file.write(html_content)
    
    return html_output_path

@app.route('/fetch_instagram', methods=['GET'])
def fetch_instagram_data():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username parameter is required"}), 400

    try:
        profile = instaloader.Profile.from_username(loader.context, username)
        folder_path = os.path.join(DATA_DIR, username)
        media_path = os.path.join(folder_path, "media")
        os.makedirs(media_path, exist_ok=True)

        profile_data = {
            "Username": profile.username,
            "Full Name": profile.full_name,
            "Bio": profile.biography,
            "Followers": profile.followers,
            "Following": profile.followees,
            "Posts": profile.mediacount,
            "Profile Picture URL": profile.profile_pic_url,
            "External URL": profile.external_url,
            "Is Business Account": profile.is_business_account,
            "Is Verified": profile.is_verified
        }

        download_media(profile.profile_pic_url, os.path.join(media_path, "profile_pic.jpg"))

        # Remove code related to fetching recent posts for public profiles

        save_to_json(folder_path, profile_data)
        generate_html_report(folder_path, profile_data)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_to_csv([ 
            timestamp, profile.username, profile.full_name, profile.biography,
            profile.followers, profile.followees, profile.mediacount,
            profile.profile_pic_url
        ])

        return jsonify(profile_data)

    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"error": "Profile does not exist"}), 404
    except instaloader.exceptions.PrivateProfileNotFollowedException:
        return jsonify({"error": "This is a private account. Data access is restricted"}), 403
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

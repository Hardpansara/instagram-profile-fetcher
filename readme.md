# Instagram Profile Fetcher 📸

This Flask-based web application allows you to fetch and display Instagram profile information for a given username. The application retrieves essential profile data such as the username, full name, bio, follower count, and more. It also fetches the most recent public post from the profile and stores the data in various formats like JSON and HTML. ✨

---

### Features 🌟

- Fetch Instagram profile data including:
  - **Username** 
  - **Full Name** 
  - **Bio** 
  - **Followers** 
  - **Following** 
  - **Posts count** 
  - **Profile picture URL** 
  - **External URL** 
  - **Business account status** 
  - **Verified status** 
  - **Public/Private profile status** 
- Download and save the **profile picture**  and **recent post media** (image or video) .
- Store profile data in a structured **JSON format** .
- Generate an aesthetically designed **HTML report** with profile and recent post details .
- Log profile information into a **CSV file** with a timestamp .

---

### Installation ⚙️

To set up this project, follow these steps:

#### 1. Clone the repository

```bash
git clone https://github.com/Hardpansara/instagram-profile-fetcher.git
cd instagram-profile-fetcher
```

#### 2. Create a virtual environment (optional but recommended)
```bash 
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```
#### 3. Install dependencies

```bash 

pip install -r requirements.txt
```

---

### Usage 🚀
**1. Run the Flask application**
   To start the server, run:

```bash
python app.py
```
The app will be available at http://localhost:5000.

**2. Fetch Instagram profile data**
Send a GET request to the `/fetch_instagram` endpoint with the `username` parameter:

Example:

```bash 
curl "http://localhost:5000/fetch_instagram?username=instagram"
```
This will return a JSON response containing the profile information.

**Example Response:**
```bash 
{
  "Username": "instagram",
  "Full Name": "Instagram",
  "Bio": "Bringing you closer to the people and things you love.",
  "Followers": 1000000000,
  "Following": 500,
  "Posts": 2500,
  "Profile Picture URL": "https://instagram.com/path/to/profile/pic.jpg",
  "External URL": "https://www.instagram.com/instagram/",
  "Is Business Account": true,
  "Is Verified": true,
  "Is Public": true,
  "Recent Post": {
    "Caption": "Exploring new places!",
    "Likes": 500000,
    "Comments": 12000,
    "Post URL": "https://www.instagram.com/p/abcd1234/",
    "Media URL": "https://instagram.com/path/to/post/media.jpg",
    "Is Video": false
  }
}
```

**3. Output Files 📁**

- Profile data will be saved in a folder named after the Instagram username (`e.g., accounts_data/instagram`).

- Profile data will be saved in the `profile_data.json` file within the respective folder.

- An HTML report (`report.html`) will be generated within the folder.

- Profile information will be logged in `instagram_data_log.csv`.

---

### File Structure 📂

```bash 
instagram-profile-fetcher/
│
├── app.py                   # Main Flask application 
├── instagram_data_log.csv   # CSV log file 
├── accounts_data/           # Folder where profile data is saved 
│   └── instagram/           # Data for the 'instagram' username 
│       ├── profile_data.json
│       ├── report.html
│       └── media/
│           ├── profile_pic.jpg
│           └── latest_post.jpg
├── requirements.txt         # List of required Python packages 
└── README.md                # Project documentation 
```

---
### Requirements 🛠️
- Python 3.x

- Flask

- Instaloader

- Requests
---
### Dependencies 
The required Python libraries are listed in requirements.txt. Install them using:
```bash 
pip install -r requirements.txt
```
---
### Limitations 
- **Private Profiles :** Data fetching is not supported for private accounts that you do not follow. If the account is private, you will get a permission error.

- **Rate Limiting :** Instagram may impose rate limits on profile requests. If you make too many requests in a short time, you might get temporarily blocked from fetching data. Please wait a few minutes before trying again.

- **API Restrictions :** This application is based on the Instaloader library, which is limited by Instagram's own API restrictions. Some information (e.g., posts or stories) might be inaccessible if the account has privacy settings in place.

- **Limited Recent Post Fetch :** Only the most recent post is fetched for public accounts. Older posts will not be retrieved.

- **Media Download Size :** Large media files (e.g., videos) may take time to download, and the process could fail depending on the size and network conditions.

- **No Real-Time Updates :** This application does not update the profile data in real time. It fetches the data at the moment of the request.

---
### 🤝 Contributing

Contributions are welcome! Whether you're fixing a bug, improving documentation, or adding new features, your help is appreciated.

#### How to Contribute

1.  Fork the repository
2.  Create a new branch (`git checkout -b feature-branch`)
3.  Make your changes
4.  Commit your changes (`git commit -m 'Add awesome feature'`)
5.  Push to the branch (`git push origin feature-branch`)
6.  Open a Pull Request

We welcome suggestions, code improvements, feature requests, and constructive feedback.

---

### 📬 Contact

If you have any questions, suggestions, or want to collaborate directly:

-  Email: [Hard Pansara](hardpansara10@gmail.com)  
-  GitHub: [Hardpansara](https://github.com/Hardpansara)  
-  LinkedIn: [Hard Pansara](http://linkedin.com/in/hard-pansara-22582a288) 

Let’s build something awesome together! 

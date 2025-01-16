# YouTube Playlist Downloader with Cookies

## Steps to Export Cookies from Firefox

1. **Install Firefox Extension**:
   - Visit [Cookies.txt Extension](https://addons.mozilla.org/en-US/firefox/addon/cookies-txt/).
   - Click "Add to Firefox" → "Add" → "Okay, Got It".
   
2. **Export YouTube Cookies**:
   - Open [YouTube](https://youtube.com) and log in.
   - Click the cookies extension icon (looks like a cookie).
   - Click "Current Site".
   - Save the file as `cookies.txt` on your desktop.

## Steps to Run Python Script

1. Ensure you have Python and pip installed:
   ```bash
   `python -m ensurepip --upgrade`
   `python -m pip install yt-dlp`
   ```

3. Make sure the `cookies.txt` file is on your desktop.

4. Run the Python script to download YouTube playlists using your authentication from the cookies file.

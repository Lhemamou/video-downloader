import subprocess
import sys
import os
import logging

def setup_logging(log_file):
    # Configure logging to write to both console and a log file
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(log_file),  # Log to a file
            logging.StreamHandler(sys.stdout)  # Log to the console
        ]
    )

def download_videos(sub_lang, urls_file):
    # Check if the file exists
    if not os.path.exists(urls_file):
        logging.error(f"The file {urls_file} does not exist.")
        return

    # Create the download directory if it doesn't exist
    download_dir = os.path.join("download", sub_lang)
    os.makedirs(download_dir, exist_ok=True)

    # Base command for yt-dlp
    command = [
        "yt-dlp",
        "--merge-output-format", "mp4",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs", sub_lang,
        "-a", urls_file,
        "--output", os.path.join(download_dir, "%(title)s.%(ext)s"),
        "--no-overwrites"  # Skip downloading if the file already exists
    ]

    try:
        # Execute the command
        logging.info(f"Starting download for language: {sub_lang}")
        subprocess.run(command, check=True)
        logging.info("Download completed.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error executing yt-dlp: {e}")
    except Exception as e:
        logging.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Check if the necessary arguments were provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <subtitle_language> <urls_file>")
        sys.exit(1)

    # Arguments
    sub_lang = sys.argv[1]  # Subtitle language (e.g., "fr")
    urls_file = sys.argv[2]  # Name of the file containing the URLs

    # Set up logging
    log_file = os.path.join("download", sub_lang, "download.log")
    os.makedirs(os.path.dirname(log_file), exist_ok=True)  # Ensure the directory exists
    setup_logging(log_file)

    # Call the download function
    download_videos(sub_lang, urls_file)
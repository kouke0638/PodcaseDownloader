# Podcast Downloader

This project is a simple Python script to download podcast episodes from an RSS feed and save them as MP3 files.

## Requirements

To run this script, you need to have Python installed on your system. Additionally, you need to install the required Python packages listed in `requirements.txt`.

### Installation

1. Clone the repository or download the script files.
2. Navigate to the project directory.
3. Install the required packages using pip:

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. Open the `main.py` file.
2. Replace `<YourPodcaseRSSFeedLink>` with your Podcast RSS feed link. You can find your Podcast RSS feed link from [Castos](https://castos.com/tools/find-podcast-rss-feed/).
3. Run the script:

   ```sh
   python main.py
   ```

The script will parse the RSS feed, create a `files` directory if it doesn't exist, and download each podcast episode as an MP3 file into the `files` directory.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

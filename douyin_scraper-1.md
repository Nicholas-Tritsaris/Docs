# douyin\_scraper

The `douyin_scraper` repository is a **command-line tool** designed to scrape **Douyin** video metadata and download videos based on a list of provided video URLs. It filters the metadata according to a specified set of **JSON keys** and outputs the results in a **CSV file**. The tool utilizes the **douyin-tiktok-scraper** library to interact with the Douyin platform.

### Overview

The `douyin_scraper` repository provides a simple and efficient way to collect and analyze **Douyin video metadata**. By specifying a list of video URLs and desired metadata fields, users can easily download videos and extract relevant information.

### Features

* Scrapes **Douyin video metadata** based on provided video URLs
* Filters metadata according to specified **JSON keys**
* Downloads videos corresponding to the provided URLs
* Outputs filtered metadata in a **CSV file**
* Utilizes the **douyin-tiktok-scraper** library for platform interaction

### Installation

{% stepper %}
{% step %}
### Clone the repository

Clone the repository using `git clone https://github.com/Clemapfel/douyin_scraper.git`
{% endstep %}

{% step %}
### Install required dependencies

```bash
pip install json
pip install csv
pip install requests
pip install douyin-tiktok-scraper
```
{% endstep %}
{% endstepper %}

### Usage

{% stepper %}
{% step %}
### Collect Video URLs

Create a file (e.g., `video_ids.txt`) containing a list of **Douyin video URLs**, one per line.
{% endstep %}

{% step %}
### Specify Metadata Filter

Create a file (e.g., `filter.txt`) containing a list of **JSON keys** to extract from the video metadata.
{% endstep %}

{% step %}
### Execute Script

Run the script using `python3 scrape.py video_ids.txt filter.txt`, replacing `video_ids.txt` and `filter.txt` with the files created in steps 1 and 2.
{% endstep %}

{% step %}
### Collect Output

After the script finishes running, collect the output **CSV file** and downloaded videos from the `./out` directory.
{% endstep %}
{% endstepper %}

### Dependencies

The `douyin_scraper` repository relies on the following dependencies:

* **json**
* **csv**
* **requests**
* **douyin-tiktok-scraper**

### Troubleshooting

For a full list of allowed **JSON keys**, run the script once and inspect one of the `raw.json` files in the `douyin_scraper/out` directory. If issues arise during execution, ensure that the required dependencies are installed and the input files are formatted correctly.

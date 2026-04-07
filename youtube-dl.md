# youtube dl

youtube-dl is a **command-line program** to download videos from [YouTube.com](https://www.youtube.com/) and other video sites. It is a free and open-source software that provides an easy way to download videos from various online platforms. The program is written in **Python** and is available for **UNIX**, **Windows**, and **macOS** operating systems.

## Overview

youtube-dl is designed to be a simple and efficient way to download videos from online platforms. It supports a wide range of video sites, including [YouTube](https://www.youtube.com/), [Vimeo](https://vimeo.com/), and many others. The program provides various options for customizing the download process, such as selecting the video format, quality, and output file name.

## Features

The key features of youtube-dl include:

* **Video download**: Download videos from YouTube and other video sites
* **Format selection**: Select the video format, quality, and codec
* **Output template**: Customize the output file name and directory
* **Video selection**: Select specific videos or playlists to download
* **Configuration**: Configure the program settings, such as proxy, user agent, and more

## Installation

{% tabs %}
{% tab title="UNIX" %}
Use `sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl` or `sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl`
{% endtab %}

{% tab title="Windows" %}
Download the [youtube-dl.exe](https://yt-dl.org/latest/youtube-dl.exe) file and add it to the system **PATH**
{% endtab %}

{% tab title="macOS" %}
Install using [Homebrew](https://brew.sh/) with `brew install youtube-dl` or [MacPorts](https://www.macports.org/) with `sudo port install youtube-dl`
{% endtab %}

{% tab title="pip" %}
Alternatively, install using **pip** with `sudo -H pip install --upgrade youtube-dl`
{% endtab %}
{% endtabs %}

## Configuration

youtube-dl provides various configuration options, including:

* **Proxy**: Set a proxy server to use for downloading videos
* **User agent**: Set a custom user agent to use for downloading videos
* **Output directory**: Set the output directory for downloaded videos
* **Format**: Set the default video format and quality

## Output Template

The output template can be customized using various placeholders, such as:

* **%**(id)s: The video ID
* **%**(title)s: The video title
* **%**(format)s: The video format
* **%**(resolution)s: The video resolution

## Format Selection

youtube-dl supports various video formats, including:

* **MP4**: A widely supported format for video playback
* **WebM**: A format for web-based video playback
* **FLV**: A format for Flash-based video playback

## Video Selection

youtube-dl provides options for selecting specific videos or playlists to download, including:

* **Video ID**: Download a specific video by ID
* **Playlist**: Download a playlist of videos
* **Channel**: Download all videos from a specific channel

## FAQ

For frequently asked questions and troubleshooting, refer to the [youtube-dl FAQ](https://ytdl-org.github.io/youtube-dl/faq.html) page.

## Developer Instructions

For instructions on how to contribute to the youtube-dl project, refer to the [developer instructions](https://github.com/ytdl-org/youtube-dl/blob/master/README.md#developer-instructions) section.

## Embedding youtube-dl

youtube-dl can be embedded in other applications using the [youtube-dl API](https://ytdl-org.github.io/youtube-dl/embedding.html).

## Bugs

To report bugs or issues, refer to the [youtube-dl issue tracker](https://github.com/ytdl-org/youtube-dl/issues).

## Copyright

youtube-dl is released under the **MIT License**. For more information, refer to the [youtube-dl copyright](https://github.com/ytdl-org/youtube-dl/blob/master/COPYING) notice.

The hacker-challenge repository is an interactive web-based challenge designed to help individuals new to the web inspector develop their skills. The challenge consists of a series of levels that can be completed using the web inspector, a hidden panel available in all web browsers that allows users to navigate and temporarily modify elements on a page. The challenge is hosted at [https://hacker-challenge.netlify.app/](https://hacker-challenge.netlify.app/) and can also be run locally by cloning the repository and running a simple HTTP server.

## Overview
The hacker-challenge is designed to be a fun and interactive way to learn about the web inspector and its various features. The challenge is divided into a series of levels, each with its own unique objective and requirements. Users can complete the levels by using the web inspector to modify elements on the page, view logs and errors, and work with local storage.

## Features
The hacker-challenge repository includes several key features, including:
* A series of challenges that can be completed using the web inspector
* A web inspector with multiple tabs, including **Elements**, **Console**, **Sources**, and **Application**
* The ability to run the challenge locally by cloning the repository and running a simple HTTP server
* The option to contribute to the challenge by creating a pull request or adding an issue with a suggestion

## Useful Inspector Tabs
The web inspector includes several useful tabs, including:
* **Elements**: This tab displays the HTML being rendered on the page and allows users to expand and collapse HTML sections
* **Console**: This tab displays logs and errors of the JavaScript being rendered on the page, including validation, tips, and hints
* **Sources**: This tab displays the files being loaded into the browser for the page, including HTML, JavaScript, and CSS
* **Application**: This tab includes the **Local Storage** area, which displays any data that the website has saved to the user's browser

## Installation
To run the hacker-challenge locally, follow these steps:
1. Clone the GitHub repository
2. `cd` into the repository
3. Run `python -m SimpleHTTPServer` in the terminal
4. Open `http://localhost:8000` in the browser

## Contributing
Users can contribute to the hacker-challenge by creating a pull request or adding an issue with a suggestion. To add a new challenge, follow these steps:
### Adding a new challenge
1. Duplicate the [challenges/template.html](challenges/template.html) page in both the `hard` and `normal` folders
2. Edit the page as needed
3. Rename the files to an animal in alphabetical order from the last page
*Note: Use [this site](https://a-z-animals.com/animals/) to find animal names in alphabetical order*
# Net Atlas Ultimate

### Overview

Net Atlas Ultimate is a **neon-themed** interactive 3D world explorer that displays websites by country using a spinning globe, visual effects, flags, icons, and categories. The application utilizes a combination of _Three.js_, _three-globe_, and _world-atlas TopoJSON_ to create a realistic and engaging experience.

### Features

The key features of Net Atlas Ultimate include:

* A **spinning 3D globe** that allows users to explore countries and their corresponding websites
* **Real country polygons** generated from _world-atlas TopoJSON_ data
* An **orbital visual style** that incorporates a starfield, layered neon orbits, and an atmosphere halo
* The ability to **click on a country** to fetch live metadata from _RESTCountries_, display its flag and stats, and show websites defined in the `websites-by-country.json` file
* **Neon**, _glassmorphism_, _CRT scanlines_, and _hover bloom_ effects to enhance the visual experience
* **Website favicons**, _country flags_, and _TLD-based categories_ to provide additional context

### Data

The `websites-by-country.json` file is used to store website data, with each country represented by its **ISO 3166-1 alpha-2 code** (e.g. "AU", "US", "JP", etc.). The file format is as follows:

```json
{
  "AU": [
    { "url": "https://abc.net.au", "category": "media" },
    { "url": "https://www.australia.gov.au", "category": "government" }
  ],
  "US": [
    { "url": "https://www.whitehouse.gov", "category": "government" },
    { "url": "https://www.nasa.gov", "category": "science" }
  ]
}
```

This data can be populated using various sources, including [Wikipedia](https://www.wikipedia.org/), [BuiltWith](https://builtwith.com/), [all.site](https://all.site/), and [internet-map.net](https://internet-map.net/).

### Installation

To deploy Net Atlas Ultimate to **GitHub Pages**, follow these steps:

1. Create a new repository and add the necessary files: `index.html`, `style.css`, `script.js`, `websites-by-country.json`, `LICENSE`, `.gitignore`, and `README.md`
2. Push the changes to GitHub
3. Enable GitHub Pages by going to Settings → Pages → source = `main` / root
4. The site will be available at `https://<username>.github.io/<repo>/`

### Usage

To use Net Atlas Ultimate, simply navigate to the deployed site and interact with the spinning globe. Click on a country to view its corresponding websites, flag, and stats. The application is designed to provide a visually engaging and informative experience, and can be used to explore websites from around the world.

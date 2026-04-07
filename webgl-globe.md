# webgl globe

The **WebGL Globe** is an open platform for geographic data visualization created by the Google Data Arts Team. It is a tool for visualizing latitude longitude based information using _WebGL_, allowing users to create interactive and animated globes. The platform encourages users to copy the code, add their own data, and create their own globes, with examples available at [experiments.withgoogle.com/chrome/globe](http://experiments.withgoogle.com/chrome/globe).

### Overview

The **WebGL Globe** supports data in _JSON_ format, with a sample available [here](https://github.com/dataarts/webgl-globe/blob/master/globe/population909500.json). The platform makes heavy use of the [Three.js library](https://github.com/mrdoob/three.js/), a popular _JavaScript_ library for creating and rendering 3D graphics in the browser.

### Features

The **WebGL Globe** has several key features, including:

* Support for _JSON_ data format
* Interactive and animated globe visualization
* Ability to add custom data and create unique globes
* Examples and inspiration available at [experiments.withgoogle.com/chrome/globe](http://experiments.withgoogle.com/chrome/globe)

### Data Format

The **WebGL Globe** expects data in the following _JSON_ format:

```javascript
var data = [
    [
    'seriesA', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
    ],
    [
    'seriesB', [ latitude, longitude, magnitude, latitude, longitude, magnitude, ... ]
    ]
];
```

This format allows for multiple series of data to be displayed on the globe, with each series consisting of a list of latitude, longitude, and magnitude values.

### Basic Usage

To use the **WebGL Globe**, users can follow these basic steps:

```javascript
// Where to put the globe?
var container = document.getElementById( 'container' );

// Make the globe
var globe = new DAT.Globe( container );

// We're going to ask a file for the JSON data.
var xhr = new XMLHttpRequest();

// Where do we get the data?
xhr.open( 'GET', 'myjson.json', true );

// What do we do when we have it?
xhr.onreadystatechange = function() {

    // If we've received the data
    if ( xhr.readyState === 4 && xhr.status === 200 ) {

        // Parse the JSON
        var data = JSON.parse( xhr.responseText );

        // Tell the globe about your JSON data
        for ( var i = 0; i < data.length; i ++ ) {
            globe.addData( data[i][1], {format: 'magnitude', name: data[i][0]} );
        }

        // Create
```

This code polls a _JSON_ file for geo-data and adds it to an animated, interactive **WebGL Globe**.

### Sharing and Community

The **WebGL Globe** community encourages users to share their creations, with a [submission form](http://www.chromeexperiments.com/submit) available for users to showcase their work. The Google Data Arts Team also posts their favorite globes publicly, providing inspiration and examples for users to create their own unique visualizations.

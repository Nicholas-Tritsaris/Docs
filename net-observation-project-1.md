# net observation project

The Net Observation Project is a non-commercial global internet observation and exposure analysis project that utilizes datasets from **Censys**. This project is led by _Nicholas Tritsaris_ and features a responsive **Cloudflare Pages** frontend paired with a zero-cold-start **Pages Function** that aggregates live intelligence from the **Censys Search v2 API**. The project provides scanning analytics, certificate insights, service enumeration, and research findings.

### Overview

The Net Observation Project is designed to provide a comprehensive overview of the global internet landscape. By leveraging the **Censys Search v2 API**, the project is able to collect and analyze large datasets, providing valuable insights into internet trends and patterns. The project's frontend is built using **Cloudflare Pages**, which provides a fast and responsive user interface. The backend is powered by **Cloudflare Pages Functions**, which enables the project to aggregate live intelligence from the **Censys Search v2 API**.

### Features

The Net Observation Project features a range of tools and functionalities, including:

* Animated **cyber-neon theme** with automatic dark/light behavior and manual override
* Collapsible **sidebar navigation** mirrored on every page for rapid context switching
* Live **/api/censys-summary** polling drives **Chart.js** charts, **D3** world heatmap, and terminal outputs
* Terminal-style **command runner** with plugin registration API and sample plugin
* **JSON/CSV data visualiser** supporting clipboard paste or file uploads
* **Settings control** for backend endpoint and **Auth0 SPA** configuration with local persistence
* Optional **Auth0 login wiring** (via **@auth0/auth0-spa-js**) when credentials are supplied
* **Versions hub** highlighting roadmap milestones and multi-version documentation sidebar

### Installation

{% stepper %}
{% step %}
### Clone the repository

Clone the repository and install any tooling you prefer for static hosting (e.g. **npm install --global wrangler** for **Cloudflare previews**).
{% endstep %}

{% step %}
### Serve the frontend

Point a static server at the **docs/** directory:

```bash
npx http-server docs
```

or use the **Cloudflare Pages** preview command:

```bash
npx wrangler pages dev docs --local --persist
```
{% endstep %}

{% step %}
### Configure environment variables

Configure environment variables for the backend function:

```bash
export CENSYS_API_ID="your-censys-id"
export CENSYS_API_SECRET="your-censys-secret"
```
{% endstep %}

{% step %}
### Run the function

Run the function locally to test its functionality.
{% endstep %}
{% endstepper %}

#### Directory Layout

The project's directory layout is as follows:

```
net-observation-project/
  docs/                 # Frontend assets served by Cloudflare Pages
  functions/api/        # Cloudflare Pages Functions (backend)
  README.md             # Project documentation
  .gitignore            # Common project ignores
```

#### Branding

The project features a stylised textual logo placeholder that is rendered throughout the UI. To add your own branding, simply drop a **logo.png** (preferably 512×512) into the **docs/** directory, and the layout will adopt it automatically.

For more information on the Net Observation Project, please visit the [Censys](https://censys.io/) website or the [Cloudflare Pages](https://pages.cloudflare.com/) documentation. You can also explore the project's \[\[Features]] and \[\[Installation]] instructions in more detail.

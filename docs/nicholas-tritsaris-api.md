## Overview
The nicholas-tritsaris-api repository is a Virtual Portfolio API designed to generate an `openapi.yaml` file in OpenAPI 3.0.3 format from public GitHub repositories and README files. This repository is intended for use with GitBook URL import, allowing the spec to render as a polished, interactive developer portal that refreshes automatically as projects change.

## Features
- **Automated Repository Fetching**: Fetches all public repositories for `Nicholas-Tritsaris` using the GitHub API.
- **README Analysis**: Fetches each repository's `README.md` and uses the Groq API (`llama3-70b-8192`) to analyze each project, generating a professional summary, key features, tech stack used, mock "API responses" for each project, and suggested project-specific subpaths.
- **OpenAPI Compliance**: Builds a single `openapi.yaml` file compliant with **OpenAPI 3.0.3**.
- **Automatic Updates**: Updates the spec automatically with GitHub Actions every 6 hours.

## API Structure
The generated OpenAPI spec documents a portfolio as if it were an API, featuring:
- `GET /profile` — bio, skills, social links (hardcoded in the script).
- `GET /repos` — all public repositories with brief summaries.
- `GET /repos/{name}` — detailed information (summary, tech stack, links) for a specific repo.
- `GET /repos/{name}/*` — AI-generated specific sub-paths for each project based on its README content.

## Repository Layout
The repository is structured as follows:
```text
.
├── .github/
│   └── workflows/
│       └── update-api.yml
├── generate_openapi.py
├── openapi.yaml
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation and Usage
To use this repository, you will need to:
- Add the required repository secrets in **Settings -> Secrets and variables -> Actions**:
  - `GROQ_API_KEY` — your Groq API key.
- To run the generator locally, set the environment variables:
  ```bash
export GROQ_API_KEY="your_groq_api_key"
```
Note that `GITHUB_TOKEN` is provided automatically by GitHub Actions.

## Requirements
- **Groq API Key**: A valid Groq API key is required for analysis and generation of the OpenAPI spec.
- **GitHub Token**: Provided automatically by GitHub Actions for fetching repositories and pushing updates.
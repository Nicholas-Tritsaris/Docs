Lunex is a sleek Windows game launcher and media dashboard built with **WPF** and **.NET 9**. It features *persistent web music playback*, customizable game configurations, automated playtime tracking, and silent background updates. This application is designed to centralize a user's game library, track play statistics, and integrate media playback in a unified interface.

## Overview
Lunex is a modern, high-performance desktop hub and media dashboard designed to provide a sleek command center for launching games, monitoring progress, and enjoying music seamlessly. Built with premium cybernetic aesthetics, it offers a unique user experience.

## Features
*   **Dynamic Game Library**: Manage your local game collection, customize titles, set individual launch arguments, and view cover and icon art.
*   **Persistent Web Media Hub**: Integrated **Chromium**-based music view supporting web players (like **YouTube** and **Spotify**). Media state is persistent, allowing playback to continue uninterrupted while navigating to other views.
*   **Playtime & Usage Tracker**: Automatically monitors and records session durations, total play minutes, and last played timestamps for all games in the library.
*   **Customizable Shell Profiles**: Customize profile details in a central user hub.
*   **Background Self-Updater**: A silent background updater checks for and applies update binaries on application startup, ensuring the shell is always running the latest version.
*   **Single-Instance Architecture**: Automatically detects duplicate launches, prevents multiple processes, and brings the active window to the front.

## Technical Stack & Requirements
Lunex is a native Windows desktop client designed with a lightweight footprint and modern architecture.
*   **Framework**: **WPF** (Windows Presentation Foundation) & Windows Forms
*   **Target Runtime**: **.NET 9.0** (built as a self-contained `win-x64` executable)
*   **Web Engine**: **Microsoft Edge WebView2** (Chromium-based rendering)
*   **System Requirements**: Windows 10 / Windows 11 (64-bit) with **Microsoft Edge WebView2** runtime installed.

## Installation
To install Lunex, ensure your system meets the [system requirements](#technical-stack--requirements). Download the latest version from the official repository and follow the installation instructions.

## Development & Packaging
Authorized developers can compile and package the application using the built-in publishing workflow. For more information, refer to the [official repository](https://github.com/user/lunex) and follow the development guidelines.
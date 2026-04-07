## Summary
WHASOS is a 64-bit operating system for x86-64 (AMD64) architecture, designed to provide a **Windows 7**-like desktop experience. It is a secure, classified-grade operating system project that combines *workplace health and safety compliance infrastructure*, **government-grade access control systems**, *SCP-style anomaly containment documentation*, and **intelligence-agency-inspired secure operating architecture**.

## Overview
WHASOS is a custom operating system that aims to provide a functional operating system architecture with **multi-tier clearance authentication** and a secure documentation system. The project is designed for integration into a high-security game environment and simulates restricted federal infrastructure.

## Features
The key features of WHASOS include:
* A **secure operating architecture** inspired by intelligence agencies
* **Workplace Health and Safety compliance infrastructure**
* **Government-grade access control systems**
* *SCP-style anomaly containment documentation*
* **Multi-tier clearance authentication**

## Installation
To install WHASOS, follow these steps:
1. Build the C components with **Visual Studio 2022** (see [docs/BUILD_VS2022.md](docs/BUILD_VS2022.md))
2. Build the ISO on **Ubuntu 24.04**: `./scripts/build_iso.sh 1.0`
3. Create a **VirtualBox VM** and attach `output/whacos-1.0-amd64.iso`
4. Boot and install or run live

## System Requirements
The build prerequisites for WHASOS include:
* **Ubuntu 24.04 LTS** (or **Debian 12** / **Fedora 40**)
* **sudo/root access**
* ~10 GB free disk space
* Install dependencies: `debootstrap xorriso grub-pc-bin grub-efi-amd64-bin squashfs-tools rsync wget build-essential`

## Project Structure
The WHASOS project structure consists of the following directories:
* `boot/grub/`
* `docs/`
* `scripts/`
* `src/`
	+ `desktop/`
	+ `init/`
	+ `installer/`
	+ `kernel/`
* `output/`

## Access Warning
*Unauthorized access attempts may trigger system lockdown, activity logging, account suspension, simulated prosecution notices, and clearance revocation.* All activity is logged and audited.

## Core Objectives
The core objectives of the WHASOS project are:
* Build a functional operating system architecture
* Implement **multi-tier clearance authentication**
* Create an *SCP-style secure documentation system*
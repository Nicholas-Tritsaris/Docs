# WHASOS

### Summary

WHASOS is a 64-bit operating system for x86-64 (AMD64) architecture, designed to provide a **Windows 7**-like desktop experience. It is a secure, classified-grade operating system project that combines _workplace health and safety compliance infrastructure_, **government-grade access control systems**, _SCP-style anomaly containment documentation_, and **intelligence-agency-inspired secure operating architecture**.

### Overview

WHASOS is a custom operating system that aims to provide a functional operating system architecture with **multi-tier clearance authentication** and a secure documentation system. The project is designed for integration into a high-security game environment and simulates restricted federal infrastructure.

### Features

The key features of WHASOS include:

* A **secure operating architecture** inspired by intelligence agencies
* **Workplace Health and Safety compliance infrastructure**
* **Government-grade access control systems**
* _SCP-style anomaly containment documentation_
* **Multi-tier clearance authentication**

### Installation

{% stepper %}
{% step %}
### Build the C components

Build the C components with **Visual Studio 2022** (see [docs/BUILD\_VS2022.md](/broken/pages/77fa1c427e40a78e5ff59ae1848799283aafe950))
{% endstep %}

{% step %}
### Build the ISO

Build the ISO on **Ubuntu 24.04**: `./scripts/build_iso.sh 1.0`
{% endstep %}

{% step %}
### Create a virtual machine

Create a **VirtualBox VM** and attach `output/whacos-1.0-amd64.iso`
{% endstep %}

{% step %}
### Boot and install

Boot and install or run live
{% endstep %}
{% endstepper %}

### System Requirements

The build prerequisites for WHASOS include:

* **Ubuntu 24.04 LTS** (or **Debian 12** / **Fedora 40**)
* **sudo/root access**
* \~10 GB free disk space
* Install dependencies: `debootstrap xorriso grub-pc-bin grub-efi-amd64-bin squashfs-tools rsync wget build-essential`

### Project Structure

The WHASOS project structure consists of the following directories:

* `boot/grub/`
* `docs/`
* `scripts/`
* `src/`
  * `desktop/`
  * `init/`
  * `installer/`
  * `kernel/`
* `output/`

### Access Warning

{% hint style="warning" %}
Unauthorized access attempts may trigger system lockdown, activity logging, account suspension, simulated prosecution notices, and clearance revocation. All activity is logged and audited.
{% endhint %}

### Core Objectives

The core objectives of the WHASOS project are:

* Build a functional operating system architecture
* Implement **multi-tier clearance authentication**
* Create an _SCP-style secure documentation system_

The Drone-Helmet is a wearable, fully offline "drone" interface designed with hardware-enforced safety features. It is a secure, consent-focused wearable restraint interface that prioritizes user safety and security. The device is equipped with various features, including a local OLED display, audio interface, and solenoid-driven physical lock, to provide a unique and controlled experience.

## Overview
The Drone-Helmet is designed to provide a secure and controlled environment for users, with a focus on consent and safety. The device features a range of hardware components, including a local OLED display, a 3.5mm audio interface, a solenoid-driven physical lock, a torque sensor for engagement, and a battery-health monitoring system. These components work together to provide a seamless and secure experience for users.

## Features
The Drone-Helmet boasts several key safety features, including:
* **Dual-Release Mechanism**: Requires both strap buckle unlatching and mouth-cap removal for device removal, ensuring that the device can only be removed with explicit user consent.
* **Torque Threshold**: Lock only engages when torque ≥ 2.2 N·m is detected, preventing accidental or unauthorized engagement.
* **Battery Safety**: Lock is disabled if battery voltage drops below 3.4 V, ensuring that the device remains safe and functional even in low-power conditions.
* **Fail-Open Design**: Solenoid fails open if power is lost or the controller hangs, providing an additional layer of safety and security.
* **Offline Only**: No cloud, no telemetry, local BLE-only communication, ensuring that user data remains private and secure.

## Installation
To get started with the Drone-Helmet, follow these steps:
1. **Calibration**: Follow the calibration protocol to calibrate the torque sensor and battery monitoring system.
2. **Firmware**: Flash the firmware to an ESP32-WROOM-32 board.
3. **Hardware**: Print and assemble the hardware components according to the provided instructions.
4. **App**: Use the local-only companion app to provide consent and trigger media patterns via the 0xBBBB GATT profile.

## Safety Warning
*ALWAYS* ensure the dual-release mechanism is tested and functional before use. *NEVER* bypass the torque sensor or battery safety checks, as this can compromise the safety and security of the device. By following these guidelines and using the Drone-Helmet responsibly, users can enjoy a unique and controlled experience while prioritizing their safety and security.
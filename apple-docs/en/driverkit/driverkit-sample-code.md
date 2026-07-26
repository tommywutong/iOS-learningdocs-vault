---
title: DriverKit sample code
framework: DriverKit
symbol_kind: article
role: collectionGroup
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/driverkit/driverkit-sample-code
source_url: 'https://developer.apple.com/documentation/driverkit/driverkit-sample-code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/driverkit/driverkit-sample-code.json'
content_hash: 'sha256:2f853649facc4536'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [DriverKit](../driverkit.md)

# DriverKit sample code

Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.

## Overview

The DriverKit SDK provide a stable, secure platform on which to build device drivers for macOS and iPadOS. It provides the interfaces you need to support many types of hardware, including USB devices, HID devices, networking devices, audio devices, and more. Package your custom code in a DriverKit extension, which runs in user space and communicates with the kernel through the framework APIs. To install your DriverKit extension on macOS, deliver it inside an app and install it using the [System Extensions](../systemextensions.md) framework. For projects that run on iPadOS, the system locates the driver in your app bundle and installs the driver for you.

The DriverKit SDK includes several practical examples that show you how to write a typical driver. Use these samples as a starting point to write your own custom drivers. The SDK’s classes provide the base code you need to support standard hardware protocols such as USB, HID, Ethernet, PCI, Thunderbolt, and more. Use your custom driver code to support proprietary features of your hardware devices.

## Topics

### Essentials

- [Communicating between a DriverKit extension and a client app](communicating-between-a-driverkit-extension-and-a-client-app.md) — Send and receive different kinds of data securely by validating inputs and asynchronously by storing and using a callback.

### Audio samples

- [Creating an audio device driver](../audiodriverkit/creating-an-audio-device-driver.md) — Implement a configurable audio input source as a driver extension that runs in user space in macOS and iPadOS.

### HID samples

- [Handling Stylus Input from a Human Interface Device](../hiddriverkit/handling-stylus-input-from-a-human-interface-device.md) — Process stylus-related input from a human interface device and dispatch events to the system.
- [Handling Keyboard Events from a Human Interface Device](../hiddriverkit/handling-keyboard-events-from-a-human-interface-device.md) — Process keyboard-related data from a human interface device and dispatch events to the system.

### Networking samples

- [Connecting a network driver](../pcidriverkit/connecting-a-network-driver.md) — Create an Ethernet driver that interfaces with the system’s network protocol stack.

---
title: Hardware-level interactions
framework: Technology Overviews
symbol_kind: article
role: article
role_heading: ''
platforms: []
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/technologyoverviews/hardware-level-interactions
source_url: 'https://developer.apple.com/documentation/technologyoverviews/hardware-level-interactions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/technologyoverviews/hardware-level-interactions.json'
content_hash: 'sha256:b7f07cd451b1867f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Technology Overviews](../technologyoverviews.md) · [Hardware, networking, and sensors](hardware-networking-sensors.md)

# Hardware-level interactions

Communicate with connected hardware and write code that runs well on Apple silicon.

Apple uses system frameworks to insulate apps from the underlying hardware, but sometimes those frameworks provide only a thin layer between your app and the hardware. Apps can communicate with wired and wireless accessories using industry-standard protocols that the accessory supports. Companies that manufacture accessories can also write custom software drivers to make proprietary features available to their own apps or the system.

Apple silicon provides developers with optimization opportunities for their software. Take advantage of Apple silicon features to improve your code’s performance and power usage.

## Access a connected accessory from your app

The [Made for iPhone (MFi) program](https://mfi.apple.com/) helps you create accessories that incorporate Apple licensed technologies. A hardware manufacturer might use this program to add AirPlay, HomeKit, and other features to an accessory that otherwise supports industry-standard connection and communication protocols.

When someone connects an MFi accessory to their iPhone or iPad using a physical cable or wireless connection, connect to that device using the [External Accessory](../externalaccessory.md) framework. This framework manages the connection to the device, and you choose one of the communication protocols the device supports. Most devices support both industry-standard and manufacturer-specific protocols. For example, a wireless blood pressure cuff might support sending blood pressure data to your app. Choose the appropriate protocol and configure a [communication session](../externalaccessory/easession.md) between your app and the device. Use that session to send commands to the device and retrieve data from it. You can also use the framework to detect when someone [disconnects](../externalaccessory/eaaccessorymanager.md#Managing-Connection-Status-Changes) an accessory.

## Build drivers to support custom hardware features

Macs and iPads provide USB ports for connecting external devices, and some devices support other types of ports. When someone attaches a device to the computer, the system searches for a driver capable of communicating with that device. If you develop custom hardware, create a _driver extension_ (_dext_) to tell the system what services your device offers and how to communicate with it.

To simplify driver development, Apple operating systems contain a set of default drivers capable of communicating with devices that adopt industry-standard protocols. If your device adopts only standard protocols, create a [codeless dext](../kernel/implementing_drivers_system_extensions_and_kexts.md#3616855) to specify the protocols it supports. If your device extends the basic features or adds custom protocols, add code to your dext to support those custom features.

Create dexts for your hardware using the DriverKit SDK, which includes the [DriverKit](../driverkit.md) framework and other frameworks for communicating with specific types of devices. The APIs in these frameworks manage data moving to and from a device. The DriverKit SDK offers support for a variety of protocols, including:

- [Audio](../audiodriverkit.md) or [MIDI](../mididriverkit.md) protocols
- [Block storage](../blockstoragedevicedriverkit.md) protocols
- [Network adapter](../networkingdriverkit.md) protocols
- [USB](../usbdriverkit.md) or [HID](../hiddriverkit.md) protocols
- [PCI](../pcidriverkit.md) protocols
- SCSI [controller](../scsicontrollerdriverkit.md) or [peripheral](../scsiperipheralsdriverkit.md) protocols
- [Serial](../serialdriverkit.md) protocols, including ones over [USB](../usbserialdriverkit.md)

On Mac, you ship drivers as part of an app and [install them](../systemextensions/installing-system-extensions-and-drivers.md) from your code using the [System Extension](../systemextensions.md) framework. On iPad, the system automatically scans for dexts in your app and loads them on demand. Because drivers interact with the kernel, your dexts must contain [entitlements](../driverkit/requesting-entitlements-for-driverkit-development.md) for the system to run them.

> [!important] Important
> Create [codeless dexts](../kernel/implementing_drivers_system_extensions_and_kexts.md#3616855) instead of writing custom driver code whenever possible. Write custom driver code only to support features that are unique to your hardware, and debug your code thoroughly to eliminate crashes. Even minor bugs in drivers can prevent apps from communicating with your hardware or cause other issues.

## Build apps specifically for Apple silicon

Apple devices with [Apple silicon](../apple-silicon.md) integrate the CPU, GPU, Apple Neural Engine (ANE), and memory into a single chip. Apple silicon is available on all Apple devices, making it easy to share code written for one device on other devices.

When building iOS apps, remember that your app can [run unmodified on Macs with Apple silicon](../apple-silicon/running-your-ios-apps-in-macos.md). To create a better experience for people using your app, [update it](../apple-silicon/adapting-ios-code-to-run-in-the-macos-environment.md) to support menus and other features that iPad and Mac use regularly.

If you still have code that runs on Intel-based Macs, [update that code](../apple-silicon/porting-your-macos-apps-to-apple-silicon.md) to run on Apple silicon. Xcode makes it easy to recompile your code for Apple silicon, but you might need to [remove assumptions](../apple-silicon/addressing-architectural-differences-in-your-macos-code.md) you made about the underlying hardware architecture when writing your original code.

When performance is absolutely crucial, [tune your code](../apple-silicon/tuning-your-code-s-performance-for-apple-silicon.md) specifically for Apple silicon. Make sure you’re running the right code and taking advantage of parallel execution when you can. Review the [Apple silicon architecture](../apple-silicon/cpu-optimization-guide.md) to make sure you’re not writing code in a way that hampers performance.

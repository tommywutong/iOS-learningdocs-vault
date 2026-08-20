---
title: Universal Serial Bus Developer Note
apple_id: TP40003026
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2008-04-28'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/HWTech_USB/Introduction/usb_intro.html
archived_at: '2026-07-15T07:41:02.761373Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](USB%20Concepts.md)

# Introduction to Universal Serial Bus Developer Note

Universal Serial Bus (USB) offers several benefits such as low cost, expandability, auto-configuration, and hot-plugging. It also provides power to the bus, enabling many peripherals to operate without the added need for an AC power adapter. Since USB is a cross-platform standard, compliant third-party devices and peripherals are compatible with compliant computers from different manufacturers, differing only in the software required for a specific operating system.

USB 1.1 can operate at 1.5 Megabits per second (Mbps), or 12 Mbps, or both. Typical USB 1.x devices include keyboards, mice, joysticks, game pads, and other low-bandwidth, low-cost devices. On systems with USB 2.0 support, USB can operate at 480 Mbps. Typical USB 2.0 devices include scanners and optical drives.

Developers who are designing peripheral devices that connect to a Macintosh computer via USB will find this document useful.

This document contains the following articles:

- [USB Concepts](USB%20Concepts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmbrfvjvomk7gezdambtgmytcnzz) describes Apple's implementation of the USB standard and defines the key concepts you need to ensure that your USB device is compatible with Macintosh computers that support USB.
- [USB Product-Specific Details](USB%20Product-Specific%20Details.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztsmbsfvjvomk7gezdambtgmytcnzz) provides details specific to particular Macintosh computers.

For specific information about a particular Macintosh computer, see the product Developer Note for that computer in the [Guides > Hardware & Drivers > Apple Hardware](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003576-TP30000519).

For a list of the standard units of measure and abbreviations used in this developer note, refer to the _[Hardware Developer Note Terms and Abbreviations](../Hardware%20Developer%20Note%20Terms%20and%20Abbreviations/Introduction%20to%20Hardware%20Developer%20Note%20Terms%20and%20Abbreviations.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztkmbt)_.

Apple offers the following additional resources for USB:

- _[USB Device Interface Guide](../../Device%20Drivers/USB%20Device%20Interface%20Guide/Introduction%20to%20USB%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzt)_ provides background information and sample code for developing applications to communicate with or control USB devices and interfaces.
- _User-Mode USB Device Arbitration_ provides information about using USB device arbitration.
- _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_ describes the I/O Kit classes (including IOUSBDeviceInterface) that support non-kernel access to I/O Kit objects through the device-interface mechanism.
- The USB Implementers Forum, Inc., website ([www.usb.org](http://www.usb.org/developers/docs/)) has a wealth of documents and tools for implementing USB support, including official specifications, licenses for use of the USB logo, and discussion forums.
[Next](USB%20Concepts.md)


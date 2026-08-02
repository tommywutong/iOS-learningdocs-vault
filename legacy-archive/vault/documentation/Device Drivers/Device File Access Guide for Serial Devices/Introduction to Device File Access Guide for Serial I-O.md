---
title: Device File Access Guide for Serial Devices
apple_id: TP40000972
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2005-12-06'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWSerial/WWSerial_Intro/WWSerial_Intro.html
archived_at: '2026-07-15T07:31:38.534094Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Working%20With%20a%20Serial%20Device.md)

# Introduction to Device File Access Guide for Serial I/O

This document describes how to communicate with a serial device from an application running in OS X. Before you read this document, you should be familiar with the I/O Kit’s device interface mechanism and device matching in particular. To learn about these things, read _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_.

This document contains the following chapters:

- [Working With a Serial Device](Working%20With%20a%20Serial%20Device.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobufvbecsseiffeisq) guides you through a sample application that communicates with a serial device that claims to be a modem.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomzrfvbecsseiffeisq) lists the changes to this document.

Apple developer documentation provides documents that describe various types and aspects of device access.

- _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the I/O Kit (the object-oriented driver-development framework of OS X) and provides an overview of application-level device access.
- _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_ describes many ways applications can access devices and provides in-depth information on the device interface mechanism of the I/O Kit.
- _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_ contains API reference for I/O Kit methods and functions and for specific device families, such as USB.
- _OS X Man Pages_ provides access to existing reference documentation for BSD and POSIX functions and tools in a convenient, HTML format.

If you're ready to create a universal binary version of your serial device-access application to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. That document describes the differences between the Intel and PowerPC architectures and provides tips for developing a universal binary.

A detailed description of the UNIX file system is beyond the scope of this document, but there are many books and websites you can refer to. In particular, you can get information on the POSIX standard at [http://standards.ieee.org](http://standards.ieee.org/).

[Next](Working%20With%20a%20Serial%20Device.md)


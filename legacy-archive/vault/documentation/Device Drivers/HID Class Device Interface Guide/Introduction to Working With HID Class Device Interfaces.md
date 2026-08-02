---
title: HID Class Device Interface Guide
apple_id: TP40000970
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2009-10-19'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/HID/intro/intro.html
archived_at: '2026-07-15T07:31:12.627791Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](USB%20HID%20Overview.md)

# Introduction to Working With HID Class Device Interfaces

The device interface mechanism supported by the I/O Kit gives applications the ability to communicate with hardware from outside the kernel. This document describes how to use the device interface provided by the Human Interface Device (HID) family to access HID class devices (such as keyboards, mice, and uninterruptible power supplies) from applications running on OS X.

You should read this document if you are an application developer who needs to write custom code to communicate with a HID class device from user space.

The document is divided into two main chapters:

- [USB HID Overview](USB%20HID%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzqfvbuqmrqgmwugssbjbcucrsg) provides basic information about HID class devices and the OS X HID Manager.
- [Working With Legacy HID Class Device Interfaces](Working%20With%20Legacy%20HID%20Class%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydcmbvfvkfaoi) briefly outlines the process of accessing a HID class device and then presents a detailed code sample illustrating this process by acquiring access to a joystick.

Although the sample code in this document has been checked for accuracy, it is not intended to meet the needs of a commercial application. For example, error handling is minimal and simply facilitates debugging of this code—you should develop your own techniques for detecting and handling errors. Therefore Apple does not recommend that you directly incorporate the entire sample program into a commercial application.

This document assumes you are familiar with the general I/O Kit and device interface information presented in _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_. In particular, for definitions of I/O Kit terms used in this document such as matching dictionary, family, and driver, see the overview of I/O Kit terms and concepts in the chapter _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_.

A detailed description of the HID class specification is beyond the scope of this document—for more information, including the complete listing of HID usage tables, visit the USB website at [http://www.usb.org](http://www.usb.org/).

For API documentation, see the `IOHIDLib.h` and `IOHIDKeys.h` entries in _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_.

[Next](USB%20HID%20Overview.md)


---
title: Bluetooth Device Access Guide
apple_id: TP30000997
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOBluetooth
published: '2012-06-11'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/Bluetooth/BT_Intro/BT_Intro.html
archived_at: '2026-07-15T07:31:12.604145Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Bluetooth%20Technology%20Basics.md)

# Introduction to Bluetooth Device Access Guide

This document describes how Bluetooth works and summarizes the Bluetooth specification in order to provide a foundation for understanding Apple’s Bluetooth support. It also provides task information, accompanied by several code examples, that illustrates how to develop applications that access Bluetooth enabled devices.

Bluetooth is an open specification that enables low-bandwidth, short-range wireless connections between computers and peripherals, such as mice, cell phones, and personal data assistants (PDAs). The appeal of the Bluetooth model lies in its convenience for wirelessly transferring information and small data files between devices.

Bluetooth is not a networking solution, so it is not a competitor of AirPort, Apple’s wireless networking technology. Nor is it a replacement for the cables needed by high-bandwidth peripherals, such as FireWire. Rather, Bluetooth offers a replacement for IrDA (Infrared Data Association) technology, because it is not constrained by IrDA’s shorter range and line-of-sight requirements.

Because this document comprises conceptual and task information, its audience is broad. This document sets the stage with an overview of Bluetooth technology. Then, it describes how Apple implements the Bluetooth specification and how to access Bluetooth enabled devices on OS X. If you’re unfamiliar with Bluetooth technology in general, you can read this document for a high-level summary. If you’re primarily interested in learning about how Apple implements the Bluetooth specification, you’ll find a thorough description in this document. Finally, if you’re developing applications that communicate with or control Bluetooth enabled devices, you should read this document to discover your options.

Apple provides application-level access to its Bluetooth API in both C and Objective-C, so knowledge of one or the other is important for understanding the code samples. Additionally, the OS X Bluetooth model is at heart an object-oriented one, so familiarity with object-oriented principles is helpful.

This book is divided into three chapters:

- [Bluetooth Technology Basics](Bluetooth%20Technology%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojxfvbuqmrrgqwviubz) describes how Bluetooth works and outlines the Bluetooth protocol stack as defined by the Bluetooth Special Interest Group. If you’re already familiar with Bluetooth technology and the architecture of the protocol stack, you may choose to skip ahead to the next chapter.
- [Bluetooth on OS X](Bluetooth%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojxfvbuqmrrguwviubz) describes the OS X Bluetooth implementation and outlines the services available to you. This chapter provides a foundation for the specific code samples in the last chapter.
- [Developing Bluetooth Applications](Developing%20Bluetooth%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsojxfvbuqmrrgywviubz) describes several common tasks that most Bluetooth applications perform. In addition, it presents a sample application that illustrates how to bring many of these tasks together in a working application. This chapter does not attempt to define the OS X Bluetooth API. For complete API reference, see [Reference > Hardware & Drivers > Bluetooth](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP40003576-TP30000490).

Apple provides comprehensive API reference documentation for its Bluetooth support. For documentation on APIs that support user-space access to Bluetooth devices, see _[Bluetooth Framework Reference](https://developer.apple.com/documentation/iobluetooth)_. For documentation on APIs that support a consistent user interface to Bluetooth services, see _[Bluetooth User Interface Framework Reference](https://developer.apple.com/documentation/iobluetoothui)_.

There are many books that describe Bluetooth technology and the Bluetooth specification. A popular one is _Bluetooth: Connect Without Cables_ by Jennifer Bray and Charles F. Sturman.

To view the Bluetooth specification itself, see [http://www.bluetooth.com](http://www.bluetooth.com/). This site also provides information about the Bluetooth Special Interest Group and the product-qualification program.

See the Apple [Developer Forums](https://developer.apple.com/devforums/) for further discussion of classic Bluetooth development issues.

[Next](Bluetooth%20Technology%20Basics.md)


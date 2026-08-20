---
title: HBA Device Driver Programming Guide
apple_id: TP40003194
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2006-05-23'
source_url: https://developer.apple.com/library/archive/documentation/HardwareDrivers/Conceptual/SCSIHBADrivers/Introduction/Introduction.html
archived_at: '2026-07-15T07:41:09.496017Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](HBA%20Devices%20and%20I-O%20Processing.md)

# Introduction to HBA Device Driver Programming Guide

A host bus adapter (HBA) device driver transmits I/O requests between a computer and a set of storage devices or network nodes. Storage HBA devices can manage sets of parallel SCSI, Fibre Channel, SAS (Serial Attached SCSI), or SATA (Serial ATA) drives, sometimes in combination.

This document provides an overview of HBA device drivers in OS X and explains how they process I/O requests. It also guides you through the development of a custom HBA driver and provides suggestions for increasing its performance.

This document contains the following chapters:

- [HBA Devices in OS X](HBA%20Devices%20and%20I-O%20Processing.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqmznknlte) presents an overview of the way HBA drivers work in OS X and describes how an I/O request travels from an application to the hardware and back again.
- [Developing an HBA Driver](Developing%20an%20HBA%20Driver.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnbnknltm) contains guidelines for implementing a custom HBA driver.
- [Improving Performance](Improving%20Performance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqnjnknltc) describes several things you should take into account when creating an HBA driver to achieve the best performance for your hardware.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaztcojufvbuqmrnknltc) lists the revisions of this document.

The ADC Reference Library contains documents on device driver development for OS X, including sample drivers and API reference.

- _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the architecture of the I/O Kit, the object-oriented framework for developing OS X device drivers.
- _[Mass Storage Device Driver Programming Guide](../../Device%20Drivers/Mass%20Storage%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzu)_ describes how to develop in-kernel device drivers for mass storage devices.
- _[Device Drivers (Kernel/IOKit) Reference](https://developer.apple.com/documentation/kernel)_ contains API reference for I/O Kit methods and functions and for specific device families.
- OS X Man Pages provides access to existing reference documentation for BSD and POSIX functions and tools in a convenient HTML format.
[Next](HBA%20Devices%20and%20I-O%20Processing.md)


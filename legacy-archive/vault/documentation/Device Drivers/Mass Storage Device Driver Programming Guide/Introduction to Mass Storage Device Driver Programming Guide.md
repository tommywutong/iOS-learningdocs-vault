---
title: Mass Storage Device Driver Programming Guide
apple_id: TP40000974
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2007-04-03'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/MassStorage/01_Introduction/Introduction.html
archived_at: '2026-07-15T07:31:28.151278Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Mass%20Storage%20Overview.md)

# Introduction to Mass Storage Device Driver Programming Guide

This document introduces the architecture of the mass storage driver stack and describes how to write in-kernel drivers for mass storage devices and media filter schemes for content on mass storage media. It includes sample code that illustrates how to develop both in-kernel logical unit and protocol services drivers and in-kernel filter-scheme drivers.

Because this book focuses on kernel-resident drivers for mass storage devices that mount file systems or are bootable, it provides only a brief description of application-based drivers for other mass storage devices, such as tape drives. For general information on how to write drivers for such devices, see _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_.

You should read this document if you need to support a mass storage device that mounts a file system or is bootable, or if you need to develop a filter-scheme driver.

Writing drivers for OS X requires the I/O Kit, Apple’s object-oriented framework for driver development. Although this document presents some information on selected I/O Kit principles to provide context for the implementation of the mass storage driver stack, it does not explain these concepts in detail. If you’re not familiar with the I/O Kit, you should read _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ before reading this document.

In addition, if you’ve never written an in-kernel device driver for OS X, you should read _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_ to become familiar with driver fundamentals such as driver life cycle and driver matching and loading.

This document contains the following chapters:

- [Mass Storage Overview](Mass%20Storage%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzufvbeoq2kifbecsq) describes how OS X supports mass storage devices and how the mass storage driver stack is built.
- [Mass Storage Device Compliance](Mass%20Storage%20Device%20Compliance.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzvfvkfawcsivddcmbr) describes the various device specifications with which your device must comply to work with the built-in mass storage device drivers.
- [Mass Storage Driver Matching and Loading](Mass%20Storage%20Driver%20Matching%20and%20Loading.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzwfvbeescjizeuisq) describes the driver matching process for protocol services, logical unit, and filter-scheme drivers.
- [Developing a Universal Binary](Developing%20a%20Universal%20Binary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbxfvjvomi) provides some tips for developing a universal binary version of a logical unit driver, a protocol services driver, and a filter-scheme driver.
- [Subclassing Logical Unit Drivers](Subclassing%20Logical%20Unit%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzxfvjvomi) describes how to subclass a built-in logical unit driver to provide device-specific support.
- [Subclassing Protocol Services Drivers](Subclassing%20Protocol%20Services%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzyfvjvomi) describes how to subclass a built-in protocol services driver to provide device-specific support.
- [Developing a Filter Scheme](Developing%20a%20Filter%20Scheme.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydomzzfvjvomi) describes how to create and test a filter-scheme driver.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbyfvjvomi) lists the revisions of this document.

The ADC Reference Library contains several documents on device driver development for OS X and numerous sample drivers and applications.

- _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ contains tutorials that introduce you to the fundamental techniques you need to develop, debug, and package kernel extensions. This document also contains information on kernel extension loading and dependencies.
- _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the architecture of the I/O Kit, the object-oriented framework for developing OS X device drivers.
- _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_ provides guidelines and tips for developing, debugging, and deploying kernel-resident device drivers.
- _[Kernel Framework Reference](https://developer.apple.com/documentation/kernel)_ contains API reference for I/O Kit methods and functions and for specific families
- [Sample Code > Hardware & Drivers > Storage](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP40003576-TP30001039) includes both application-level and in-kernel code samples.
- OS X Man Pages provides access to existing reference documentation for BSD and POSIX functions and tools in a convenient HTML format.
- The [darwin-drivers](http://lists.apple.com/mailman/listinfo/darwin-drivers) mailing list provides a forum for discussing technical issues related to I/O Kit device driver development.

If you're ready to create a universal binary version of your device driver or filter scheme to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. The _Universal Binary Programming Guidelines_ describes the differences between the Intel and PowerPC architectures and provides tips for developing a universal binary.

The OS X mass storage stack supports mass storage devices that comply with the SCSI Architecture Model SCSI primary commands specification, declare peripheral device types of $00, $05, $07, or $0E, and connect to ATAPI, USB, or FireWire buses. In addition, a USB device must be compliant with the USB mass storage class specification and a FireWire device must be compliant with the FireWire Serial Bus Protocol 2 (SBP-2) specification. The following websites provide more information on these specifications:

- SCSI Architecture Model specifications ([http://t10.org](http://t10.org/))—Provides computer interface and command set specifications and the FireWire Serial Bus Protocol 2 specification.
- ATA/ATAPI standards ([http://t13.org](http://t13.org/))—Provides access to the ATA/ATAPI-5 specification.
- USB specifications ([http://www.usb.org](http://www.usb.org/))—Contains the USB Mass Storage Class Specification Overview.
- FireWire specifications ([http://standards.ieee.org](http://standards.ieee.org/))—Provides access to FireWire standards.

  1394 Trade Association ([http://1394ta.org](http://1394ta.org/))—Provides access to new and draft specifications for the IEEE 1394 standard.
[Next](Mass%20Storage%20Overview.md)


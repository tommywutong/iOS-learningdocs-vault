---
title: SCSI Architecture Model Device Interface Guide
apple_id: TP40000971
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWithSAM/WWS_Intro/WWS_Intro.html
archived_at: '2026-07-15T07:31:38.633293Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Accessing%20SCSI%20Parallel%20Devices.md)

# Introduction to SCSI Architecture Model Device Interface Guide

The I/O Kit provides a device interface mechanism that allows applications to communicate with and control hardware from outside the kernel. This document describes how to access SCSI devices from applications using the SCSI family device interfaces and the SCSI Architecture Model family device interfaces.

This document contains the following chapters:

- [Accessing SCSI Parallel Devices](Accessing%20SCSI%20Parallel%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobwfvjvomi) describes how to use both the SCSI Architecture Model family APIs and the deprecated SCSI family APIs to look up a SCSI Parallel device. It then shows how to access the device using the deprecated SCSI family API. To access a device using the SCSI Architecture Model family API, see [Accessing SCSI Architecture Model Devices](Accessing%20SCSI%20Architecture%20Model%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobxfvjvomi).
- [Accessing SCSI Architecture Model Devices](Accessing%20SCSI%20Architecture%20Model%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobxfvjvomi) describes how to use the SCSI Architecture Model family device interfaces to access and control devices that conform to the SCSI Architecture Model specifications and declare a peripheral device type other than $00, $05, $07, or $0E. This chapter also contains a section on creating a universal binary version of your device access application.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbzfvjvomi) lists the revisions of this document.

The ADC Reference Library contains several documents on device driver development for OS X and numerous sample drivers and applications.

- _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_ describes various ways to access devices from outside the kernel, including the device interface mechanism provided by the I/O Kit. For an overview of the I/O Kit terms and concepts used in this document, read the chapter [Device Access and the I/O Kit](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Device_Access_IOKit/AH_Device_Access_IOKit.html#//apple_ref/doc/uid/TP30000378).
- _[Audio, FireWire, SCSI, Storage, USB Device Access Reference](https://developer.apple.com/documentation/iokit)_ contains API reference for I/O Kit methods and functions and for specific device families.
- [Sample Code > Hardware & Drivers > SCSI](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP40003576-TP30000567) includes both application-level and in-kernel code samples. Of particular relevancy to this document is the _[SCSIOldAndNew](../../../samplecode/SCSIOldAndNew/SCSIOldAndNew.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbuha)_ sample project.
- Additional application-level code samples are included as part of the OS X Developer Tools installation package in `/Developer/Examples/IOKit/scsi`.
- OS X Man Pages provides access to existing reference documentation for BSD and POSIX functions and tools in a convenient HTML format.
- The [ata-scsi-dev](http://lists.apple.com/mailman/listinfo/ata-scsi-dev) mailing list provides a forum for discussing OS X development related to devices based on ATA and SCSI technology.

If you're ready to create a universal binary version of your SCSI device-access application to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. The _Universal Binary Programming Guidelines_ describes the differences between the Intel and PowerPC architectures and provides tips for developing a universal binary.

A detailed description of the SCSI Architecture Model specifications is beyond the scope of this document—for more information, see [http://t10.org](http://t10.org/).

[Next](Accessing%20SCSI%20Parallel%20Devices.md)


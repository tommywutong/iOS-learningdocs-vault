---
title: USB Device Interface Guide
apple_id: TP40000973
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2012-01-09'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/USBBook/USBIntro/USBIntro.html
archived_at: '2026-07-15T07:31:34.706453Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](USB%20Device%20Overview.md)

# Introduction to USB Device Interface Guide

The I/O Kit provides a device interface mechanism that allows applications to communicate with and control hardware from outside the kernel. This document focuses on how to use that mechanism to create an application that detects the attachment of a USB device, communicates with it, and detects its detachment.

This document does not describe how to develop an in-kernel driver for a USB modem or networking device. If you need to do this, refer to the documentation and sample code listed in [See Also](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbtfvkfawcsivddcmbv).

This document contains the following chapters:

- [USB Device Overview](USB%20Device%20Overview.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbufvkfawcsivddcmbr) provides an overview of USB device architecture and terminology and describes how USB devices are represented in OS X.
- [Working With USB Device Interfaces](Working%20With%20USB%20Device%20Interfaces.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbvfvkfawcsivddcmbr) describes how to use the device interface mechanism to create a command-line tool that accesses a USB device.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdmnbwfvjvomi) lists the revisions of this document.

The ADC Reference Library contains several documents on device driver development for OS X and numerous sample drivers and applications.

- _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_ describes various ways to access devices from outside the kernel, including the device interface mechanism provided by the I/O Kit. For an overview of the I/O Kit terms and concepts used in this document, read the chapter [Device Access and the I/O Kit](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Device_Access_IOKit/AH_Device_Access_IOKit.html#//apple_ref/doc/uid/TP30000378).
- _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_ contains API reference for I/O Kit methods and functions and for specific device families.
- [Sample Code > Hardware & Drivers > USB](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP40003576-TP30000583) includes both application-level and in-kernel code samples. Of particular relevance to this document is the application-level sample _[USBPrivateDataSample](../../../samplecode/USBPrivateDataSample/USBPrivateDataSample.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanbvgy)_.
- OS X Man Pages provides access to existing reference documentation for BSD and POSIX functions and tools in a convenient HTML format.
- The [usb](http://lists.apple.com/mailman/listinfo/usb) mailing list provides a forum for discussing technical issues relating to USB devices in OS X.

If you need to develop an in-kernel driver for a USB modem or networking device, refer to the following:

- _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the architecture of the I/O Kit, the object-oriented framework for developing OS X device drivers.
- ADC members can view the AppleUSBCDCDriver project in the source code for OS X v10.3.7 and later, available at [Darwin Releases](http://www.opensource.apple.com/darwinsource/). To find the source code, select a version of OS X equal to or greater than v10.3.7 and click Source (choose the source for the PPC version, if there's a choice). This displays a new page, which lists the open source projects available for the version of OS X you've chosen. Scroll down to AppleUSBCDCDriver and click it to view the source. Be prepared to supply your ADC member name and password.
- Additional code samples that demonstrate specific in-kernel driver programming techniques are included as part of the OS X Developer Tools installation package in `/Developer/Examples/Kernel/IOKit/usb`.

If you're ready to create a universal binary version of your USB device-access application to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. The _Universal Binary Programming Guidelines_ describes the differences between the Intel and PowerPC architectures and provides tips for developing a universal binary.

If you are working with a device that complies with the USB mass storage specification but declares its device class to be vendor specific, see _[Mass Storage Device Driver Programming Guide](../Mass%20Storage%20Device%20Driver%20Programming%20Guide/Introduction%20to%20Mass%20Storage%20Device%20Driver%20Programming%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzu)_ for information on how to ensure the correct built-in driver loads for the device.

Apple provides additional USB information (including the OS X USB Debug Kits) at [http://developer.apple.com/hardwaredrivers/usb/index.html](https://developer.apple.com/hardwaredrivers/usb/index.html).

A detailed description of the USB device specification is beyond the scope of this document—for more information, see _Universal Serial Bus Specification Revision 2.0_ available at [http://www.usb.org](http://www.usb.org/).

[Next](USB%20Device%20Overview.md)


---
title: FireWire Device Interface Guide
apple_id: TP40000969
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WorkingWFireWireDI/FWDevIntro/FWDevintro.html
archived_at: '2026-07-15T07:31:34.791298Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](FireWire%20on%20OS%20X.md)

# Introduction to FireWire Device Interface Guide

The I/O Kit device interface mechanism provides applications with a means of communicating with hardware from outside the kernel. To communicate with FireWire devices, OS X provides several device interfaces that are specific to different protocols and different types of communication. This document describes the range of device interfaces available in OS X that your application can use to control a FireWire device or unit.

You should read this document if you are developing an application that needs to communicate with or control a FireWire device. Although this document describes how OS X supports FireWire devices in the kernel, it does not describe how to develop in-kernel drivers for them.

Before you read this document, you should be familiar with the I/O Kit and the device interface mechanism it provides. To learn more about the I/O Kit in general and device interfaces in particular, see the documents listed in [See Also](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqguwuescdizcuussg).

A detailed description of the FireWire specification is beyond the scope of this document—for more information see the 1394 Trade Association website at [http://www.1394ta.org](http://www.1394ta.org/).

This document contains the following chapters:

- [FireWire on OS X](FireWire%20on%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgewviucykjcummjqge) gives a brief overview of FireWire, presents basic information about in-kernel OS X support for FireWire devices, and describes the three device interface libraries the IOFireWire family provides.
- [Accessing FireWire Devices From Applications](Accessing%20FireWire%20Devices%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgiwviucykjcummjqge) describes the process of communicating with FireWire devices from applications, from finding the device or unit in the I/O Registry to getting the appropriate device interface.
- [Using the FireWire Device Interface Libraries](Using%20the%20FireWire%20Device%20Interface%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwviucykjcummjqge) uses specific code examples to explain how to use some of the IOFireWire family’s device interfaces.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgywugskiinauqrkc) lists the changes to this document.

The chapter [Using the FireWire Device Interface Libraries](Using%20the%20FireWire%20Device%20Interface%20Libraries.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrzfvbuqmrqgmwviucykjcummjqge) uses projects in the FireWire SDK as a code base. The latest version of the SDK is available for download at [http://developer.apple.com/hardwaredrivers/download](https://developer.apple.com/hardwaredrivers/download). The complete SDK contains a large number of samples covering many different kinds of hardware access from applications in a variety of programming languages (Objective-C using the Cocoa framework, C, and C++). In the interests of brevity, this document includes only fragments of some of the projects to illustrate the concepts it describes. Refer to the SDK for the complete versions of the code fragments used, in addition to other projects not described here.

Apple developer documentation includes several documents that cover device access and the I/O Kit. Some of these documents are listed below.

- _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_
- _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_
- _[I/O Kit Framework Reference](https://developer.apple.com/documentation/iokit)_

In addition to these documents, Apple maintains a website devoted to FireWire on OS X, with links to the SDK and related topics, at [http://developer.apple.com/hardwaredrivers/firewire](https://developer.apple.com/hardwaredrivers/firewire).

Apple provides a FireWire mailing list on which you can post questions and discuss issues of interest to the FireWire community. You can also search the archives for helpful information. You can subscribe to the FireWire mailing list at [http://lists.apple.com/mailman/listinfo/firewire](http://lists.apple.com/mailman/listinfo/firewire).

If you’re ready to create a universal binary version of your FireWire device-access application to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. The _Universal Binary Programming Guidelines_ describes the differences betweeen the Intel and PowerPC architectures and provides tips for developing a universal binary.

[Next](FireWire%20on%20OS%20X.md)


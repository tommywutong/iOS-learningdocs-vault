---
title: Accessing Hardware From Applications
apple_id: TP30000376
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2007-02-08'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/AccessingHardware/AH_Intro/AH_Intro.html
archived_at: '2026-07-15T07:31:09.117754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Hardware-Access%20Options.md)

# Introduction to Accessing Hardware From Applications

There are many reasons your application might need to access hardware: Receiving mouse and keyboard events, accessing devices, such as a FireWire DV camcorder, and driving a device from an application are just a few. Although only code that resides in the kernel can access hardware directly, OS X provides many services that allow you to communicate with hardware from plug-ins, applications, shared libraries, and other code running outside the kernel.

This document describes how software running in OS X can access hardware by communicating with the kernel, focusing on services the I/O Kit provides to develop an application-based driver. You should read this document if you need to access a device from an application. Note that many applications will be able to handle all their hardware-access needs using high-level APIs, such as Open Transport and QuickTime, that are available through Carbon and Cocoa. To help you determine which approach is right for you, and for a summary of other services OS X provides for hardware access from applications, see [Hardware-Access Options](Hardware-Access%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvbecsseiffeisq).

This document includes many code fragments illustrating the various tasks involved in developing an application that accesses hardware, but it is not intended to be a step-by-step cookbook for accessing a particular type of device. To determine how to access a particular device, see [I/O Kit Family Device-Access Support](I-O%20Kit%20Family%20Device-Access%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojtfvbecqsdinbessq); For each device family it specifies how to access a device in that family and where to find more detailed documentation.

This document does _not_ describe how to write kernel-resident code to access hardware. Kernel programmers should refer to _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ and in-kernel device-driver developers should read _[IOKit Device Driver Design Guidelines](../IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_. In particular, if you are developing your own device interface and user client to create a custom solution to access your device, you should read the [Making Hardware Accessible to Applications](https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/MakingHWAccessible/MakingHWAccessible.html#//apple_ref/doc/uid/TP30000698) chapter in that document. For other documents that cover how to access particular devices, visit [Reference Library > Hardware & Drivers](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40003576-TP30000511).

_Accessing Hardware From Applications_ includes the following chapters:

- [Hardware-Access Options](Hardware-Access%20Options.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzxfvbecsseiffeisq)

  Describes many other methods you can use to access hardware from an application, such as Core Audio, QuickTime, and the Carbon Event Manager. Read this chapter to determine if such high-level APIs can meet your needs.
- [Device Access and the I/O Kit](Device%20Access%20and%20the%20I-O%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzyfvbecsseiffeisq)

  Summarizes I/O Kit architecture, providing a list of terms used throughout this document and describing how the I/O Kit models I/O connections. It then describes the two fundamental hardware-access methods the I/O Kit supports: device interfaces and device files.
- [Finding and Accessing Devices](Finding%20and%20Accessing%20Devices.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzzfvbecsseiffeisq)

  Describes the steps you take to access a device using an I/O Kit device interface and, for appropriate devices, using a device file.
- [The IOKitLib API](The%20IOKitLib%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobqfvbecsseiffeisq)

  Categorizes and describes the functions of the main API that supports user-space device access through the I/O Kit.
- [Handling Errors](Handling%20Errors.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobrfvbecsseiffeisq)

  Describes how to interpret I/O Kit return values and provides information on the exclusive-access error.
- [I/O Kit Family Device-Access Support](I-O%20Kit%20Family%20Device-Access%20Support.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojtfvbecqsdinbessq)

  Lists the current I/O Kit families and describes what support they provide for hardware access from applications.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdomjvfvbecsseiffeisq)

  Lists changes to this document.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgobtfvkfami)

  Defines key terms used in this document.

Although this document includes a summary of basic I/O Kit information (in [I/O Kit Summary](Device%20Access%20and%20the%20I-O%20Kit.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzyfvbuuqkijffemsi)), you should read _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ for a thorough understanding of this subsystem.

Familiarity with the CFPlugIn architecture is useful in reading this document. This architecture is described in the developer documentation available in [Reference Library > Core Foundation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000421-TP30000511).

Knowledge of the OS X kernel and device drivers may be useful but is not required. To get more information about these topics, visit [Reference Library > Darwin](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000422-TP30000511).

When you install the Developer package, you get developer documentation as well as tools and example code. You can find all the I/O Kit and kernel documents mentioned in this document listed in `/Developer/ADC Reference Library/documentation/Darwin` and `/Developer/ADC Reference Library/documentation/HardwareDrivers`. Sample projects are available in `/Developer/Examples`. Most of the sample projects that are relevant to device access from applications reside in `/Developer/Examples/IOKit`.

There you can view the documentation for BSD and POSIX functions and tools by typing `man` _function_name_ in a Terminal window (for example, `man gdb`) or in HTML at OS X Man Pages.

You can access reference documentation on I/O Kit families from Xcode, Help Viewer, and [Reference Library > Hardware & Drivers](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40003576-TP30000511). Of course, you can also browse the header files for various I/O Kit families and other I/O Kit services accessible from user space in `/System/Library/Frameworks/IOKit.framework/Headers`.

[Next](Hardware-Access%20Options.md)


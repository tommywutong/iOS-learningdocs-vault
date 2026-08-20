---
title: IOKit Device Driver Design Guidelines
apple_id: TP30000694
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-08-14'
source_url: https://developer.apple.com/library/archive/documentation/DeviceDrivers/Conceptual/WritingDeviceDriver/Introduction/Intro.html
archived_at: '2026-07-15T07:31:49.422193Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](The%20libkern%20C%2B%2B%20Runtime.md)

# Introduction to I/O Kit Device Driver Design Guidelines

To create and deploy an I/O Kit device driver requires a range of knowledge and skills, some of which seem only remotely connected to the business of writing driver code. For example, you need to package the driver for installation. You may need to localize text and images associated with the driver and display dialogs when user intervention is necessary. And unless the code you write is always perfect when first typed, you’ll need to debug your driver.

This document describes various tasks that driver writers commonly perform. It is intended as a kind of “sequel” to _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_. Whereas that document is primarily conceptual in nature—describing such things as the I/O Kit architecture and families, event handling, and memory and power management—this document takes a more practical approach. It is a collection of sundry topics related to writing, debugging, testing, and deploying I/O Kit device drivers.

If you are developing a device driver to run in OS X, you should read this document. Because this document assumes familiarity with basic I/O Kit concepts and terminology, it’s a good idea to read _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ first. It also helps to be familiar with object-oriented programming in general, and C++ programming specifically.

If you need to develop an application that accesses a device, you should read instead _[Accessing Hardware From Applications](../Accessing%20Hardware%20From%20Applications/Introduction%20to%20Accessing%20Hardware%20From%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydgnzw)_ for more information on various ways to do that. If this sounds like a good solution for you, be aware that Objective-C does not provide interfaces for I/O Kit or BSD APIs. However, because these are C APIs, you can call them from a Cocoa application.

_I/O Kit Device Driver Design Guidelines_ has the following chapters:

- [The libkern C++ Runtime](The%20libkern%20C%2B%2B%20Runtime.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojvfvbecssjijdeiri)

  Describes the libkern library’s runtime typing system and the role of the OSMetaClass in it. It also describes techniques for object creation and destruction, dynamic casting, object introspection, and binary compatibility.
- [libkern Collection and Container Classes](libkern%20Collection%20and%20Container%20Classes.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojwfvbecqsejbdeusq)

  Describes what the libkern collection and container classes are and how to use them. It includes code samples showing how your driver can use these classes to configure itself during runtime.
- [The IOService API](The%20IOService%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojxfvbucq2jirduery)

  Provides an overview of the methods and types defined in IOService, the base class for all I/O Kit drivers. It includes descriptions of the methods for driver matching, sending and receiving notifications, client and provider messaging, power management, memory mapping, and interrupt handling. This chapter is an indispensable resource for those developing their own I/O Kit families or familyless drivers.
- [Making Hardware Accessible to Applications](Making%20Hardware%20Accessible%20to%20Applications.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojyfvbeeq2djjceksa)

  Starts by discussing issues related to the transfer of data between a driver and a user-space program and summarizing the various approaches for doing so. It then describes one of the approaches: Custom user clients. It gives an overview of user-client architecture and points out factors affecting the design of user clients. Finally, it describes how to implement both sides of a user client: The IOUserClient subclass in the kernel and the library in user space.
- [Kernel-User Notification](Kernel-User%20Notification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmojzfvbecssjjfauosq)

  Describes how you can use the Kernel–User Notification Center to present users with localized dialogs (blocking and non-blocking), launch user-space executables (including specific preference panes of System Preferences), and load sophisticated and localized user interfaces from bundles.
- [Displaying Localized Information About Drivers](Displaying%20Localized%20Information%20About%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombqfvbeeq2kjbbeqqq)

  Summarizes the steps for internationalizing the bundles known as kernel extensions and describes how to access the localized resources in these bundles from user space.
- [Debugging Drivers](Debugging%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombrfvbeeq2gijfeusi)

  A collection of tips and techniques for debugging I/O Kit device drivers. It discusses (among other things) debugging drivers during the matching and loading stages, setting up for two-machine debugging, using the kernel debugging macros, logging techniques, and debugging panics and system hangs.
- [Testing and Deploying Drivers](Testing%20and%20Deploying%20Drivers.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombsfvbegskfiveemry)

  Discusses strategies for driver testing and offers guidance on packaging and deploying device drivers.
- [Developing a Device Driver to Run on an Intel-Based Macintosh](Developing%20a%20Device%20Driver%20to%20Run%20on%20an%20Intel-Based%20Macintosh.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmbqfvjvomi)

  Provides tips for developing an in-kernel device driver to run in either a PowerPC-based or Intel-based Macintosh computer.
- [Document Revision History](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdqmbrfvbecsseiffeisq)

  Lists changes to this document.
- [Glossary](Glossary.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydombtfvkfami)

  Defines key terms used in this document.

In addition to _I/O Kit Device Driver Design Guidelines_, Apple developer documentation includes several documents that cover the OS X kernel, the I/O Kit in general, and driver development for specific devices. Some of these documents are listed below.

- _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ describes at a high level the architecture and facilities of the OS X core operating system, including Mach, BSD, the Virtual File System, networking, virtual memory, and kernel services. In addition, it discusses topics of interest to kernel programmers, such as performance, security, and coding conventions.
- _[IOKit Fundamentals](../IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ describes the features, architecture, classes, and general mechanisms of the I/O Kit and includes discussions of driver matching and loading, event handling, memory management, and power management.
- _[Kernel Extension Programming Topics](../../Darwin/Kernel%20Extension%20Programming%20Topics/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrt)_ contains a collection of tutorials that introduce you to the development tools and take you through the steps required to create, debug, and package kernel extensions and I/O Kit drivers. It also includes information on other aspects of kernel extensions.
- Documentation that provides in-depth information on writing drivers for specific device families is available in Hardware & Drivers Reference Library.

In addition to these Apple publications, you can browse the BSD man pages for more information on BSD and POSIX APIs. You can view the documentation for BSD and POSIX functions and tools by typing `man`_function_name_ in a Terminal window (for example, `man gdb`) or in HTML at _OS X Man Pages_.

Of course, you can always browse the header files shipped with the I/O Kit, which are installed in `Kernel.framework/Headers/iokit` (kernel-resident) and `IOKit.framework/Headers` (user-space).

You can also view developer documentation in Xcode. To do this, select Help from the Xcode menu and then click Show Documentation Window.

If you're ready to create a universal binary version of your device driver to run in an Intel-based Macintosh, see _[Universal Binary Programming Guidelines, Second Edition](../../Mac%20OSX/Universal%20Binary%20Programming%20Guidelines%2C%20Second%20Edition/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdemjx)_. The _Universal Binary Programming Guidelines_ describes the differences between the Intel and PowerPC architectures and provides tips for developing a universal binary.

Apple maintains several websites where developers can go for general and technical information on Darwin and OS X.

- The Darwin Open Source site ([http://developer.apple.com/darwin/](https://developer.apple.com/darwin/)) contains information and resources for Darwin and other open-source projects maintained by Apple.
- Apple Developer Connection: OS X ([http://developer.apple.com/devcenter/mac](https://developer.apple.com/devcenter/mac)) offers SDKs, release notes, product notes and news, and other resources and information related to OS X.
- The AppleCare Support site ([http://www.apple.com/support](http://www.apple.com/support)) provides a search feature that enables you to locate technical articles, manuals, specifications, and discussions on OS X and other areas.
[Next](The%20libkern%20C%2B%2B%20Runtime.md)


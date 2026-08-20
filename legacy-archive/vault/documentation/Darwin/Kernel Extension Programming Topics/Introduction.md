---
title: Kernel Extension Programming Topics
apple_id: TP40001063
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2010-09-01'
source_url: https://developer.apple.com/library/archive/documentation/Darwin/Conceptual/KEXTConcept/KEXTConceptIntro/introduction.html
archived_at: '2026-07-15T07:23:07.339601Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md)

# Introduction

A __kernel extension__ (or __kext__) is a dynamically loaded bundle of executable code that runs in kernel space. You can create a kext to perform low-level tasks that cannot be performed in user space. Kexts typically belong to one of three categories:

- Low-level device drivers
- Network filters
- File systems

This document is a primary resource for kext programming in OS X. It describes the structure of a kext and demonstrates the process for developing a kext, from creating an Xcode project to packaging your kext for distribution.

This document is intended for developers who are developing a kernel extension for OS X. Because kext development has numerous pitfalls, you are encouraged to stay away from creating a kext unless you absolutely have to. Read [Deciding Whether to Create a Kernel Extension](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrzfvjvomi) to make sure a kext is the correct solution for your needs.

If you are developing a driver for a USB or FireWire device, it can and should run in user space. See _[USB Device Interface Guide](../../Device%20Drivers/USB%20Device%20Interface%20Guide/Introduction%20to%20USB%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnzt)_ and _[FireWire Device Interface Guide](../../Device%20Drivers/FireWire%20Device%20Interface%20Guide/Introduction%20to%20FireWire%20Device%20Interface%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaydsnrz)_ for details.

This document contains the following chapters:

- [Deciding Whether to Create a Kernel Extension](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tgnrzfvjvomi) explains when it is absolutely necessary to create a kext, along with safer, simpler alternatives for common issues.
- [The Anatomy of a Kernel Extension](The%20Anatomy%20of%20a%20Kernel%20Extension.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dilkdjfeeuqsdjfca) describes the components of a kext bundle.
- [Creating a Generic Kernel Extension with Xcode](Creating%20a%20Generic%20Kernel%20Extension%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dklkcifbeuscdjjaq) guides you through creating a simple generic kext.
- [Creating a Device Driver with Xcode](Creating%20a%20Device%20Driver%20with%20Xcode.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dmlkdjfeekq2ijbcq) guides you through creating a simple I/O Kit device driver.
- [Debugging a Kernel Extension with GDB](Debugging%20a%20Kernel%20Extension%20with%20GDB.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dolkdjbcesscgireq) guides you through debugging a kernel extension with GDB.
- [Command-Line Tools for Analyzing Kernel Extensions](Command-Line%20Tools%20for%20Analyzing%20Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tinjvfvjvomi) describes command-line tools you can use when working with kexts.
- [Packaging a Kernel Extension for Distribution and Installation](Packaging%20a%20Kernel%20Extension%20for%20Distribution%20and%20Installation.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgiydambsgm3dqlkdjbcegqsdjjaq) guides you through using the Package Maker application to package your kext.
- [Info.plist Properties for Kernel Extensions](Info.plist%20Properties%20for%20Kernel%20Extensions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4tiobrfvjvomi) describes kext-specific properties for your kext’s information property list.

- _[Kernel Programming Guide](../Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_ provides fundamental high-level information about the OS X core operating-system architecture.
- _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ explains the terminology, concepts, architecture, and basic mechanisms of the I/O Kit.
- _[IOKit Device Driver Design Guidelines](../../Device%20Drivers/IOKit%20Device%20Driver%20Design%20Guidelines/Introduction%20to%20I-O%20Kit%20Device%20Driver%20Design%20Guidelines.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydmoju)_ describes common tasks to perform when creating an I/O Kit driver.
[Next](Deciding%20Whether%20to%20Create%20a%20Kernel%20Extension.md)


---
title: IOPrintSuperClasses
apple_id: DTS10000447
resource_type: Sample Code
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: IOKit
published: '2005-08-17'
source_url: https://developer.apple.com/library/archive/samplecode/IOPrintSuperClasses/Introduction/Intro.html
archived_at: '2026-07-18T03:12:05.471691Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](IOPrintSuperClasses.c.md)

# IOPrintSuperClasses

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-08-17 Updated to produce a universal binary. No code changes were required. Separately, updated to use IOObjectCopySuperclassForClass, which was introduced in Mac OS X 10.4. |
| __Build Requirements:__ | Xcode 2.1 |
| __Runtime Requirements:__ | Mac OS X 10.2 or later |

The sample is a trivial example of using the I/O Kit registry, but it also represents a useful tool for exploring the I/O Kit class hierarchy. Given the name of a class, this tool will print all of the super-classes of that class. For example, if you ask it for the super-classes of IOUSBInterface, the tool will print IOUSBNub, IORegistryEntry, IOService, and OSObject.

[Next](IOPrintSuperClasses.c.md)


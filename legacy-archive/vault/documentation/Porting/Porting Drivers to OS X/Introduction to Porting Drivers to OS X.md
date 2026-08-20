---
title: Porting Drivers to OS X
apple_id: TP30001169
resource_type: Guide
platform: macOS
topic: Drivers, Kernel, & Hardware
technology: Kernel
published: '2009-05-06'
source_url: https://developer.apple.com/library/archive/documentation/Porting/Conceptual/PortingDrivers/intro/intro.html
archived_at: '2026-07-18T01:50:43.073768Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Driver%20Porting%20Basics.md)

# Introduction to Porting Drivers to OS X

This book was intended to be used by developers who have existing drivers for other platforms, particularly classic Mac OS and other UNIX-based operating systems. Its goal is to provide you with useful ways to port these non-I/O Kit drivers to OS X with minimal reengineering.

Before you begin porting a device driver to OS X, you should read _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_.

This book is only relevant if you are porting a driver that resides in the kernel. To find out if this applies to your driver, read [Does Your Driver Belong in the Kernel?](Driver%20Porting%20Basics.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytcnrzfvbuqmrqguwueqkkjfeuirci).

For information on specific technology areas, you should consult the appropriate API reference in the I/O Kit section of Apple’s Technical Publications website.

For more information on the OS X Kernel and the I/O Kit, see the books _[IOKit Fundamentals](../../Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi)_ and _[Kernel Programming Guide](../../Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv)_.

For more information on driver porting, two good sources of information are the _Darwin-drivers_ and _Darwin-development_ mailing lists. For more information, visit [http://www.lists.apple.com](http://www.lists.apple.com/).

[Next](Driver%20Porting%20Basics.md)


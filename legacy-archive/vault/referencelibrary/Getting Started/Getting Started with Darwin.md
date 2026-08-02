---
title: Getting Started with Darwin
apple_id: TP30001006
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-01-06'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Darwin/_index.html
archived_at: '2026-07-18T02:39:21.321226Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Mac OS X is a UNIX-based operating system with modern GUI and application support frameworks layered on top. The lowest layer, Darwin, includes the kernel, device drivers and driver support frameworks, a BSD personality layer, and various libraries and command-line utilities.

The Darwin layers of Mac OS X are open source. This serves two main purposes: to provide a resource for other open source development efforts (such as Linux and BSD variants) to make their software available on Mac hardware and to provide source code to aid developers writing device drivers and other low-level technologies for Mac OS X.

In addition to being part of Mac OS X, Darwin is a standalone, BSD-based operating system. (BSD, short for Berkeley Software Distribution, is a family of UNIX variants descended from Berkeley’s version of UNIX.)

Darwin is also occasionally used to refer to the Darwin Streaming Server, also known as the QuickTime Streaming Server (QTSS). For more information on QTSS, see the [QuickTime Streaming Documentation](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000433-TP30000577).

### Start Here

For more information about how Darwin fits into Mac OS X, you should read [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx).

For a better understanding of Darwin as a standalone operating system, you should read a book on system administration, such as [UNIX System Administration Handbook](http://www.amazon.com/UNIX-System-Administration-Handbook-3rd/dp/0130206016/) by Nemeth and others.

### Choose a Learning Path

There are five primary areas of learning related to Darwin: the kernel and device drivers, tools, porting, the Darwin OS components, and system administration.

#### The Kernel and Device Drivers

The first thing you should do before starting to write a device driver is to find out whether your driver should be in the kernel or not. Many drivers and other services are traditionally provided outside the kernel in Mac OS X. The document Should You Program in the Kernel? explains how to decide whether your driver or service needs to be in the kernel.

- [Getting Started with Hardware and Drivers](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_HardwareDrivers/_index.html#//apple_ref/doc/uid/TP40003522) to learn about resources of interest to device driver programmers.
- [Kernel Programming Guide](../../documentation/Darwin/Kernel%20Programming%20Guide/About%20This%20Document.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsmbv) to learn about non-driver programming in the kernel. This canonical document contains some information that may be helpful for driver writers, but is primarily intended for people developing other technologies.
- [IOKit Fundamentals](../../documentation/Device%20Drivers/IOKit%20Fundamentals/Introduction%20to%20I-O%20Kit%20Fundamentals.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridambqgaydcmi) to get a general overview of the I/O Kit.

#### Tools

To learn about Apple’s tools, including its open source tools, read [Tools & Languages Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102).

#### Porting

To learn about porting software to Mac OS X, read Getting Started With Porting. If you are planning to port a 64-bit tool to Mac OS X, or if you plan to transition a 32-bit command-line tool to a 64-bit environment, read [64-Bit Transition Guide](../../documentation/Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru).

#### The Darwin OS Components

Look at the [Open Source](https://developer.apple.com/opensource/) topic page to learn about Apple-created open source technologies.

#### System Administration

To learn about system administration, look at the ADC topic page for [Mac OS X](https://developer.apple.com/macosx/). For additional information about security, including documentation on Mac OS X's support for access control lists (ACLs), see [Security Overview](../../documentation/Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw).

### Next Steps

The [Darwin Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP30000422) includes the following high-level resource pages, which can be bookmarked for easy access.

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP30000422)

  Conceptual and how-to information for Darwin technologies.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP30000422)

  Focused, detailed descriptions in reference format for Darwin technologies.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP30000422)

  Sample applications demonstrating various Darwin technologies.
- [Technical Notes](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000924-TP30000422)

  Late-breaking documents on issues related to Darwin.
- [Technical Q&As](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000926-TP30000422)

  Programming tips, code snippets, and FAQs by Apple’s support engineers.
- Mailing Lists

  There are numerous mailing lists available to discuss Darwin topics with other developers. To discuss Darwin software development, join [darwin-development](http://lists.apple.com/mailman/listinfo/darwin-development). Other, more specialized Darwin lists of interest include [darwin-documentation](http://lists.apple.com/mailman/listinfo/darwin-documentation) (for discussion pertaining to Darwin documentation), [darwin-drivers](http://lists.apple.com/mailman/listinfo/darwin-drivers) (on Darwin hardware drivers), [darwin-kernel](http://lists.apple.com/mailman/listinfo/darwin-kernel) (on the Darwin Mach+BSD kernel, [darwin-userlevel](http://lists.apple.com/mailman/listinfo/darwin-userlevel) (on Darwin user-level software), and [darwin-x86](http://lists.apple.com/mailman/listinfo/darwin-x86) (on Darwin on the x86 platform).

  For discussion on the QuickTime Streaming Server, join the mailing list for developers ([streaming-server-developers](http://lists.apple.com/mailman/listinfo/streaming-server-developers)) or users ([streaming-server-users](http://lists.apple.com/mailman/listinfo/streaming-server-users)). To get announcements of key events and milestones for Apple’s open source projects, join [publicsource-announce](http://lists.apple.com/mailman/listinfo/publicsource-announce), and to get announcements of open source software submissions, join [publicsource-modifications](http://lists.apple.com/mailman/listinfo/publicsource-modifications). For software development discussion about OpenPlay and NetSprockets, join [openplay-development](http://lists.apple.com/mailman/listinfo/openplay-development).

These additional websites may also be helpful:

- [Darwin](https://developer.apple.com/darwin/)

  Apple’s Darwin topic page.
- [Open Source Technologies](http://www.apple.com/opensource/)

  Apple’s open source technologies website.
- [FreeBSD](http://www.freebsd.org/)

  Information about FreeBSD, upon which much of Darwin is based.
- [Single UNIX Specification](http://www.opengroup.org/products/publications/catalog/un.htm)

  Documentation on UNIX standards.
- [Mac OS Forge](http://www.macosforge.org/)

  A community-driven website about various open source projects.


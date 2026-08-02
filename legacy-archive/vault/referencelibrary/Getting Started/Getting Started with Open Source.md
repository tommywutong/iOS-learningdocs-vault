---
title: Getting Started with Open Source
apple_id: TP40003840
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2009-05-06'
source_url: https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_OpenSource/_index.html
archived_at: '2026-07-18T02:39:25.974982Z'
---
> 导航：[总目录](../../README.md) · [referencelibrary](../../_indexes/referencelibrary.md)



## Introduction

### Technology Overview

Open Source means many things to many people. To some, it is software whose source code is available to the people who use it. To others, it is a philosophy of writing source code that can be reused freely. To still others, it is a group of software licenses that meet certain criteria for openness. In general, though, it refers to software licensed under a broad range of licenses, all sharing one common characteristic: the source code is available for anyone to see, inspect, and modify.

Mac OS X contains many open source tools and technologies, including third-party tools that are built and packaged with the operating system, as well as fundamental parts of the operating system itself. If you haven’t already done so, you should read the ADC topic page for [Open Source](https://developer.apple.com/opensource/).

### Start Here

Before porting or writing open source software for Mac OS X, read [Mac Technology Overview](../../documentation/Mac%20OSX/Mac%20Technology%20Overview/About%20Developing%20for%20Mac.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanrx) to help you understand how open source software fits into Mac OS X and to familiarize yourself with the Mac OS X environment as a whole.

If you need to familiarize yourself with the UNIX-based underpinnings of Mac OS X, read a book on system administration, such as [UNIX System Administration Handbook](http://www.admin.com/) by Nemeth and others. In addition, you may find Mac OS X Man Pages helpful in understanding the details of Mac OS X command-line tool syntax and UNIX-based C API interfaces.

### Choose a Learning Path

If you are an open source developer, you need to understand the Mac OS X programming environment. If you are a high-performance/scientific computing user or developer, you need to understand what high-performance computing technologies are available to you. If you are a system administrator, you need to understand how administering Mac OS X systems differs from administering other UNIX-based systems.

#### Porting and Developing Applications

Before you port or develop an open source application on Mac OS X, you need to learn about the differences between Mac OS X and other operating systems that you already support. Two good starting points are [Porting UNIX/Linux Applications to OS X](../../documentation/Porting/Porting%20UNIX-Linux%20Applications%20to%20OS%20X/Introduction%20to%20Porting%20UNIX-Linux%20Applications%20to%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytambt) and [Porting to Mac OS X from Windows Win32 API](../../documentation/Porting/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API/Porting%20to%20Mac%20OS%20X%20from%20Windows%20Win32%20API.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpgeydambqge4ta2i).

If you are planning to port a 64-bit tool to Mac OS X or transition a 32-bit command-line tool to a 64-bit environment, read [64-Bit Transition Guide](../../documentation/Darwin/64-Bit%20Transition%20Guide/Introduction%20to%2064-Bit%20Transition%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytanru).

#### Using and Developing High-Performance and Scientific Computing Technology

If you are a high-performance computing user or developer looking for information about high-performance computing, read [Tools & Languages Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102), then read the ADC topic page for [high-performance computing](https://developer.apple.com/hardware/hpc/).

#### Administering Mac OS X Workstations and Servers

If you are a system administrator interested in open source technologies in Mac OS X, you should learn about the technology areas that interest you.

- __If you’re looking for general information about system administration issues__, look at the ADC topic page for [Mac OS X Server](https://developer.apple.com/server/).
- __If you’re interested in Apple open source technologies__, look at the Apple [Open Source](https://developer.apple.com/opensource/) website and the [Mac OS Forge](http://www.macosforge.org/) website.
- __If you’re interested in open source database technologies in Mac OS X__, go to the web sites for [SQLite](http://www.sqlite.org/) and [MySQL](http://www.mysql.org/).
- __If you're interested in shared authentication across multiple computers__, see the ADC topic page for [Directory Services](https://developer.apple.com/opensource/dirservices/).
- __If you’re interested in Apple’s tools__, including its open source tools, read [Tools & Languages Starting Point](https://developer.apple.com/library/archive/referencelibrary/GettingStarted/GS_Tools/index.html#//apple_ref/doc/uid/TP30001102).
- __If you're interested in security__, including documentation on support for access control lists (ACLs) in Mac OS X, see [Security Overview](../../documentation/Security/Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw).
- __If you’re interested in scripting in Mac OS X__, look at the ADC topic page for [scripting](https://developer.apple.com/opensource/scripting/). In addition, you can learn more about shell scripting in [Shell Scripting Primer](../../documentation/Shell%20Scripting%20Primer/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga2denry).

### Next Steps

The [Open Source Reference Library](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000943-TP40003594) includes the following high-level resource pages, which can be bookmarked for easy access:

- [Guides](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000440-TP40003594)

  Conceptual and how-to information for open source technologies.
- [Reference](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30001281-TP40003594)

  Sample applications demonstrating various open source technologies.
- [Sample Code](https://developer.apple.com/library/archive/navigation/redirect.html#//apple_ref/doc/uid/TP30000925-TP40003594)

  Sample applications demonstrating various open source technologies.
- Mailing Lists

  There are numerous mailing lists available to discuss open source topics with other developers. To get announcements of key events and milestones for Apple’s open source projects, join [publicsource-announce](http://lists.apple.com/mailman/listinfo/publicsource-announce), and to get announcements of open source software submissions, join [publicsource-modifications](http://lists.apple.com/mailman/listinfo/publicsource-modifications).

  In addition to these general lists, many Apple open source technologies have their own mailing lists.

  To discuss Darwin (kernel, driver, and command-line) software development, join [darwin-dev](http://lists.apple.com/mailman/listinfo/darwin-dev). Other, more specialized Darwin lists of interest include [darwin-documentation](http://lists.apple.com/mailman/listinfo/darwin-documentation) (for discussion pertaining to Darwin documentation), [darwin-drivers](http://lists.apple.com/mailman/listinfo/darwin-drivers) (on Darwin hardware drivers), [darwin-kernel](http://lists.apple.com/mailman/listinfo/darwin-kernel) (on the Darwin Mach+BSD kernel, [darwin-userlevel](http://lists.apple.com/mailman/listinfo/darwin-userlevel) (on Darwin user-level software), and [darwin-x86](http://lists.apple.com/mailman/listinfo/darwin-x86) (on Darwin on the x86 platform).

  For discussion on the QuickTime Streaming Server, join the mailing list for developers ([streaming-server-dev](http://lists.apple.com/mailman/listinfo/streaming-server-dev)) or users ([streaming-server-users](http://lists.apple.com/mailman/listinfo/streaming-server-users)).

  For software development discussion about OpenPlay and NetSprockets, join [openplay-dev](http://lists.apple.com/mailman/listinfo/openplay-dev).

  For discussion about HeaderDoc, the Man Page Generation Language (MPGL), and other related documentation tools, join [headerdoc-dev](http://lists.apple.com/mailman/listinfo/headerdoc-dev).

  For discussion of the Web Kit SDK, join the [webkitsdk-dev](http://lists.apple.com/mailman/listinfo/webkitsdk-dev) mailing list. For discussion of potential improvements and extensions to the Web Core and JavaScript Core frameworks, joine the [webcore-dev](http://lists.apple.com/mailman/listinfo/webcore-dev) mailing list.

  For discussion of web development (including server and client-side scripting, page design, and so on), join the [web-dev](http://lists.apple.com/mailman/listinfo/web-dev) mailing list.

  For discussion of Apple's open source security technologies, join the [apple-cdsa](http://lists.apple.com/mailman/listinfo/apple-cdsa) mailing list.

  For other mailing lists that may be of interest, see the Apple mailing list [info page](http://lists.apple.com/mailman/listinfo).

These additional websites may also be helpful:

- [Open Source Technologies](http://www.apple.com/opensource/)

  Apple’s open source technologies website.
- [Mac OS Forge](http://www.macosforge.org/)

  Home to a number of Apple open source technologies.
- [Open Source](https://developer.apple.com/opensource/)

  Apple’s open source topic page.
- [FreeBSD](http://www.freebsd.org/)

  Information about FreeBSD, upon which many of the open source components of Mac OS X are based.
- [Single UNIX Specification](http://www.opengroup.org/products/publications/catalog/un.htm)

  Documentation on UNIX standards.


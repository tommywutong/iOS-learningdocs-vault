---
title: BootstrapDump
apple_id: DTS10000747
resource_type: Sample Code
platform: macOS
topic: Data Management
technology: null
published: '2008-06-18'
source_url: https://developer.apple.com/library/archive/samplecode/BootstrapDump/Introduction/Intro.html
archived_at: '2026-07-18T03:02:11.702710Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](BootstrapDump.c.md)

Relevant replacement documents include:

- [http://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/launchctl.1.html](https://developer.apple.com/library/mac/#documentation/Darwin/Reference/ManPages/man1/launchctl.1.html)

# BootstrapDump

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2008-06-18 Fix a benign bug that was tripping an assert. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydanzug4wvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 2.4.1 |
| __Runtime Requirements:__ | Mac OS X 10.4 or later |

BootstrapDump is a small program that does two useful things:

- It will print the Mach bootstrap namespace for a specified process. This is helpful when debugging programs that register with the bootstrap server, or that cross bootstrap port contexts.

- It will print a map of the hierarchy of Mach bootstrap namespaces on the system and shows which processes are in which namespaces. This is useful when you want to understand the overall bootstrap namespace hierarchy.

[Next](BootstrapDump.c.md)


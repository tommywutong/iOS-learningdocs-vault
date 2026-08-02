---
title: MachPortDump
apple_id: DTS10003448
resource_type: Sample Code
platform: macOS
topic: Interapplication Communication
technology: null
published: '2005-08-10'
source_url: https://developer.apple.com/library/archive/samplecode/MachPortDump/Introduction/Intro.html
archived_at: '2026-07-18T03:14:09.228417Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](MachPortDump.c.md)

# MachPortDump

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2005-08-10 This sample code has been updated to include a project (for Xcode 2.1) to produce a universal binary and there were no code changes required for it to run correctly on the Developer Transition Systems. |
| __Build Requirements:__ | Mac OS X 10.4, Xcode 2.1 |
| __Runtime Requirements:__ | Mac OS X |

This sample dumps out the Mach port name space of a process. It is designed to be used as a tool by developers who are writing inter-process communication code on Mac OS X. Typically this code is based on Mach ports, or some higher-level wrapper around Mach ports. You can run this sample to check to see whether your code leaks ports.

[Next](MachPortDump.c.md)


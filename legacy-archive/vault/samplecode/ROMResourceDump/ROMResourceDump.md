---
title: ROMResourceDump
apple_id: DTS10000607
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/ROMResourceDump/Introduction/Intro.html
archived_at: '2026-07-18T03:21:49.669738Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Document%20Revision%20History.md)

# ROMResourceDump

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 Illustrates how to copy all resources in the Macintosh's ROM into a file. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This little utility copies all of the resources in the Macintosh's ROM into a file called "ROM Resource Dump File". This is useful for the insanely curious, those with a professional "need to know" (like DTS engineers), and as a trivial Resource Manager sample. Some notes: 1. When you run this program on some older machines it will create a resource file that ResEdit reports as corrupt. ResEdit is complaining because the file contains two resources with the same type and ID. The program does this because both resources exist in the ROM on that machine. 2. The program makes heavy use of Metrowerks Pascal's console and the ostrich error checking algorithm. 3. Efficiency was not the goal of this program. I call UpdateResFile religiously while creating the output file, which doesn't make it any faster.

[Next](Document%20Revision%20History.md)


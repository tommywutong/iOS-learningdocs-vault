---
title: OSA Preserve 68K Registers
apple_id: DTS10000209
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OSA_Preserve_68K_Registers/Introduction/Intro.html
archived_at: '2026-07-18T03:17:09.710961Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Preserve68KRegsActiveProc.h.md)

# OSA Preserve 68K Registers

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

The purpose of these functions are to save and restore a group of emulated 68K registers around calls to a PowerPC active or send function, which in turn calls YieldToAnyThread. This work-around is necessary because, at the current time, the PPC Thread Manager doesn't do anything with the emulated 68K registers, and without this work-around, the OSA AppleScript component get totally confused and blows-up. Requires: PowerPC, AppleScript, Thread Manager Keywords: AppleScript, Thread Manager, threads

[Next](Preserve68KRegsActiveProc.h.md)


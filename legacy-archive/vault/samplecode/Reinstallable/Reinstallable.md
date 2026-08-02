---
title: Reinstallable
apple_id: DTS10000196
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Reinstallable/Introduction/Intro.html
archived_at: '2026-07-18T03:22:05.762867Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](LaunchInits.c.md)

# Reinstallable

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This sample INIT patches a trap globally yet is reinstallable: it can be recompiled and run without rebooting. Usually, when an INIT patches a trap, changing the INIT requires reinstalling the INIT in the Extensions folder and rebooting. This INIT demonstrates a technique which allows new INIT code to replace most of the old code without the developer having to reboot. This INIT just patches Standard File (_Pack3) and beeps when a standard file dialog is raised.

[Next](LaunchInits.c.md)


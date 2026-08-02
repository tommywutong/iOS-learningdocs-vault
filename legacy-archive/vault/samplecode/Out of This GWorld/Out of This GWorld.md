---
title: Out of This GWorld
apple_id: DTS10000094
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-03-12'
source_url: https://developer.apple.com/library/archive/samplecode/Out_of_This_GWorld/Introduction/Intro.html
archived_at: '2026-07-18T03:18:16.043020Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CarbonPrefix.h.md)

# Out of This GWorld

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-03-12 Demonstrates the use of offscreen GWorlds and palette animation to simulate animation. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon 8 bit color, CarbonLib |

This sample has been updated for the Carbon API. The application basically uses offscreen GWorlds and palette animation to simulate totally cool animation. Since the program hopes to provide a better understanding of GWorld and palette usage, only the source file, out.c, has been commented. This file, which contains all the Color QuickDraw routines, is actually the meat of the example. The remaining source files are just typical toolbox routine calls for event and menu handling. Note that this application was written to work on 8bit devices, but can easily be modified for others. Requirements: 8 bit color, CarbonLib Keywords: Palette animation, GWorld, DisposeGWorld, AnimatePalette, Palette2CTab, CopyBits, GetEntryColor, SetEntryColor, NewGWorld, Carbon

[Next](CarbonPrefix.h.md)


---
title: Palette and GWorld
apple_id: DTS10000503
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-10-10'
source_url: https://developer.apple.com/library/archive/samplecode/Palette_and_GWorld/Introduction/Intro.html
archived_at: '2026-07-18T03:18:46.195441Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CodeWarrior%20%28OS%209%29-CarbonPrefix.h.md)

# Palette and GWorld

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-10-10 Demonstrates the use of palette and color tables with GWorlds. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon (both 9 and X) Color QuickDraw, CarbonLib |

This sample demonstrates the use of palette and color tables with GWorlds. It has been updated for Carbon. This app copies from two offscreen GWorlds into the left and right halves of the window. The contents of the GWorlds are vertical lines that show all the entries in the color tables associated with the GWorlds. The GWorlds were created as described below. One commonly asked question is how to use a palette when drawing into a GWorld. The trick is understanding that while setting a palette to a GWorld is permitted, doing so does not change the GWorld's color table. The solution is to make a palette from the color table ( or the color table from a palette) and to use that color table to create or update the GWorld. After then doing a SetGWorld you can either draw with Index2Color and RGBForeColor, or you can set the palette to the GWorld and draw with PmForeColor. These techniques are shown in the procedures createRGBForeColorImage and createPmForeColorImage in Palette and GWorld.c. Requirements: Color QuickDraw, CarbonLib Keywords: palette, GWorld, Index2Color, RGBForeColor, PmForeColor, GetCTable, NewPalette, GetMainDevice, NSetPalette, pmTable, ctSeed, GetGWorldPixMap, Carbon

[Next](CodeWarrior%20%28OS%209%29-CarbonPrefix.h.md)


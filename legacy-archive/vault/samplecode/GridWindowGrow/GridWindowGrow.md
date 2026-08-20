---
title: GridWindowGrow
apple_id: DTS10000575
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/GridWindowGrow/Introduction/Intro.html
archived_at: '2026-07-18T03:11:07.587372Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](GrowToGrid.c.md)

# GridWindowGrow

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

This snippet shows how to grow a window constrained to a grid (i.e. only allow a window to grow or shrink by 30 pixels). You might think that using something like DragHook (see the Window Manager documentation) would be the best way to approach this, but the easiest way to do this is just to write a small MyGrowWIndow function and use that. Or, even better, just grab this one demonstrated here. Requirements: Keywords: hwindowide, grid, DragHook

[Next](GrowToGrid.c.md)


---
title: DragWindowGrid
apple_id: DTS10000570
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-30'
source_url: https://developer.apple.com/library/archive/samplecode/DragWindowGrid/Introduction/Intro.html
archived_at: '2026-07-18T03:07:11.363932Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Application.c.md)

# DragWindowGrid

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-30 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

DragWindowGrid- a sample showing how to write a function to drag a window around on the screen so that it can only be released along grid lines. No patches, no hooking into drag procs, nothing fancy. This just tracks an XOR frame around the screen similar to how the Window Manager behaves, and when you let go in a different spot MoveWindow moves the window to the right place. DrawCode.c has the DragWindowGrid routine in it. You can change the kIncrement constant to change the size of the grid rects. Keywords: grid, window, MoveWindow, Window Manager

[Next](Application.c.md)


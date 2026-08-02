---
title: ViewerCallbackSample
apple_id: DTS10000137
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/ViewerCallbackSample/Introduction/Intro.html
archived_at: '2026-07-18T03:27:58.170087Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Headers-ViewerCallbacks.h.md)

# ViewerCallbackSample

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

Prior to QuickDraw 3D 1.6 it was only possible to have a window with a grow box that resized the Viewer's dimensions and always fill the entire window. This was done by setting the Viewer's kQ3ViewerDrawGrowBox flag. Some applications still need a resizable window and a resizable Viewer but wish to resize them independently. A new flag kQ3ViewerPaneGrowBox has been added so the Viewer can be resized in it's own pane. Setting this flag draws a grow box inside the Viewer's control strip which accepts mouse clicks and resized the Viewer when the user click in it. This sample show the appearance of the Viewer with this new flag, and demonstrates how the new viewer callback mechanism works.

[Next](Headers-ViewerCallbacks.h.md)


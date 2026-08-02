---
title: LiveVideoMixer2
apple_id: DTS10003747
resource_type: Sample Code
platform: macOS
topic: null
technology: QuickTime
published: '2006-05-05'
source_url: https://developer.apple.com/library/archive/samplecode/LiveVideoMixer2/Introduction/Intro.html
archived_at: '2026-07-18T03:13:38.300885Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# LiveVideoMixer2

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2006-05-05 An updated LiveVideoMixer with DV out over FireWire |
| __Build Requirements:__ | FireWire SDK 22 or later, QuickTime 7 |
| __Runtime Requirements:__ | FireWire SDK 22 or later, QuickTime 7 |

This version of the LiveVideoMixer uses the new QuickTime 7 VisualContext with CoreVideo and OpenGL compositing. It adds video output capability with DV over FireWire using the AVC VideoServices in the FireWire SDK to the first camera it finds. It demonstrates readback from the GPU, buffer handling with the AVC VideoServices and DV compression using QuickTime.
Note:
This version of the LiveVideoMixer 2 is using the FireWire SDK 22; you can find the latest SDK at: http://developer.apple.com/sdk/index.html
When you are using a later version of the FireWire SDK, make sure you change the path to the framework as well as the search path in the project.

[Next](main.m.md)


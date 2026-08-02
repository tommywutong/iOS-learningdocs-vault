---
title: Tumbler and Podium
apple_id: DTS10000127
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/Tumbler_and_Podium/Introduction/Intro.html
archived_at: '2026-07-18T03:27:20.459157Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](TumblerSource-TumblerAEVT.c.md)

# Tumbler and Podium

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Power Macintosh with at least 16Mb Ram (the more the better). You must run them with the version of the QuickDraw 3D shared library in this folder copy the entire folder you your hard disk for best results. |

QuickDraw 3D Tumbler & Podium The code (found elsewhere) illustrates how to do many things a regular app needs, such as copy and paste, drag and drop, camera manipulation, metafile read/write and very basic user interaction. Originally written as a demo, they have proved useful as sample apps (though they need a bit of cleaning up still). Let me know what you think. Requirements: Power Macintosh with at least 16Mb Ram (the more the better). You must run them with the version of the QuickDraw 3D shared library in this folder copy the entire folder you your hard disk for best results. Tumbler reads metafile data and allows you to alter various settings, such as the renderer and interpolation style. You can drag and drop to and from the finder and other 3d aware applications. You can texture map objects (if they have the appropriate parameterizations) by dropping pict data onto them. The types that you can drop are 3DMF and PICT. PICT drags will only work if there is already 3DMF data being displayed, they will be used to texture map objects. Podium is a mock up of a multimedia app. You can read in "presentations" which are actually just PICT files. It lets you drag 3D data from other Apps. You can use Shift-click to zoom in, Apple-click to zoom out, ctrl-click to move the object around. Although I'm "caretaking" the code at the moment, these applications incorporate ideas and code from everybody in the QuickDraw 3D team, so a big thank you to them (and also to Pablo Fernicola, who wrote the orginal versions of both these apps). Please not that at this time, the apps behave erratically under extreme low memory conditions, so if you have odd hangs and crashes, t is likely that this is due to low memory. These are samples, and as such are not as robust as commercial software!! Enjoy.

[Next](TumblerSource-TumblerAEVT.c.md)


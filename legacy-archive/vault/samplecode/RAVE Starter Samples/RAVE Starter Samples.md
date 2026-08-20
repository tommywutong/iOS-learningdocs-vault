---
title: RAVE Starter Samples
apple_id: DTS10000155
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/RAVE_Starter_Samples/Introduction/Intro.html
archived_at: '2026-07-18T03:21:47.886262Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](CallBack%20Sample-Gouraud%20Callback.cp.md)

# RAVE Starter Samples

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 First Version |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon |

There are three different samples here, each showing a variation on the same theme -- we create a window and do some simple 2D drawing into it. These samples don't show any clipping code or a full featured 3D engine; these will appear in a future sample. These versions were compiled with CodeWarrior Pro 3 and the RAVE 1.5 SDK. For more information, check out TechNote 1125, which covers many issues related to developing RAVE applications. RAVE Common Code -- A few routines are used by multiple samples, so I pulled them out here to have a single code base. They are also routines that are very useful for many RAVE applications. Gouraud Sample -- This creates context on a specific GDevice and draws a single shaded triangle onto it until you click the mouse. Callback Sample -- This is identical to the Gouraud sample, except that it also demonstrates how to implement a compositing callback. Erase callbacks look identical to compositing callbacks, and these are the two most common callbacks games will implement. Texture Sample -- Loads a texture into memory and then draws a textured triangle. Requires: RAVE Keywords: RAVE, Gouraud, compsite, callback, texture, 3D

[Next](CallBack%20Sample-Gouraud%20Callback.cp.md)


---
title: PBORenderToVertexArray
apple_id: DTS10004089
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2006-10-02'
source_url: https://developer.apple.com/library/archive/samplecode/PBORenderToVertexArray/Introduction/Intro.html
archived_at: '2026-07-18T03:18:20.307906Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# PBORenderToVertexArray

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2006-10-02 Minor revision to the OpenGL extension checking code. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgmjqgaydimbyhewvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v.10.4.3 and Xcode 2.3 |
| __Runtime Requirements:__ | Mac OS X v.10.4.3 and a graphics card that supports the FBO and PBO extensions |

This sample demonstrates render-to-vertex-array using FBO, PBO, and VBO.
A VBO is allocated with storage and indices for an N x N mesh.
Then content is drawn into an N x N texture attached to an FBO.
The pixel data is copied from the FBO into the VBO, by binding a PBO to the VBO id and calling glReadPixels.
Now the pixel RGBA colors can be used as vertex XYZW data.

[Next](ReadMe.txt.md)


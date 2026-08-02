---
title: Passing IOSurfaces from one process to another via Mach RPC
apple_id: DTS40010132
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2014-10-13'
source_url: https://developer.apple.com/library/archive/samplecode/MultiGPUIOSurface/Introduction/Intro.html
archived_at: '2026-07-18T03:16:25.401312Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Readme.txt.md)

# Passing IOSurfaces from one process to another via Mach RPC

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.2, 2014-10-13 Updated with Core Profile. Cleaned up code. Removed deprecated calls. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaytamjtgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | OS X 10.9 or later, Xcode 5.1 or later |
| __Runtime Requirements:__ | OS X 10.7 or later |

MutiGPUIOSurface shows how to create IOSurfaces and bind them to OpenGL textures for both reading and writing. It demonstrates one way of passing IOSurfaces from one process to another via Mach RPC calls. It also demonstrates the system's ability to track IOSurface changes across process and GPU boundaries.

After building the integrated target "MultiGPUApps", first run the server application "MultiGPUServer" and then the client application "MultiGPUClient".

[Next](Readme.txt.md)


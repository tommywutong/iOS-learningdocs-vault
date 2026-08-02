---
title: OpenCL Procedural Geometric Displacement Example
apple_id: DTS40008192
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2009-09-24'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Procedural_Geometric_Displacement_Example/Introduction/Intro.html
archived_at: '2026-07-18T03:17:51.921497Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# OpenCL Procedural Geometric Displacement Example

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.4, 2009-09-24 Updated to adapt to API changes. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmjzgiwvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6, Xcode 3.2 |
| __Runtime Requirements:__ | Mac OS X v10.6 |

This example shows how OpenCL can bind to existing OpenGL buffers to avoid copying data back off a compute device when using the results for rendering. This is demonstrated by displacing the vertices of an OpenGL managed vertex buffer object (VBO) using a compute kernel which calculates several octaves of procedural noise to push the resulting vertex positions outwards and calculate new normal directions using finite differences.

[Next](ReadMe.txt.md)


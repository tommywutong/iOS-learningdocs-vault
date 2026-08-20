---
title: OpenCL Procedural Grass and Terrain Example
apple_id: DTS40008186
resource_type: Sample Code
platform: macOS
topic: Performance
technology: OpenCL
published: '2011-01-12'
source_url: https://developer.apple.com/library/archive/samplecode/OpenCL_Procedural_Grass_and_Terrain_Example/Introduction/Intro.html
archived_at: '2026-07-18T03:17:52.832221Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](ReadMe.txt.md)

# OpenCL Procedural Grass and Terrain Example

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.5, 2011-01-12 Removed the line that caused over-releasing of the "path" object. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqmjygywvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Mac OS X v10.6 or later |
| __Runtime Requirements:__ | Max OS X v10.6 or later |

This example shows how OpenCL can be used to create a procedural field of grass on a generated terrain model which is then rendered with OpenGL. Because OpenGL buffers are shared with OpenCL, the data can remain on the graphics card, thus eliminating the API overhead of creating and submitting the vertices from the host.

All geometry is generated on the compute device, and outputted into a shared OpenGL buffer. The terrain gets generated only within the visible arc covering the camera's view frustum to avoid the need for culling. A page of grass is computed on the surface of the terrain as bezier patches, and flow noise is applied to the angle of the blades to simulate wind. Multiple instances of grass are rendered at jittered offsets to add more grass coverage without having to compute new pages. Finally, a physically based sky shader (via OpenGL) is applied to the background to provide an environment for the grass.

Note that the .cl compute kernel file(s) and shader files (.vert and .frag) are loaded and compiled at runtime. The example source assumes that these files are in the same path as the built executable.

[Next](ReadMe.txt.md)


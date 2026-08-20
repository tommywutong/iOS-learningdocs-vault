---
title: VertexPerformanceTest
apple_id: DTS10000554
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/VertexPerformanceTest/Introduction/Intro.html
archived_at: '2026-07-18T03:27:48.676247Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](main.m.md)

# VertexPerformanceTest

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 A tool that measures triangle throughput and allows comparison of different methods. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon ProjectBuilder, Mac OS X v10.2 or later |

Vertex Performance Test Change History -------------- version 1.3 - added 4 texture units - added secondary color - rearranged UI version 1.2 - added Size slider. - added Macros checkbox and functionality - added Matrix checkbox and functionality version 1.1 - Support for GL_APPLE_vertex_array_range - Added this fancy about box - Added auto-rotate - Took timing down from .5 seconds to .1 second to make animation a little smoother version 1.0 first release About ----- This tool was written as I was writing some code to enhance the performance of display lists. It measures triangle throughput and allows comparison of different methods. To see something interesting, enable the "Texture" and "Normal" and "Auto" checkboxes. Right now, the light stays stationary and the camera rotates. It would probably be more interesting to keep the light with the camera. The Macros checkbox test the performance of going through direct calls to the function dispatch table instead of through normal function calls. This only affects the "Vertex Calls" setting. The Matrix checkbox loads a Matrix using glLoadMatrix() before drawing to illustrate the performance impact of unnecessary calls to glLoadMatrix. Secondary color only modifies the output color when lighting is off (in this app that is when the drawing isn't using normals). It is correct for seconday color to not be used when lighting is enabled. Notes ----- The model is generated using code from Jason Shankel's "Fractal Terrain Generation - Fault Formation" article in Game Programming Gems. More information about this book is available at http://www.satori.org/gamegems/ Requirements: ProjectBuilder, Mac OS X v10.2 or later Keywords: OpenGL, AGL, vertex array range, VAR, VAO, display list

[Next](main.m.md)


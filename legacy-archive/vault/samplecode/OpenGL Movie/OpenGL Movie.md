---
title: OpenGL Movie
apple_id: DTS10000539
resource_type: Sample Code
platform: macOS
topic: null
technology: null
published: '2003-01-14'
source_url: https://developer.apple.com/library/archive/samplecode/OpenGL_Movie/Introduction/Intro.html
archived_at: '2026-07-18T03:18:11.895558Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Carbon%20Include.h.md)

# OpenGL Movie

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-01-14 A demonstration of QuickTime and OpenGL integration and optimized texture mapping. |
| __Build Requirements:__ |  |
| __Runtime Requirements:__ | Carbon OpenGL, 3D, full screen, DrawSprocket, QuickTime, Movie, |

A demonstration of QuickTime and OpenGL integration and optimized texture mapping. This includes demonstrating the use of the OpenGL packed pixel extension. Version 1.1: Updated for Mac OS X including full screen support. Version 1.0: Carbonized for Mac OS X. OpenGL Movie is built with CodeWarrior 6 and the latest Carbon SDK (1.3d6 as of this writing). It requires the latest Carbon SetupGL and aglString sample code. OpenGL Movie demonstrates the integration of OpenGL with QuickTime in a Carbon framework. Particluar attention has been paid to performance and clarity. Carbon timers are used to handle frame drawing. Only frames that actually chnage are uploaded as textures. The Packed Pixel extension is checked for and used is available. The application allows many setting changes for developers to see how performance varies. Any suggestions and/or bugs can be directed to the Apple bug reporter at: <http://developer.apple.com/bugreporter/index.html> Note: Some of the access paths will have to reset to point to the location of the OpenGL SDK and the Carbon SDK on your local system and this is built using Universal Interfaces 3.4a5 and Carbon SDK 1.2f2 or later. If you are not useing the latest OpenGL 1.2 headers then some small modifcations may have to be made be removing the glext.h file. We hope this helps people get up and running with OpenGL and QuickTime (and texturing) in a quick and painless manner. CodeWarrior 6, Carbon SDK 1.3d6 or later, PowerPC, System 8.1+, OpenGL SDK, DrawSprocket, and Universal Interfaces 3.4b5 or later Requirements: OpenGL, 3D, full screen, DrawSprocket, QuickTime, Movie, Keywords: texture mapping

[Next](Carbon%20Include.h.md)


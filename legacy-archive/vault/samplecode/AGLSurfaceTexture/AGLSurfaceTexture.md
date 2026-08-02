---
title: AGLSurfaceTexture
apple_id: DTS10000508
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2003-07-07'
source_url: https://developer.apple.com/library/archive/samplecode/AGLSurfaceTexture/Introduction/Intro.html
archived_at: '2026-07-18T02:59:34.549510Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](AGLSurfaceTexture.c.md)

# AGLSurfaceTexture

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.0, 2003-07-07 Example of render to texture/texture from surface using aglSurfaceTexture. |
| __Build Requirements:__ | Mac OS X v10.2 |
| __Runtime Requirements:__ | Mac OS X v10.2 |

A sample showing an example of render to texture/texture from surface using aglSurfaceTexture. Version 1.0: Initial release This sample demonstrates using aglSurfaceTexture to texture from a surface which in turn is an aglContext thus also demonstrates render to texture. The basic concept to build an AGLcontext which, is the source for texturing. This surface must comply with all the constraints for the current texturing mode, such as dimensions being a power of two for TEXTURE_2D. This surface (identified by the AGLContext) is then used as the source for the aglSurfaceTexture API. This API is very similar to Texture2D as it provides a current texture for GL to using in texturing operations. All other texturing requirements remain the same (enable, texture coords, etc). Note: Under CodeWarrior you will have to change the access path for the OpenGL SDK with valid a one for your local environment. Requirements: Mac OS X v10.2 Keywords: Carbon, OpenGL, render to texture, texture from surface, aglSurfaceTexture

[Next](AGLSurfaceTexture.c.md)


---
title: GLUTSurfaceTexture
apple_id: DTS10000532
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2004-03-26'
source_url: https://developer.apple.com/library/archive/samplecode/GLUTSurfaceTexture/Introduction/Intro.html
archived_at: '2026-07-18T03:10:33.578332Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](glutSurfaceTexture.c.md)

# GLUTSurfaceTexture

|  |  |
| --- | --- |
| __Last Revision:__ | Version 1.1, 2004-03-26 Fixed bug in which sample was incorrectly using the default texture (not allowed with surface texture). Corrected other rendering problems dealing with lighting and glut current windows. Updated for Xcode. Updated sample code disclaimers. |
| __Build Requirements:__ | Xcode |
| __Runtime Requirements:__ | Mac OS X glut 3.1+, Mac OS X 10.2.3 or later. |

A fairly simple example of using glutSurfaceTexture to texture from one surface to
another.
Surface textre API notes:
glutSurfaceTexture (GLenum target, GLenum internalformat, int surfacewin)
target: Specifies an allowable 2D OpenGL texture target such as GL_TEXTURE_2D or GL_TEXTURE_RECTANGLE_EXT.
internalformat: Specifies the internal texture layout, which must be a supported format listed on table 3.15, 3.16, 3.17 or 3.18 of the OpenGL 1.3 Specification.
surfacewin: Specifies the GLUT window from which to get the texture.
glutSurfaceTexture allows direct texturing from a window by using the window contents as the source data for the texture, behaving much the same way as glTexImage2D. The texture target, internal format must be supported the renderer of the target context. Additionally, the source window geometry must be compatible with the texture target. Thus, if the texture target is GL_TEXTURE_2D, the window must conform to power of two dimensions.
This routine is designed for performance so the graphics driver will attempt to provide an optimum data path, keeping the data in VRAM if possible. Also, there is no window tracking, thus both target and source windows must be on the same virtual screen (renderer) or failure (likely lack of texturing) will result.

[Next](glutSurfaceTexture.c.md)


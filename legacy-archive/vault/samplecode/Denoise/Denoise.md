---
title: Denoise
apple_id: DTS40008908
resource_type: Sample Code
platform: macOS
topic: Graphics & Animation
technology: null
published: '2011-06-27'
source_url: https://developer.apple.com/library/archive/samplecode/Denoise/Introduction/Intro.html
archived_at: '2026-07-18T03:06:24.736604Z'
---
> 导航：[总目录](../../README.md) · [samplecode](../../_indexes/samplecode.md)


[Next](Sources-Classes-Application-Core-Controller-CIGLDenoiseViewController.h.md)

# Denoise

|  |  |
| --- | --- |
| __Last Revision:__ | Version 2.1, 2011-06-27 Removed duplicate references in the Xcode project. Removed obsolete build settings in the Xcode project. [(Full Revision History)](Document%20Revision%20History.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpirkfgnbqgaydqojqhawvezlwnfzws33ojbuxg5dpoj4s2rdpnz2ey2lonncwyzlnmvxhiskel4yq) |
| __Build Requirements:__ | Xcode 4 Xcode v3.2 Xcode v3.2 |
| __Runtime Requirements:__ | Snow Leopard 10.6 |

This application demonstrates how to use the Core Image noise-reduction and median filters to denoise a picture, and then save the results as a JPEG image using Core Graphics application programming interfaces.

This is the fifth application in the series that includes QTCoreVideo102, QTCoreVideo103, QTCoreVideo201, and QTCoreVideo202 that leverage a common graphics and media utility toolkits for Snow Leopard.

• Application

• CIGLDenoiseViewController - Controller class for the application. • CIGLDenoiseView - Main view class for the application.

• Utility Kits

• Model

• CIGLDenoiseFilter - A facade for managing Core Image median and noise reduction filters. • CIGLFilter - Utility base class for mediating between a Core Image filters, context, and a frame buffer object. • CIGLFramebuffer - Utility class for managing Core Image context and render to texture using a frame buffer object. • NSPropertyList - Utility class to deserialize a property list file. • OpenGLBitmap - Utility toolkit to save a pixel buffer as bmp, pict, png, gif, jpeg, tga, or jp2000 file(s). • OpenGLCopier - A functor for copying pixels from a source to destination. • OpenGLDrawElements - Utility class to deserialize a property list that describes a VBO draw elements parameters and draws an object using the parameters values. • OpenGLFramebuffer2D - Utility class for managing 2D FBOs. • OpenGLIBO - Utility class that implements a method for generating a 3D object using IBOs. • OpenGLIBORenderer - Class that implements methods for creating an IBO based renderer. • OpenGLIBOIndices - Utility class to deserialize a property list that describes a VBO's indices. • OpenGLIBOGeometry - Utility class to deserialize a property list that describes a IBO normals, vertices, colors, and texture coordinates. • OpenGLImage2DAuthor - A facade for handling PBO read or draw pixels. • OpenGLQuad - A facade for for handling a texture 2D or texture rectangle bound to a VBO quad. • OpenGLPBO - Utility toolkit providing basic functionality for PBOs (pack/unpack). • OpenGLPixelAttributes - Utility class to parse property list file and obtain the desired pixel format attributes. • OpenGLPixelFormat - Utility class to obtain pixel format for an OpenGL view. • OpenGLRotation - Utility class for managing rotation of a 3D object. • OpenGLSurface2D - Utility toolkit for 2D I/O surfaces. • OpenGLTeapot - a facade that implements methods for generating an IBO teapot with enabled sphere map texture coordinate generation. • OpenGLTexture2D - Utility toolkit for handling hinted texture 2D or rectangles. • OpenGLTexture2DAuthor - A facade for managing PBOs for texture read or writes.

• View

• OpenGLView - OpenGL view base class.

[Next](Sources-Classes-Application-Core-Controller-CIGLDenoiseViewController.h.md)


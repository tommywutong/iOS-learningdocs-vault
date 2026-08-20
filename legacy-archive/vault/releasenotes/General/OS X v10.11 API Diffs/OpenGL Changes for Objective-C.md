---
title: OS X v10.11 API Diffs
apple_id: TP40016197
resource_type: Release Note
platform: macOS
topic: General
technology: null
published: '2015-09-16'
source_url: https://developer.apple.com/library/archive/releasenotes/General/APIDiffsMacOSX10_11/Objective-C/OpenGL.html
archived_at: '2026-07-18T02:53:11.204694Z'
---
> 导航：[总目录](../../../README.md) · [releasenotes](../../../_indexes/releasenotes.md) · [OS X v10.11 API Diffs](OS%20X%20v10.11%20API%20Diffs.md)


# OpenGL Changes for Objective-C

### OpenGL

#### CGLCurrent.h

Modified CGLGetCurrentContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLContextObj CGLGetCurrentContext (     void ); ``` |
| To | ``` CGLContextObj _Nullable CGLGetCurrentContext (     void ); ``` |

Modified CGLSetCurrentContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetCurrentContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLSetCurrentContext (     CGLContextObj _Nullable ctx ); ``` |

#### CGLDevice.h

Modified CGLGetDeviceFromGLRenderer()

|  | Declaration |
| --- | --- |
| From | ``` cl_device_id CGLGetDeviceFromGLRenderer (     GLint rendererID ); ``` |
| To | ``` cl_device_id _Nonnull CGLGetDeviceFromGLRenderer (     GLint rendererID ); ``` |

Modified CGLGetShareGroup()

|  | Declaration |
| --- | --- |
| From | ``` CGLShareGroupObj CGLGetShareGroup (     CGLContextObj ctx ); ``` |
| To | ``` CGLShareGroupObj _Nullable CGLGetShareGroup (     CGLContextObj _Nonnull ctx ); ``` |

#### CGLIOSurface.h

Modified CGLTexImageIOSurface2D()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLTexImageIOSurface2D (     CGLContextObj ctx,     GLenum target,     GLenum internal_format,     GLsizei width,     GLsizei height,     GLenum format,     GLenum type,     IOSurfaceRef ioSurface,     GLuint plane ); ``` |
| To | ``` CGLError CGLTexImageIOSurface2D (     CGLContextObj _Nonnull ctx,     GLenum target,     GLenum internal_format,     GLsizei width,     GLsizei height,     GLenum format,     GLenum type,     IOSurfaceRef _Nonnull ioSurface,     GLuint plane ); ``` |

#### CGLTypes.h

Added #def OPENGL_ASSUME_NONNULL_BEGINAdded #def OPENGL_ASSUME_NONNULL_ENDAdded #def OPENGL_NONNULLAdded #def OPENGL_NULLABLEModified kCGLPFAStereo

|  | Deprecation |
| --- | --- |
| From | -- |
| To | OS X 10.11 |

#### OpenGL.h

Modified CGLChoosePixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLChoosePixelFormat (     const CGLPixelFormatAttribute *attribs,     CGLPixelFormatObj *pix,     GLint *npix ); ``` |
| To | ``` CGLError CGLChoosePixelFormat (     const CGLPixelFormatAttribute * _Nonnull attribs,     CGLPixelFormatObj  _Nullable * _Nonnull pix,     GLint * _Nonnull npix ); ``` |

Modified CGLClearDrawable()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLClearDrawable (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLClearDrawable (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLCopyContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLCopyContext (     CGLContextObj src,     CGLContextObj dst,     GLbitfield mask ); ``` |
| To | ``` CGLError CGLCopyContext (     CGLContextObj _Nonnull src,     CGLContextObj _Nonnull dst,     GLbitfield mask ); ``` |

Modified CGLCreateContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLCreateContext (     CGLPixelFormatObj pix,     CGLContextObj share,     CGLContextObj *ctx ); ``` |
| To | ``` CGLError CGLCreateContext (     CGLPixelFormatObj _Nonnull pix,     CGLContextObj _Nullable share,     CGLContextObj  _Nullable * _Nonnull ctx ); ``` |

Modified CGLCreatePBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLCreatePBuffer (     GLsizei width,     GLsizei height,     GLenum target,     GLenum internalFormat,     GLint max_level,     CGLPBufferObj *pbuffer ); ``` |
| To | ``` CGLError CGLCreatePBuffer (     GLsizei width,     GLsizei height,     GLenum target,     GLenum internalFormat,     GLint max_level,     CGLPBufferObj  _Nullable * _Nonnull pbuffer ); ``` |

Modified CGLDescribePBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDescribePBuffer (     CGLPBufferObj obj,     GLsizei *width,     GLsizei *height,     GLenum *target,     GLenum *internalFormat,     GLint *mipmap ); ``` |
| To | ``` CGLError CGLDescribePBuffer (     CGLPBufferObj _Nonnull obj,     GLsizei * _Nonnull width,     GLsizei * _Nonnull height,     GLenum * _Nonnull target,     GLenum * _Nonnull internalFormat,     GLint * _Nonnull mipmap ); ``` |

Modified CGLDescribePixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDescribePixelFormat (     CGLPixelFormatObj pix,     GLint pix_num,     CGLPixelFormatAttribute attrib,     GLint *value ); ``` |
| To | ``` CGLError CGLDescribePixelFormat (     CGLPixelFormatObj _Nonnull pix,     GLint pix_num,     CGLPixelFormatAttribute attrib,     GLint * _Nonnull value ); ``` |

Modified CGLDescribeRenderer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDescribeRenderer (     CGLRendererInfoObj rend,     GLint rend_num,     CGLRendererProperty prop,     GLint *value ); ``` |
| To | ``` CGLError CGLDescribeRenderer (     CGLRendererInfoObj _Nonnull rend,     GLint rend_num,     CGLRendererProperty prop,     GLint * _Nullable value ); ``` |

Modified CGLDestroyContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDestroyContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLDestroyContext (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLDestroyPBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDestroyPBuffer (     CGLPBufferObj pbuffer ); ``` |
| To | ``` CGLError CGLDestroyPBuffer (     CGLPBufferObj _Nonnull pbuffer ); ``` |

Modified CGLDestroyPixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDestroyPixelFormat (     CGLPixelFormatObj pix ); ``` |
| To | ``` CGLError CGLDestroyPixelFormat (     CGLPixelFormatObj _Nonnull pix ); ``` |

Modified CGLDestroyRendererInfo()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDestroyRendererInfo (     CGLRendererInfoObj rend ); ``` |
| To | ``` CGLError CGLDestroyRendererInfo (     CGLRendererInfoObj _Nonnull rend ); ``` |

Modified CGLDisable()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLDisable (     CGLContextObj ctx,     CGLContextEnable pname ); ``` |
| To | ``` CGLError CGLDisable (     CGLContextObj _Nonnull ctx,     CGLContextEnable pname ); ``` |

Modified CGLEnable()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLEnable (     CGLContextObj ctx,     CGLContextEnable pname ); ``` |
| To | ``` CGLError CGLEnable (     CGLContextObj _Nonnull ctx,     CGLContextEnable pname ); ``` |

Modified CGLErrorString()

|  | Declaration |
| --- | --- |
| From | ``` const char * CGLErrorString (     CGLError error ); ``` |
| To | ``` const char * _Nonnull CGLErrorString (     CGLError error ); ``` |

Modified CGLFlushDrawable()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLFlushDrawable (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLFlushDrawable (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLGetContextRetainCount()

|  | Declaration |
| --- | --- |
| From | ``` GLuint CGLGetContextRetainCount (     CGLContextObj ctx ); ``` |
| To | ``` GLuint CGLGetContextRetainCount (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLGetGlobalOption()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetGlobalOption (     CGLGlobalOption pname,     GLint *params ); ``` |
| To | ``` CGLError CGLGetGlobalOption (     CGLGlobalOption pname,     GLint * _Nonnull params ); ``` |

Modified CGLGetOffScreen()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetOffScreen (     CGLContextObj ctx,     GLsizei *width,     GLsizei *height,     GLint *rowbytes,     void **baseaddr ); ``` |
| To | ``` CGLError CGLGetOffScreen (     CGLContextObj _Nonnull ctx,     GLsizei * _Nonnull width,     GLsizei * _Nonnull height,     GLint * _Nonnull rowbytes,     void * _Nullable * _Nonnull baseaddr ); ``` |

Modified CGLGetOption()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetOption (     CGLGlobalOption pname,     GLint *param ); ``` |
| To | ``` CGLError CGLGetOption (     CGLGlobalOption pname,     GLint * _Nonnull param ); ``` |

Modified CGLGetParameter()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetParameter (     CGLContextObj ctx,     CGLContextParameter pname,     GLint *params ); ``` |
| To | ``` CGLError CGLGetParameter (     CGLContextObj _Nonnull ctx,     CGLContextParameter pname,     GLint * _Nonnull params ); ``` |

Modified CGLGetPBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetPBuffer (     CGLContextObj ctx,     CGLPBufferObj *pbuffer,     GLenum *face,     GLint *level,     GLint *screen ); ``` |
| To | ``` CGLError CGLGetPBuffer (     CGLContextObj _Nonnull ctx,     CGLPBufferObj  _Nullable * _Nonnull pbuffer,     GLenum * _Nonnull face,     GLint * _Nonnull level,     GLint * _Nonnull screen ); ``` |

Modified CGLGetPBufferRetainCount()

|  | Declaration |
| --- | --- |
| From | ``` GLuint CGLGetPBufferRetainCount (     CGLPBufferObj pbuffer ); ``` |
| To | ``` GLuint CGLGetPBufferRetainCount (     CGLPBufferObj _Nonnull pbuffer ); ``` |

Modified CGLGetPixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` CGLPixelFormatObj CGLGetPixelFormat (     CGLContextObj ctx ); ``` |
| To | ``` CGLPixelFormatObj _Nullable CGLGetPixelFormat (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLGetPixelFormatRetainCount()

|  | Declaration |
| --- | --- |
| From | ``` GLuint CGLGetPixelFormatRetainCount (     CGLPixelFormatObj pix ); ``` |
| To | ``` GLuint CGLGetPixelFormatRetainCount (     CGLPixelFormatObj _Nonnull pix ); ``` |

Modified CGLGetVersion()

|  | Declaration |
| --- | --- |
| From | ``` void CGLGetVersion (     GLint *majorvers,     GLint *minorvers ); ``` |
| To | ``` void CGLGetVersion (     GLint * _Nullable majorvers,     GLint * _Nullable minorvers ); ``` |

Modified CGLGetVirtualScreen()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLGetVirtualScreen (     CGLContextObj ctx,     GLint *screen ); ``` |
| To | ``` CGLError CGLGetVirtualScreen (     CGLContextObj _Nonnull ctx,     GLint * _Nonnull screen ); ``` |

Modified CGLIsEnabled()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLIsEnabled (     CGLContextObj ctx,     CGLContextEnable pname,     GLint *enable ); ``` |
| To | ``` CGLError CGLIsEnabled (     CGLContextObj _Nonnull ctx,     CGLContextEnable pname,     GLint * _Nonnull enable ); ``` |

Modified CGLLockContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLLockContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLLockContext (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLQueryRendererInfo()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLQueryRendererInfo (     GLuint display_mask,     CGLRendererInfoObj *rend,     GLint *nrend ); ``` |
| To | ``` CGLError CGLQueryRendererInfo (     GLuint display_mask,     CGLRendererInfoObj  _Nullable * _Nonnull rend,     GLint * _Nonnull nrend ); ``` |

Modified CGLReleaseContext()

|  | Declaration |
| --- | --- |
| From | ``` void CGLReleaseContext (     CGLContextObj ctx ); ``` |
| To | ``` void CGLReleaseContext (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLReleasePBuffer()

|  | Declaration |
| --- | --- |
| From | ``` void CGLReleasePBuffer (     CGLPBufferObj pbuffer ); ``` |
| To | ``` void CGLReleasePBuffer (     CGLPBufferObj _Nonnull pbuffer ); ``` |

Modified CGLReleasePixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` void CGLReleasePixelFormat (     CGLPixelFormatObj pix ); ``` |
| To | ``` void CGLReleasePixelFormat (     CGLPixelFormatObj _Nonnull pix ); ``` |

Modified CGLRetainContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLContextObj CGLRetainContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLContextObj _Nonnull CGLRetainContext (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLRetainPBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLPBufferObj CGLRetainPBuffer (     CGLPBufferObj pbuffer ); ``` |
| To | ``` CGLPBufferObj _Nonnull CGLRetainPBuffer (     CGLPBufferObj _Nonnull pbuffer ); ``` |

Modified CGLRetainPixelFormat()

|  | Declaration |
| --- | --- |
| From | ``` CGLPixelFormatObj CGLRetainPixelFormat (     CGLPixelFormatObj pix ); ``` |
| To | ``` CGLPixelFormatObj _Nonnull CGLRetainPixelFormat (     CGLPixelFormatObj _Nonnull pix ); ``` |

Modified CGLSetFullScreen()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetFullScreen (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLSetFullScreen (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLSetFullScreenOnDisplay()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetFullScreenOnDisplay (     CGLContextObj ctx,     GLuint display_mask ); ``` |
| To | ``` CGLError CGLSetFullScreenOnDisplay (     CGLContextObj _Nonnull ctx,     GLuint display_mask ); ``` |

Modified CGLSetGlobalOption()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetGlobalOption (     CGLGlobalOption pname,     const GLint *params ); ``` |
| To | ``` CGLError CGLSetGlobalOption (     CGLGlobalOption pname,     const GLint * _Nullable params ); ``` |

Modified CGLSetOffScreen()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetOffScreen (     CGLContextObj ctx,     GLsizei width,     GLsizei height,     GLint rowbytes,     void *baseaddr ); ``` |
| To | ``` CGLError CGLSetOffScreen (     CGLContextObj _Nonnull ctx,     GLsizei width,     GLsizei height,     GLint rowbytes,     void * _Nonnull baseaddr ); ``` |

Modified CGLSetParameter()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetParameter (     CGLContextObj ctx,     CGLContextParameter pname,     const GLint *params ); ``` |
| To | ``` CGLError CGLSetParameter (     CGLContextObj _Nonnull ctx,     CGLContextParameter pname,     const GLint * _Nonnull params ); ``` |

Modified CGLSetPBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetPBuffer (     CGLContextObj ctx,     CGLPBufferObj pbuffer,     GLenum face,     GLint level,     GLint screen ); ``` |
| To | ``` CGLError CGLSetPBuffer (     CGLContextObj _Nonnull ctx,     CGLPBufferObj _Nonnull pbuffer,     GLenum face,     GLint level,     GLint screen ); ``` |

Modified CGLSetVirtualScreen()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLSetVirtualScreen (     CGLContextObj ctx,     GLint screen ); ``` |
| To | ``` CGLError CGLSetVirtualScreen (     CGLContextObj _Nonnull ctx,     GLint screen ); ``` |

Modified CGLTexImagePBuffer()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLTexImagePBuffer (     CGLContextObj ctx,     CGLPBufferObj pbuffer,     GLenum source ); ``` |
| To | ``` CGLError CGLTexImagePBuffer (     CGLContextObj _Nonnull ctx,     CGLPBufferObj _Nonnull pbuffer,     GLenum source ); ``` |

Modified CGLUnlockContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLUnlockContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLUnlockContext (     CGLContextObj _Nonnull ctx ); ``` |

Modified CGLUpdateContext()

|  | Declaration |
| --- | --- |
| From | ``` CGLError CGLUpdateContext (     CGLContextObj ctx ); ``` |
| To | ``` CGLError CGLUpdateContext (     CGLContextObj _Nonnull ctx ); ``` |

## Sending feedback…

## We’re sorry, an error has occurred.

Please try submitting your feedback later.

## Thank you for providing feedback!

Your input helps improve our developer documentation.

## How helpful is this document?

\*

Very helpful

Somewhat helpful

Not helpful

## How can we improve this document?

Fix typos or links

Fix incorrect information

Add or update code samples

Add or update illustrations

Add information about...

\*

_\* Required information_

To submit a product bug or enhancement request, please visit the
[Bug Reporter](https://developer.apple.com/bugreporter/)
page.

Please read [Apple's Unsolicited Idea Submission Policy](http://www.apple.com/legal/policies/ideas.html)
before you send us your feedback.

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)

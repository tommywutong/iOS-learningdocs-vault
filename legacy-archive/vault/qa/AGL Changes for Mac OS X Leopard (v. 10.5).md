---
title: AGL Changes for Mac OS X Leopard (v. 10.5)
apple_id: DTS10004506
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2008-01-04'
source_url: https://developer.apple.com/library/archive/qa/qa1523/_index.html
archived_at: '2026-07-18T02:32:09.710448Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1523

# AGL Changes for Mac OS X Leopard (v. 10.5)

## Q:  What has changed for AGL in Mac OS X v.10.5?

A: The following is a detailed list of changes to the AGL framework on Mac OS X v.10.5 as shown on the agl.h header file.

This header is located at:


```
/System/Library/Frameworks/AGL.framework/Headers/agl.h
```


The Apple OpenGL Interface or AGL, has been updated on this release of the OS to take full advantage of the Quartz Display Services and support setting `HIViewRef` and `WindowRef` directly as rendering destinations.

- The new version of the API is defined as:


```
 #define AGL_VERSION_3_0  1
```


- The new entry points regarding pixel formats are as follows:


```
 AGLPixelFormat aglCreatePixelFormat(const GLint *attribs);
 CGDirectDisplayID *aglDisplaysOfPixelFormat(AGLPixelFormat pix, GLint *ndevs);
```

  To support the new pixel format creation with `aglCreatePixelFormat`, the following pixel formate attribute name is defined as:


```
#define AGL_DISPLAY_MASK          84  /* mask limiting supported displays             */
```

  As an example of usage, the following listing creates a pixel format that limits the renderers to those supported by the main display only.

  __Listing 1__  Creating a pixel format .

```
 // Get display ID to use for a mask
    // The main display as configured via System Preferences
    CGDirectDisplayID displayID = CGMainDisplayID();
    CGOpenGLDisplayMask openGLDisplayMask = CGDisplayIDToOpenGLDisplayMask(displayID);

    // Solely as an example of possible use, this pixel format limits
    // the possible renderers to those supported by the screen mask.
    // In this case the main display.
    GLint attrib[] = {	AGL_RGBA,
                        AGL_DOUBLEBUFFER,
                        AGL_DEPTH_SIZE, 16,
                        AGL_DISPLAY_MASK, openGLDisplayMask, // New to Mac OS X v10.5
                        AGL_NONE };

    // aglChoosePixelFormat has been deprecated on Mac OS X v10.5 use aglCreatePixelFormat
    // as shown below.
    AGLPixelFormat thePixelFormat = aglCreatePixelFormat(attrib); // New to Mac OS X v10.5
```


- The new way of querying renderer information based on `CGDirectDisplayID`:


```
 AGLRendererInfo aglQueryRendererInfoForCGDirectDisplayIDs(const CGDirectDisplayID *dspIDs, GLint ndev);
```


- The new drawable functions are based on `WindowRef` and `HIViewRef` and are defined as:


```
 GLboolean aglSetWindowRef(AGLContext ctx, WindowRef window);
 WindowRef aglGetWindowRef(AGLContext ctx);

 GLboolean aglSetHIViewRef(AGLContext ctx, HIViewRef hiview);
 HIViewRef aglGetHIViewRef(AGLContext ctx);
```

  The following source shows how to create an AGL context and set it's drawable based on a `WindowRef`

  __Listing 2__  Setting the AGL context drawable based on a `WindowRef`.

```
 AGLContext theAGLContext = aglCreateContext(thePixelFormat, NULL); // No context to share with

    // Instead of aglSetDrawable use
    // aglSetWindowRef or aglSetHIViewRef
    aglSetWindowRef(theAGLContext, window);
```


- `AGLDevice` is a QuickDraw type; it has been deprecated, use `CGDirectDisplayID`.


```
typedef GDHandle AGLDevice;
```
- The integer parameter AGL_CLIP_REGION has been deprecated.


```
#define AGL_CLIP_REGION          254  /* Enable or set the drawable clipping region */
```
- `AGLDrawable` is a QuickDraw type; it has been deprecated, use `WindowRef` or `HIViewRef`.


```
typedef CGrafPtr AGLDrawable;
```
- `aglSetDrawable` and `aglGetDrawable` have been deprecated; use aglGetWindowRef or aglSetHIViewRef.


```
 GLboolean aglSetDrawable(AGLContext ctx, AGLDrawable draw);
 AGLDrawable aglGetDrawable(AGLContext ctx);
```
- `aglUseFont` has been deprecated and no replacement is available at this time. As an alternative Quartz can be used to draw text into a string texture, or a texture atlas of several characters.


```
GLboolean aglUseFont(AGLContext ctx, GLint fontID,
                                         Style face, GLint size, GLint first, GLint count, GLint base);
```
- `aglSurfaceTexture` has been deprecated, no replacement available at this time. There is no explicit need for a replacement since a framebuffer object (FBO) or a PBuffer provides this functionality.


```
 void aglSurfaceTexture (AGLContext context, GLenum target, GLenum internalformat, AGLContext surfacecontext);
```


- [AGL Framework Reference](https://developer.apple.com/documentation/GraphicsImaging/Reference/AGL_OpenGL/index.html)
- [AGL Reference Update](https://developer.apple.com/documentation/GraphicsImaging/Reference/AGLRefUpdate/index.html)
- [OpenGL Programming Guide for Mac OS X](https://developer.apple.com/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/)
- [Quartz Display Services Reference](https://developer.apple.com/documentation/GraphicsImaging/Reference/Quartz_Services_Ref/)

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-06 | This Q&A describes the new and deprecated APIs for Apple OpenGL (AGL) |
| 2008-01-04 | New document that this Q&A describes the new and deprecated APIs for Apple OpenGL (AGL) |


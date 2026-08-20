---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/opengl_pixelformats/opengl_pixelformats.html
archived_at: '2026-07-15T07:36:43.443665Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Working%20with%20Rendering%20Contexts.md)[Previous](Drawing%20Offscreen.md)

# Choosing Renderer and Buffer Attributes

Renderer and buffer attributes determine the renderers that the system chooses for your application. Each of the Apple-specific OpenGL APIs provides constants that specify a variety of renderer and buffer attributes. You supply a list of attribute constants to one of the Apple OpenGL functions for choosing a pixel format object. The pixel format object maintains a list of renderers that meet the requirements defined by those attributes.

In a real-world application, selecting attributes is an art because you don't know the exact combination of hardware and software that your application will run on. An attribute list that is too restrictive may miss out on future capabilities or it may fail to return renderers on some systems. For example, if you specify a buffer of a specific depth, your application won't be able to take advantage of a larger buffer when more memory is available in the future. In this case, you might specify a required minimum and direct OpenGL to use the maximum available.

Although you might specify attributes that make your OpenGL content look and run its best, you also need to consider whether your application should run on a less-capable system with less speed or detail. If tradeoffs are acceptable, you need to set the attributes accordingly.

When your application is running on OS X v10.7, it should always include the `kCGLPFAOpenGLProfile` attribute, followed by a constant for the profile whose functionality your application requires. A profile affects different parts of OpenGL in OS X:

- A profile requires that a specific version of the OpenGL API must provided by the renderer. The renderer may implement a different version of the OpenGL specification only if that version implements the same functions and constants required by the profile; typically, this means a renderer that supports a later version of the OpenGL specification that did not remove or alter behavior specified in the version of the OpenGL specification your application requested.
- The profile alters the list of OpenGL extensions returned by the renderer. For example, extensions whose functionality is provided by the version of the OpenGL specification you requested are not also returned in the list of extensions.
- On OS X, the profile affects what other renderer and buffer attributes may be included in the attributes list.

Follow these guidelines to choose an OpenGL profile:

- If you are developing a new OS X v10.7 application, implement your OpenGL functionality using the OpenGL 3.2 Core profile; include the `kCGLOGLPVersion_3_2_Core` constant.

  The OpenGL 3.2 core profile is defined by Khronos and explicitly removes deprecated features described in earlier versions of the OpenGL specification; further the core profile prohibits these functions from being added back into OpenGL using extensions. OpenGL 3.2 core represents a complete break from the fixed function pipeline of OpenGL 1.x in favor of a clean, lean shader-based pipeline.

  When you use the OpenGL 3.2 Core profile on OS X, legacy extensions are removed wherever their functionality is already provided by OpenGL 3.2. Further, pixel and buffer format attributes that are marked as deprecated may not be used in conjunction with the OpenGL 3.2 core profile.
- If you are updating an existing OS X application, include the `kCGLOGLPVersion_Legacy` constant.

  The legacy profile provides the same functionality found in earlier versions of OS X, with no changes. It continues to support older extensions as well as deprecated pixel and buffer format attributes. No new functionality will be added to the legacy profile in future versions of OS X.
- If you want to use OpenGL 3.2 in your application, but also want to support earlier versions of OS X or Macs that lack hardware support for OpenGL 3.2, you must implement multiple OpenGL rendering options in your application. On OS X v10.7, your application should first test to see if OpenGL 3.2 is supported. If OpenGL 3.2 is supported, create a context and provide it to your OpenGL 3.2 rendering path. Otherwise, search for a pixel format using the legacy profile instead.

For more information on migrating an application to OpenGL 3.2, see [Updating an Application to Support the OpenGL 3.2 Core Specification](Updating%20an%20Application%20to%20Support%20the%20OpenGL%203.2%20Core%20Specification.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmznknltc).

Follow these guidelines to choose buffer attributes that specify buffer size:

- To choose color, depth, and accumulation buffers that are greater than or equal to a size you specify, use the minimum policy attribute (`NSOpenGLPFAMinimumPolicy` or `kCGLPFAMinimumPolicy`).
- To choose color, depth, and accumulation buffers that are closest to a size you specify, use the closest policy attribute (`NSOpenGLPFAClosestPolicy` or `kCGLPFAClosestPolicy`).
- To choose the largest color, depth, and accumulation buffers available, use the maximum policy attribute (`NSOpenGLPFAMaximumPolicy` or `kCGLPFAMaximumPolicy`). As long as you pass a value that is greater than `0`, this attribute specifies the use of color, depth, and accumulation buffers that are the largest size possible.

When your application uses a double-buffered context, it displays the rendered image by calling a function to flush the image to the screen— the`NSOpenGLContext` class’s `flushBuffer` method or the CGL function `CGLFlushDrawable`. When the image is displayed, the contents of the back buffer are not preserved. The next time your application wants to update the back buffer, it must completely redraw the scene.

Your application can add a backing store attribute (`NSOpenGLPFABackingStore` or `kCGLPFABackingStore`) to preserve the contents of the buffer after the back buffer is flushed. Adding this attribute disables some optimizations that the system can perform, which may impact the performance of your application.

The pixel format routines (the [initWithAttributes:](https://developer.apple.com/documentation/appkit/nsopenglpixelformat/1436219-init) method of the `NSOpenGLPixelFormat` class and the `CGLChoosePixelFormat` function) return a pixel format object to your application that you use to create a rendering context. The buffer and renderer attributes that you supply to the pixel format routine determine the characteristics of the OpenGL drawing sent to the rendering context. If the system can't find at least one pixel format that satisfies the constraints specified by the attribute array, it returns `NULL` for the pixel format object. In this case, your application should have an alternative that ensures it can obtain a valid object.

One alternative is to set up your attribute array with the least restrictive attribute first and the most restrictive attribute last. Then, it is fairly easy to adjust the attribute list and make another request for a pixel format object. The code in Listing 6-1 illustrates this technique using the CGL API. Notice that the initial attributes list is set up with the supersample attribute last in the list. If the function `CGLChoosePixelFormat` returns `NULL`, it clears the supersample attribute to `NULL` and tries again.

__Listing 6-1__  Using the CGL API to create a pixel format object

```
int last_attribute = 6;
CGLPixelFormatAttribute attribs[] =
{
    kCGLPFAAccelerated,
    kCGLPFAColorSize, 24
    kCGLPFADepthSize, 16,
    kCGLPFADoubleBuffer,
    kCGLPFASupersample,
    0
};

CGLPixelFormatObj pixelFormatObj;
GLint numPixelFormats;
long value;

CGLChoosePixelFormat (attribs, &pixelFormatObj, &numPixelFormats);

if( pixelFormatObj == NULL ) {
    attribs[last_attribute] = NULL;
    CGLChoosePixelFormat (attribs, &pixelFormatObj, &numPixelFormats);
}

if( pixelFormatObj == NULL ) {
    // Your code to notify the user and take action.
}
```


There are times when you want to ensure that you obtain a pixel format that supports a specific renderer type, such as a hardware-accelerated renderer. Table 6-1 lists attributes that support specific types of renderers. The table reflects the following tips for setting up pixel formats:

- To select only hardware-accelerated renderers, use both the accelerated and no-recovery attributes.
- To use only the floating-point software renderer, use the appropriate generic floating-point constant.
- To render to system memory, use the offscreen pixel attribute. Note that this rendering option does not use hardware acceleration.
- To render offscreen with hardware acceleration, specify a pixel buffer attribute. (See [Rendering to a Pixel Buffer](Drawing%20Offscreen.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqgmwvgvzt).)

__Table 6-1__  Renderer types and pixel format attributes

| Renderer type | CGL | Cocoa |
| Hardware-accelerated onscreen | `kCGLPFAAccelerated`  `kCGLPFANoRecovery` | `NSOpenGLPFAAccelerated`  `NSOpenGLPFANoRecovery` |
| Software (floating-point) | `kCGLPFARendererID`  `kCGLRendererGenericFloatID` | `NSOpenGLPFARendererID`  `kCGLRendererGenericFloatID` |
| System memory (not accelerated) | `kCGLPFAOffScreen` | `NSOpenGLPFAOffScreen` |
| Hardware-accelerated offscreen | `kCGLPFAPBuffer` | `NSOpenGLPFAPixelBuffer` |

In some cases you may want to use a specific hardware renderer and nothing else. Since the OpenGL framework normally provides a software renderer as a fallback in addition to whatever hardware renderer it chooses, you need to prevent OpenGL from choosing the software renderer as an option. To do this, specify the no-recovery attribute for a windowed drawable object.

Limiting a context to use a specific display, and thus a single renderer, has its risks. If your application runs on a system that uses more than one display, dragging a windowed drawable object from one display to the other is likely to yield a less than satisfactory result. Either rendering fails, or OpenGL uses the specified renderer and then copies the result to the second display. The same unsatisfactory result happens when attaching a full-screen context to another display. If you choose to use the hardware renderer associated with a specific display, you need to add code that detects and handles display changes.

The code examples that follow show how to use each of the Apple-specific OpenGL APIs to set up a context that uses a single renderer. Listing 6-2 shows how to set up an `NSOpenGLPixelFormat` object that supports a single renderer. The attribute `NSOpenGLPFANoRecovery` specifies to OpenGL not to provide the fallback option of the software renderer.

__Listing 6-2__  Setting an `NSOpenGLContext` object to use a specific display

```objc
#import <Cocoa/Cocoa.h>
+ (NSOpenGLPixelFormat*)defaultPixelFormat
{
    NSOpenGLPixelFormatAttribute attributes [] = {
                        NSOpenGLPFAScreenMask, 0,
                        NSOpenGLPFANoRecovery,
                        NSOpenGLPFADoubleBuffer,
                        (NSOpenGLPixelFormatAttribute)nil };
CGDirectDisplayID display = CGMainDisplayID ();
// Adds the display mask attribute for selected display
attributes[1] = (NSOpenGLPixelFormatAttribute)
                    CGDisplayIDToOpenGLDisplayMask (display);
return [[(NSOpenGLPixelFormat *)[NSOpenGLPixelFormat alloc] initWithAttributes:attributes]
                                       autorelease];
}
```

Listing 6-3 shows how to use CGL to set up a context that uses a single renderer. The attribute `kCGLPFANoRecovery` ensures that OpenGL does not provide the fallback option of the software renderer.

__Listing 6-3__  Setting a CGL context to use a specific display

```c
#include <OpenGL/OpenGL.h>
CGLPixelFormatAttribute attribs[] = { kCGLPFADisplayMask, 0,
                                 kCGLPFANoRecovery,
                                 kCGLPFADoubleBuffer,
                                  0 };
CGLPixelFormatObj pixelFormat = NULL;
GLint numPixelFormats = 0;
CGLContextObj cglContext = NULL;
CGDirectDisplayID display = CGMainDisplayID ();
// Adds the display mask attribute for selected display
attribs[1] = CGDisplayIDToOpenGLDisplayMask (display);
CGLChoosePixelFormat (attribs, &pixelFormat, &numPixelFormats);
```


Adding the attribute `NSOpenGLPFAAllowOfflineRenderers` allows OpenGL to include offline renderers in the list of virtual screens returned in the pixel format object. Apple recommends you include this attribute, because it allows your application to work better in environments where renderers come and go, such as when a new display is plugged into a Mac.

If your application includes `NSOpenGLPFAAllowOfflineRenderers` in the list of attributes, your application must also watch for display changes and update its rendering context. See [Update the Rendering Context When the Renderer or Geometry Changes](Working%20with%20Rendering%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgywvgvzv).

If your applications uses OpenCL to perform other computations, you may want to find an OpenGL renderer that also supports OpenCL. To do this, add the attribute `NSOpenGLPFAAcceleratedCompute` to the pixel format attribute list. Adding this attribute restricts the list of renderers to those that also support OpenCL.

More information on OpenCL can be found in the _[OpenCL Programming Guide for Mac](../../Performance/OpenCL%20Programming%20Guide%20for%20Mac/About%20OpenCL%20for%20OS%20X.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga4dgmjs)_.

There are several renderer and buffer attributes that are no longer recommended either because they are too narrowly focused or no longer useful. Your application should move away from using any of these attributes:

- The robust attribute (`NSOpenGLPFARobust` or `kCGLPFARobust`) specifies only those renderers that do not have any failure modes associated with a lack of video card resources.
- The multiple-screen attribute (`NSOpenGLPFAMultiScreen` or `kCGLPFAMultiScreen`) specifies only those renderers that can drive more than one screen at a time.
- The multiprocessing-safe attribute (`kCGLPFAMPSafe`) specifies only those renderers that are thread safe. This attribute is deprecated in OS X because all renderers can accept commands for threads running on a second processor. However, this does not mean that all renderers are thread safe or reentrant. See [Concurrency and OpenGL](Concurrency%20and%20OpenGL.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqnbqhewvgvzr).
- The compliant attribute (`NSOpenGLPFACompliant` or `kCGLPFACompliant`) specifies only OpenGL-compliant renderers. All OS X renderers are OpenGL-compliant, so this attribute is no longer useful.
- The full screen attribute (`kCGLPFAFullScreen`) requested special full screen contexts. The window screen attribute (`kCGLPFAWindow)` required the context to support windowed contexts. OS X no longer requires a special full screen context to be created, as it automatically provides the same performance benefits with a properly formatted window.
- The offscreen buffer attribute (`kCGLPFAOffScreen`) selects renderers capable of rendering to offscreen memory. Instead, use a frame buffer object as the rendering target and read the final results back to application memory.
- The pixel buffer attributes (`kCGLPFAPBuffer` and `kCGLPFARemotePBuffer` are no longer recommended; use frame buffer objects instead.
- The auxiliary buffers attribute (`kCGLPFAAuxBuffers`) specifies the number of required auxiliary buffers your application requires. Auxiliary buffers are not supported by the OpenGL 3.2 Core profile. Because auxiliary buffers are not supported, the `kCGLPFAAuxDepthStencil` attribute that modifies it is also deprecated.
- The accumulation buffer size attribute (`kCGLPFAAccumSize`) specifies the desired size for the accumulation buffer. Accumulation buffers are not supported by the OpenGL 3.2 Core Profile.

[Next](Working%20with%20Rendering%20Contexts.md)[Previous](Drawing%20Offscreen.md)


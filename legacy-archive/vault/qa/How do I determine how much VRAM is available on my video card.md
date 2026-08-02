---
title: How do I determine how much VRAM is available on my video card?
apple_id: DTS10003307
resource_type: QA
platform: macOS
topic: Graphics & Animation
technology: ApplicationServices
published: '2014-03-11'
source_url: https://developer.apple.com/library/archive/qa/qa1168/_index.html
archived_at: '2026-07-18T02:30:11.877680Z'
---
> 导航：[总目录](../README.md) · [qa](../_indexes/qa.md)



Technical Q&A QA1168

# How do I determine how much VRAM is available on my video card?

## Q:  How do I determine how much VRAM is available on my video card?

A: The `CGLQueryRendererInfo()` and `CGLDescribeRenderer()` functions allow you to obtain the properties of the renderers on your system, including their VRAM sizes. On OS X 10.7 and later, you can query a renderer with the `kCGLRPVideoMemoryMegabytes` parameter to get the number of megabytes of video memory available to the renderer.

See [CGL Reference Renderer Properties](https://developer.apple.com/library/mac/documentation/graphicsimaging/reference/cgl_opengl/Reference/reference.html#//apple_ref/c/tdef/CGLRendererProperty) for the complete list of renderer property constants including `kCGLRPVideoMemoryMegabytes`, `kCGLRPTextureMemoryMegabytes`, etc.

Listing 1 demonstrates how to determine the VRAM size for your current OpenGL renderer.

__Listing 1__  Finding the current renderer's VRAM size

```objc
- (void)logVideoMemoryCurrentRenderer
{
    GLint virtualScreen = [[self openGLContext] currentVirtualScreen];

    // Since this may be called from outside the display loop, make sure
    // the context is current so the GL calls all work properly.
    [[self openGLContext] makeCurrentContext];

    // Use the current virtual screen index to interrogate the pixel format
    // for its display mask and renderer id.
    // Note, "pixelFormat" is the NSOpenGLPixelFormat that your OpenGL context
    // is created from, typically created in your OpenGL view's -initWithFrame:
    GLint displayMask;
    GLint rendererID;
    [pixelFormat getValues:&displayMask forAttribute:NSOpenGLPFAScreenMask forVirtualScreen:virtualScreen];
    [pixelFormat getValues:&rendererID  forAttribute:NSOpenGLPFARendererID forVirtualScreen:virtualScreen];

    // Get renderer info for all renderers that match the display mask.
    GLint i, nrend = 0;
    CGLRendererInfoObj rend;

    CGLQueryRendererInfo((GLuint)displayMask, &rend, &nrend);

    GLint videoMemory = 0;
    for (i = 0; i < nrend; i++)
    {
        GLint thisRendererID;

        CGLDescribeRenderer(rend, i, kCGLRPRendererID, &thisRendererID);

        // See if this is the one we want
        if (thisRendererID == rendererID) {
            CGLDescribeRenderer(rend, i, kCGLRPVideoMemoryMegabytes, &videoMemory);

            NSLog(@"%@", [NSString stringWithCString:(const char *)glGetString(GL_RENDERER)
                                            encoding:NSASCIIStringEncoding]);
            NSLog(@"Renderer ID = 0x%x", thisRendererID);
            NSLog(@"Video Memory = %d MB", videoMemory);
        }
    }

    CGLDestroyRendererInfo(rend);
}
```

If you are looking for the VRAM sizes of all the renderers on your system, including those that are not attached to monitors (offline renderers), you may specify a `-1/0xFFFFFFFF` display mask in the `CGLQueryRendererInfo()` function. See Listing 2 for an example.

__Listing 2__  Finding all renderers' VRAM sizes

```objc
- (void)logVideoMemoryAllRenderers
{
    // Get renderer info for all renderers that match the display mask.
    GLint i, nrend = 0;
    CGLRendererInfoObj rend;

    // Using a -1/0xFFFFFFFF display mask enables us to find all renderers,
    // including those GPUs that are not attached to monitors, aka. offline renderers.
    const GLint displayMask = 0xFFFFFFFF;

    CGLQueryRendererInfo((GLuint)displayMask, &rend, &nrend);

    for(i = 0; i < nrend; i++)
    {
        GLint thisRendererID;
        GLint videoMemory = 0;

        CGLDescribeRenderer(rend, i, kCGLRPRendererID, &thisRendererID);
        NSLog(@"Renderer ID = 0x%x", thisRendererID);

        CGLDescribeRenderer(rend, i, kCGLRPVideoMemoryMegabytes, &videoMemory);
        NSLog(@"Video Memory = %d MB", videoMemory);
    }

    CGLDestroyRendererInfo(rend);
}
```

---

#### Document Revision History

| __Date__ | __Notes__ |
| 2014-03-11 | Updated for OS X 10.9. |
| 2004-10-11 | New document that using CGLDescribeRenderer to find the physical size of VRAM on installed hardware. |


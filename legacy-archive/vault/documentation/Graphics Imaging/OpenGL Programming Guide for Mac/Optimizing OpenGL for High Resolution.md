---
title: OpenGL Programming Guide for Mac
apple_id: TP40001987
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: OpenGL
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/OpenGL-MacProgGuide/EnablingOpenGLforHighResolution/EnablingOpenGLforHighResolution.html
archived_at: '2026-07-15T07:36:28.893459Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [OpenGL Programming Guide for Mac](About%20OpenGL%20for%20OS%20X.md)


[Next](Drawing%20to%20the%20Full%20Screen.md)[Previous](Drawing%20to%20a%20Window%20or%20View.md)

# Optimizing OpenGL for High Resolution

OpenGL is a pixel-based API so the `NSOpenGLView` class does not provide high-resolution surfaces by default. Because adding more pixels to renderbuffers has performance implications, you must explicitly opt in to support high-resolution screens. It’s easy to enable high-resolution backing for an OpenGL view. When you do, you’ll want to perform a few additional tasks to ensure the best possible high-resolution experience for your users.

You can opt in to high resolution by calling the method `setWantsBestResolutionOpenGLSurface:` when you initialize the view, and supplying `YES` as an argument:

```
[self  setWantsBestResolutionOpenGLSurface:YES];
```

If you don’t opt in, the system magnifies the rendered results.

The `wantsBestResolutionOpenGLSurface` property is relevant only for views to which an `NSOpenGLContext` object is bound. Its value does not affect the behavior of other views. For compatibility, `wantsBestResolutionOpenGLSurface` defaults to `NO`, providing a 1-pixel-per-point framebuffer regardless of the backing scale factor for the display the view occupies. Setting this property to `YES` for a given view causes AppKit to allocate a higher-resolution framebuffer when appropriate for the backing scale factor and target display.

To function correctly with `wantsBestResolutionOpenGLSurface` set to `YES`, a view must perform correct conversions between view units (points) and pixel units as needed. For example, the common practice of passing the width and height of `[self bounds]` to `glViewport()` will yield incorrect results at high resolution, because the parameters passed to the `glViewport()` function must be in pixels. As a result, you’ll get only partial instead of complete coverage of the render surface. Instead, use the backing store bounds:

```
 [self convertRectToBacking:[self bounds]];
```

You can also opt in to high resolution by enabling the Supports Hi-Res Backing setting for the OpenGL view in Xcode, as shown in Figure 3-1.

__Figure 3-1__  Enabling high-resolution backing for an OpenGL view

!!

The viewport dimensions are in pixels relative to the OpenGL surface. Pass the width and height to `glViewPort` and use 0,0 for the `x` and `y` offsets. Listing 3-1 shows how to get the view dimensions in pixels and take the backing store size into account.

__Listing 3-1__  Setting up the viewport for drawing

```objc
- (void)drawRect:(NSRect)rect   // NSOpenGLView subclass
{
    // Get view dimensions in pixels
    NSRect backingBounds = [self convertRectToBacking:[self bounds]];

    GLsizei backingPixelWidth  = (GLsizei)(backingBounds.size.width),
            backingPixelHeight = (GLsizei)(backingBounds.size.height);

    // Set viewport
    glViewport(0, 0, backingPixelWidth, backingPixelHeight);

    // draw…
}
```

You don’t need to perform rendering in pixels, but you do need to be aware of the coordinate system you want to render in. For example, if you want to render in points, this code will work:

```
glOrtho(NSWidth(bounds), NSHeight(bounds),...)
```


If you opt in to high-resolution drawing, you also need to adjust the model and texture assets of your app. For example, when running on a high-resolution display, you might want to choose larger models and more detailed textures to take advantage of the increased number of pixels. Conversely, on a standard-resolution display, you can continue to use smaller models and textures.

If you create and cache textures when you initialize your app, you might want to consider a strategy that accommodates changing the texture based on the resolution of the display.

These functions use pixel dimensions:

- `glViewport (GLint x, GLint y, GLsizei width, GLsizei height)`
- `glScissor (GLint x, GLint y, GLsizei width, GLsizei height)`
- `glReadPixels (GLint x, GLint y, GLsizei width, GLsizei height, ...)`
- `glLineWidth (GLfloat width)`
- `glRenderbufferStorage (..., GLsizei width, GLsizei height)`
- `glTexImage2D (..., GLsizei width, GLsizei height, ...)`

Performance is an important factor when determining whether to support high-resolution content. The quadrupling of pixels that occurs when you opt in to high resolution requires more work by the fragment processor. If your app performs many per-fragment calculations, the increase in pixels might reduce its frame rate. If your app runs significantly slower at high resolution, consider the following options:

- Optimize fragment shader performance. (See [Tuning Your OpenGL Application](Tuning%20Your%20OpenGL%20Application.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgaytsobxfvbuqmrrgmwvgvzr).)
- Choose a simpler algorithm to implement in your fragment shader. This reduces the quality of each individual pixel to allow for rendering the overall image at a higher resolution.
- Use a fractional scale factor between 1.0 and 2.0. A scale factor of 1.5 provides better quality than a scale factor of 1.0, but it needs to fill fewer pixels than an image scaled to 2.0.
- Multisampling antialiasing can be costly with marginal benefit at high resolution. If you are using it, you might want to reconsider.

The best solution depends on the needs of your OpenGL app; you should test more than one of these options and choose the approach that provides the best balance between performance and image quality.

When you draw standard controls and Cocoa text to a layer-backed view, the system handles scaling the contents of that layer for you. You need to perform only a few steps to set and use the layer. Compare the controls and text in standard and high resolutions, as shown in Figure 3-2. The text looks the same on both without any additional work on your part.

__Figure 3-2__  A text overlay scales automatically for standard resolution (left) and high resolution (right)

!!![bullet](../../../_unindexed/Resources/1282/Images/task_2x.png)To set up a layer-backed view for OpenGL content

1. Set the `wantsLayer` property of your [NSOpenGLView](https://developer.apple.com/documentation/appkit/nsopenglview) subclass to `YES`.

   Enabling the `wantsLayer` property of an `NSOpenGLView` object activates layer-backed rendering of the OpenGL view. Drawing a layer-backed OpenGL view proceeds mostly normally through the view’s [drawRect:](https://developer.apple.com/documentation/appkit/nsview/1483686-draw) method. The layer-backed rendering mode uses its own `NSOpenGLContext` object, which is distinct from the `NSOpenGLContext` that the view uses for drawing in non-layer-backed mode.

   AppKit automatically creates this context and assigns it to the view by invoking the [setOpenGLContext:](https://developer.apple.com/documentation/appkit/nsopenglview/1414942-openglcontext) method. The view’s [openGLContext](https://developer.apple.com/documentation/appkit/nsopengllayer/1522570-openglcontext) accessor will return the layer-backed OpenGL context (rather than the non-layer-backed context) while the view is operating in layer-backed mode.
2. Create the layer content either as a XIB file or programmatically.

   The controls shown in Figure 3-2 were created in a XIB file by subclassing [NSBox](https://developer.apple.com/documentation/appkit/nsbox) and using static text with a variety of standard controls. Using this approach allows the [NSBox](https://developer.apple.com/documentation/appkit/nsbox) subclass to ignore mouse events while still allowing the user to interact with the OpenGL content.
3. Add the layer to the OpenGL view by calling the [addSublayer:](https://developer.apple.com/documentation/quartzcore/calayer/1410833-addsublayer) method.

For the best user experience, if you want your app to run full screen, create a window that covers the entire screen. This approach offers two advantages:

- The system provides optimized context performance.
- Users will be able to see critical system dialogs above your content.

You should avoid changing the display mode of the system.

Always convert window event coordinates when performing hit testing in OpenGL. The [locationInWindow](https://developer.apple.com/documentation/appkit/nsevent/1529068-locationinwindow) method of the [NSEvent](https://developer.apple.com/documentation/appkit/nsevent) class returns the receiver’s location in the base coordinate system of the window. You then need to call the [convertPoint:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483269-convertpoint) method to get the local coordinates for the OpenGL view.

```
NSPoint aPoint = [theEvent locationInWindow];
NSPoint localPoint = [myOpenGLView convertPoint:aPoint fromView:nil];
```

[Next](Drawing%20to%20the%20Full%20Screen.md)[Previous](Drawing%20to%20a%20Window%20or%20View.md)


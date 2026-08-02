---
title: Quartz Programming Guide for QuickDraw Developers
apple_id: TP40001098
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2006-09-05'
source_url: https://developer.apple.com/library/archive/documentation/Carbon/Conceptual/QuickDrawToQuartz2D/tq_copybits/tq_copybits.html
archived_at: '2026-07-15T05:24:31.882861Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Quartz Programming Guide for QuickDraw Developers](Introduction%20to%20Quartz%20Programming%20Guide%20for%20QuickDraw%20Developers.md)


[Next](Performance.md)[Previous](Hit%20Testing.md)

# Offscreen Drawing

QuickDraw applications often draw in an offscreen graphics world and use `CopyBits` to blit the image to the screen in one operation. Prior to Mac OS X, this was the recommended way to prevent flicker during lengthy drawing operations. Windows in Mac OS X are double-buffered, and window buffers are flushed automatically inside the application event loop. Therefore the use of offscreen graphics worlds for this purpose should no longer be necessary.

There are occasions when it still makes sense to draw offscreen and move the offscreen image into a window in a single operation. In Mac OS X, the primary motivation for drawing offscreen is to cache content. For example, you may want to cache an image that’s used more than once, or move selected areas of a large image into a window at different times. During rapid animation sequences, some applications prepare a background image offscreen, move the background to the window as a unit, and draw the animated parts of the scene over the background.

Quartz provides two offscreen drawing environments: bitmap graphics contexts and CGLayer objects (introduced in Mac OS X 10.4). The HIView function `HIViewCreateOffscreenImage` is also worth considering if your application is HIView based. This function creates a CGImage object for the HIView passed to it.

If your application runs in Mac OS X v10.4 and later, you should consider using CGLayer objects for offscreen drawing. Prior to that version, offscreen drawing is done to a bitmap graphics context.

A bitmap graphics context in Quartz is analogous to an offscreen graphics world with user-supplied storage for the pixel map (`NewGWorldFromPtr`). You can create bitmap contexts with many different pixel formats, including 8-bit gray, 16-bit RGB, and 32 bit RGBA, ARGB, and CMYK.

You create a bitmap context by calling the function [CGBitmapContextCreate](https://developer.apple.com/documentation/coregraphics/cgcontext/1455939-init) and passing in a specific set of attributes, including a bitmap into which Quartz renders your drawing. You’re free to use the bitmap for other purposes—for example, you could create a bitmap context and a graphics world that share the same memory.

After drawing in a bitmap context, you can easily transfer the bitmap image to another Quartz context of any type. To maintain device independence, copying an image is a drawing operation and not a blitting operation. There are two steps:

1. Create a Quartz image from the bitmap. In Mac OS X v10.4 and later, you can use the function `CGBitmapContextCreateImage`.
2. Draw the image in the destination context using the function [CGContextDrawImage](https://developer.apple.com/documentation/coregraphics/1454845-cgcontextdrawimage).

For detailed information about creating and using bitmap contexts, see [Graphics Contexts](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_context/dq_context.html#//apple_ref/doc/uid/TP30001066-CH203) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

Starting in Mac OS X 10.4, the recommended way to draw offscreen is to create a CGLayer object and draw to it. CGLayers are opaque types that provide a context for offscreen drawing. A CGLayer object is created from an existing graphics context by calling the function [CGLayerCreateWithContext](https://developer.apple.com/documentation/coregraphics/1450892-cglayercreatewithcontext). The resulting CGLayer object has all the characteristics of the graphics context that the layer is created from. After the layer object is created, you pass it to the function [CGLayerGetContext](https://developer.apple.com/documentation/coregraphics/1450902-cglayergetcontext) to get a graphics context for the layer. It is this graphics context that you draw to using the function `CGLayerDrawAtPoint` and `CGLayerDrawInRect`. You cannot access layer drawing directly.

CGLayer objects are cached by the operating system whenever possible, which greatly improves drawing performance. One important feature of CGLayers is that you do not need to know the device characteristics of the destination context.

It’s best to use a CGLayer when you need to:

- Reuse your drawing, as in the background scene for a game.
- Draw the same image multiple times, as in a game sprite.

To use CGLayer, follow these steps:

1. Call the function [CGLayerCreateWithContext](https://developer.apple.com/documentation/coregraphics/1450892-cglayercreatewithcontext) to create a CGLayer object from an existing graphics context. The resulting CGLayer object has all the characteristics of the graphics context that the layer is created from. Carbon applications can use the context provided in the `kEventControlDraw` event for this purpose.
2. After the layer object is created, pass it to the function [CGLayerGetContext](https://developer.apple.com/documentation/coregraphics/1450902-cglayergetcontext) to get a graphics context for the layer. It is this graphics context that you draw to.
3. To draw to the layer graphics context, use any of the Quartz drawing functions (such as [CGContextDrawPath](https://developer.apple.com/documentation/coregraphics/cgcontext/1455195-drawpath), [CGContextFillRect](https://developer.apple.com/documentation/coregraphics/1454700-cgcontextfillrect), and so forth), passing the layer graphics context as the context parameter. Note that you cannot access the drawing in the layer directly.
4. To draw the contents of a CGLayer to a destination graphics context (possibly the same graphics context used to create the layer, but it doesn’t need to be). Use the functions `CGLayerDrawAtPoint` and `CGLayerDrawInRect`.

For a code example that shows how to draw using CGLayer objects, see [CGLayer Drawing](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_layers/dq_layers.html#//apple_ref/doc/uid/TP30001066-CH219) in _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_.

In _[Quartz 2D Programming Guide](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Introduction.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrw)_, see:

- [CGLayer Drawing](../../Graphics%20Imaging/Quartz%202D%20Programming%20Guide/Graphics%20Contexts.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaytanrwfvbuqmrqgmwugsscirbuqqkd)
- [Graphics Contexts](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/dq_context/dq_context.html#//apple_ref/doc/uid/TP30001066-CH203)

See these reference documents:

- _[CGContext Reference](https://developer.apple.com/documentation/coregraphics/cgcontext)_
- _[CGBitmapContext Reference](https://developer.apple.com/documentation/coregraphics/cgbitmapcontext)_
- _[CGLayer Reference](https://developer.apple.com/documentation/coregraphics/cglayer)_

[Next](Performance.md)[Previous](Hit%20Testing.md)


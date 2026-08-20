---
title: High Resolution Guidelines for OS X
apple_id: TP40012302
resource_type: Guide
platform: macOS
topic: Graphics & Animation
technology: null
published: '2012-09-19'
source_url: https://developer.apple.com/library/archive/documentation/GraphicsAnimation/Conceptual/HighResolutionOSX/APIs/APIs.html
archived_at: '2026-07-15T07:34:59.547902Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [High Resolution Guidelines for OS X](About%20High%20Resolution%20for%20OS%20X.md)


[Next](Testing%20and%20Troubleshooting%20High-Resolution%20Content.md)[Previous](Advanced%20Optimization%20Techniques.md)

# APIs for Supporting High Resolution

This chapter highlights the APIs you should use, and points out the older methods and functions you should no longer use. You’ll also find information on APIs added or modified to support high resolution. Please also see the appropriate reference documentation for each API mentioned in this chapter.

There are very few, if any, situations for which you need to use device coordinates directly. You should be able to accomplish any task that relates to drawing geometry by using the APIs described in this section.

In all cases it is best to rely on using one of the APIs that support high resolution rather than trying to manage values yourself. Although multiplying by a scale factor (as shown below) might produce the desired result:

```
    NSNumber *myValue = [[NSNumber alloc] initWithDouble:value.y * scaleFactor];
```

the preferred approach is to use a conversion method:

```
    NSNumber *myValue = [[NSNumber alloc]
                        initWithDouble:[self convertPointToBacking:value].y];
```

You might be tempted to use device coordinates if your app allows users to choose a screen resolution, such as for a game. However, keep in mind that with high resolution, users will be unaware of the pixel dimensions. You should refer to display dimensions only in points.

To support high resolution, you might need to convert rectangles or points from the coordinate system of one `NSView` instance to another (typically the superview or subview), or from one `NSView` instance to the containing window. The [NSView](https://developer.apple.com/documentation/appkit/nsview) class defines six methods that convert rectangles, points, and sizes in either direction.

| Convert to the receiver from the specified view | Convert from the receiver to the specified view |
| --- | --- |
| [convertPoint:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483269-convertpoint) | [convertPoint:toView:](https://developer.apple.com/documentation/appkit/nsview/1483406-convertpoint) |
| [convertRect:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483785-convert) | [convertRect:toView:](https://developer.apple.com/documentation/appkit/nsview/1483217-convert) |
| [convertSize:fromView:](https://developer.apple.com/documentation/appkit/nsview/1483307-convert) | [convertSize:toView:](https://developer.apple.com/documentation/appkit/nsview/1483744-convertsize) |

The `convert...:fromView:` methods convert values to the receiver’s coordinate system from the coordinate system of the view passed as the second parameter. If you pass `nil` as the view, the values are assumed to be in the window coordinate system and are converted to the receiver coordinate system. The `convert..:toView:` methods perform the inverse operation—converting values in the receiver coordinate system to the coordinate system of the view passed as a parameter. If the `view` parameter is `nil`, the values are converted to the coordinate system of the receiver’s window.

`NSView` also defines the [centerScanRect:](https://developer.apple.com/documentation/appkit/nsview/1483725-centerscanrect) method, which converts a given rectangle to device coordinates, adjusts the rectangle to lie in the center of the area (pixels), and then converts the resulting rectangle back to the receiver’s coordinate system (points). Although this method works well for high resolution, some situations might require more precise control over the rounding behavior of the alignment operation on each edge of a rectangle. If you need a high level of control, consider using [backingAlignedRect:options:](https://developer.apple.com/documentation/appkit/nsview/1483321-backingalignedrect) (see [Aligning a Rectangle on Pixel Boundaries](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknlts)).

For more information about coordinate conversion in views, see:

- [Working with the View Hierarchy](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaViewsGuide/WorkingWithAViewHierarchy/WorkingWithAViewHierarchy.html#//apple_ref/doc/uid/TP40002978-CH4) in _[View Programming Guide](../../Cocoa/View%20Programming%20Guide/Introduction%20to%20View%20Programming%20Guide%20for%20Cocoa.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdsnzy)_
- [Coordinate Systems and Transforms](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CocoaDrawingGuide/Transforms/Transforms.html#//apple_ref/doc/uid/TP40003290-CH204) in _[Cocoa Drawing Guide](../../Cocoa/Cocoa%20Drawing%20Guide/Introduction%20to%20Cocoa%20Drawing%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazteojq)_

The [NSView](https://developer.apple.com/documentation/appkit/nsview) class provides methods for converting between a view’s local coordinate system and the interior coordinate system of the layer (for layer-backed views). Use these methods when you have custom layer trees and need to position the layers appropriately in the parent view.

The coordinate system of a layer that backs an `NSView` object is not necessarily identical to its local view coordinate system. For example, Core Animation layers always use an unflipped coordinate system, whereas the `NSView` class allows a given view class to choose whether or not it is flipped. For the case of a flipped `NSView` object that is layer-backed, the following conversion methods account for this difference.

| Convert to the view’s layer coordinate system | Convert from the view’s layer coordinate system |
| --- | --- |
| [convertPointToLayer:](https://developer.apple.com/documentation/appkit/nsview/1483315-convertpointtolayer) | [convertPointFromLayer:](https://developer.apple.com/documentation/appkit/nsview/1483554-convertpointfromlayer) |
| [convertSizeToLayer:](https://developer.apple.com/documentation/appkit/nsview/1483701-convertsizetolayer) | [convertSizeFromLayer:](https://developer.apple.com/documentation/appkit/nsview/1483479-convertsizefromlayer) |
| [convertRectToLayer:](https://developer.apple.com/documentation/appkit/nsview/1483776-converttolayer) | [convertRectFromLayer:](https://developer.apple.com/documentation/appkit/nsview/1483404-convertrectfromlayer) |

The [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class provides these methods for converting between window local coordinates and screen global coordinates:

- [convertRectToScreen:](https://developer.apple.com/documentation/appkit/nswindow/1419286-convertrecttoscreen)
- [convertRectFromScreen:](https://developer.apple.com/documentation/appkit/nswindow/1419603-convertfromscreen)

Use them instead of the deprecated [convertBaseToScreen:](https://developer.apple.com/documentation/appkit/nswindow/1419550-convertbasetoscreen) and [convertScreenToBase:](https://developer.apple.com/documentation/appkit/nswindow/1419414-convertscreentobase) methods.

Views, windows, and screens each have their own backing coordinate system. In other words, backing store coordinates are relative to an object; they do not refer to absolute positions onscreen. By default, coordinate values increase up and to the right in coordinate system units.

The backing coordinate system is suitable for pixel alignment for that specific object. Always use the same object for round-tripping to and from the backing store.

Each of the following methods converts between the object’s local coordinate system and a pixel-aligned coordinate system that matches the characteristics of the backing store for that object. In the case of the `NSScreen` class, the backing coordinate system is the native frame buffer of the display.

For more information on each method, see the appropriate reference documentation (_[NSView Class Reference](https://developer.apple.com/documentation/appkit/nsview)_, _[NSWindow Class Reference](https://developer.apple.com/documentation/appkit/nswindow)_, _[NSScreen Class Reference](https://developer.apple.com/documentation/appkit/nsscreen)_.

| Convert to backing store coordinates | Convert from backing store coordinates |
| --- | --- |
| [convertPointToBacking:](https://developer.apple.com/documentation/appkit/nsview/1483803-converttobacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview)) | [convertPointFromBacking:](https://developer.apple.com/documentation/appkit/nsview/1483456-convertpointfrombacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview)) |
| [convertSizeToBacking:](https://developer.apple.com/documentation/appkit/nsview/1483227-convertsizetobacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview)) | [convertSizeFromBacking:](https://developer.apple.com/documentation/appkit/nsview/1483319-convertfrombacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview)) |
| [convertRectToBacking:](https://developer.apple.com/documentation/appkit/nsview/1483648-convertrecttobacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview))  [convertRectToBacking:](https://developer.apple.com/documentation/appkit/nswindow/1419260-converttobacking) ([NSWindow](https://developer.apple.com/documentation/appkit/nswindow))  [convertRectToBacking:](https://developer.apple.com/documentation/appkit/nsscreen/1388389-convertrecttobacking) ([NSScreen](https://developer.apple.com/documentation/appkit/nsscreen)) | [convertRectFromBacking:](https://developer.apple.com/documentation/appkit/nsview/1483819-convertrectfrombacking) ([NSView](https://developer.apple.com/documentation/appkit/nsview))  [convertRectFromBacking:](https://developer.apple.com/documentation/appkit/nswindow/1419273-convertfrombacking) ([NSWindow](https://developer.apple.com/documentation/appkit/nswindow))  [convertRectFromBacking:](https://developer.apple.com/documentation/appkit/nsscreen/1388364-convertrectfrombacking) ([NSScreen](https://developer.apple.com/documentation/appkit/nsscreen)) |

Achieving consistent pixel alignment for high resolution often requires more control over rounding behaviors than the `NSView` class [centerScanRect:](https://developer.apple.com/documentation/appkit/nsview/1483725-centerscanrect) method offers. The `NSView`, `NSWindow`, and `NSScreen` classes all provide a `backingAlignedRect:options:` method.

The `backingAlignedRect:options:` method accepts rectangles in local coordinates and ensures that the result is aligned on backing store pixel boundaries, subject to specific rounding hints given in the `options` argument. Use [NSAlignmentOptions](https://developer.apple.com/documentation/foundation/nsalignmentoptions) constants to specify how to treat each edge of the rectangle. You can push a rectangle’s width and height to the next inward, outward, or closest pixel boundary.

For example, this code:

```
NSRect rect = {0.3,0.3,10.0,10.0};
NSAlignmentOptions alignOpts = NSAlignMinXOutward | NSAlignMinYOutward |
                               NSAlignWidthOutward | NSAlignMaxYOutward ;
NSRect alignedRect = [self backingAlignedRect:rect options:alignOpts];
```

produces a rectangle with this origin and size:

```
{{0, 0}, {10, 11}}
```

For a complete list of options, see [NSAlignmentOptions](https://developer.apple.com/documentation/foundation/nsalignmentoptions) in _[Foundation Constants Reference](https://developer.apple.com/documentation/foundation/foundation_constants)_.

Objects in an app, such as custom layers, windows, and screens, might not have the same resolution. When you need to find out scaling information for an object, choose the API that’s appropriate for that object.

The [contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale) property of the [CALayer](https://developer.apple.com/documentation/quartzcore/calayer) class defines the mapping between the coordinate space of the layer (measured in points) and the backing store (measured in pixels). You can change this value as needed to indicate to Core Animation that the bitmap of the backing layer needs to be bigger or smaller.

For example, to avoid blurry text for a layer that is magnified when composited to the screen, use the [contentsScale](https://developer.apple.com/documentation/quartzcore/calayer/1410746-contentsscale) property to specify a text-layer bitmap at twice the layer size, with mipmaps enabled.

The [backingScaleFactor](https://developer.apple.com/documentation/appkit/nsscreen/1388385-backingscalefactor) method of the [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) class returns the scale factor that represents the number of backing store pixels that correspond to each linear unit in screen space on the `NSScreen` object. You should not use this method except in the rare case when the explicit scale factor is needed. Instead, use the backing store conversion methods (see [Converting to and from the Backing Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknltk)).

Note that the value returned by [backingScaleFactor](https://developer.apple.com/documentation/appkit/nsscreen/1388385-backingscalefactor) does not represent anything concrete, such as pixel density or physical size, because it can vary based on the configured display mode. For example, the display might be in a mirrored configuration that is still scaled for high resolution, resulting in pixel geometry that might not match the native resolution of the display device.

The [backingScaleFactor](https://developer.apple.com/documentation/appkit/nswindow/1419459-backingscalefactor) method of the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class returns the scale factor for a specific window. As with its [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) counterpart, it is preferable that you use the backing store conversion methods.

The preferred way to get the scaling information for a CGContext object is to call the conversion function [CGContextConvertRectToDeviceSpace](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac):

```
deviceRect = CGContextConvertRectToDeviceSpace(context, userRect);
```

Then you can divide `deviceRect.size.height` by `userRect.size.height`. This works for both implicitly scaled window contexts and explicitly scaled bitmap contexts.

An alternative is to get the transform applied to the CGContext object by calling the function [CGContextGetUserSpaceToDeviceSpaceTransform](https://developer.apple.com/documentation/coregraphics/cgcontext/1455677-userspacetodevicespacetransform). The scaling information is in the `a` and `d` components of the returned transform. For example:

```
CGAffineTransform  deviceTransform =
        CGContextGetUserSpaceToDeviceSpaceTransform(myContext);
NSLog(@"x-scaling = %f y-scaling = %f", deviceTransform.a, deviceTransform.d);
```

If you applied any additional scaling to the context, that will be reflected in the values. Note that this function reports a scale for the implicitly scaled window contexts, and it does not handle bitmap contexts because those are not implicitly scaled.

For simple conversions between user space and device space, you can also use one of the conversion functions listed below (for details, see _[CGContext Reference](https://developer.apple.com/documentation/coregraphics/cgcontext)_). However, they convert only global coordinates, so you need to perform additional calculations to translate the results to view-centric coordinates.

- [CGContextConvertPointToDeviceSpace](https://developer.apple.com/documentation/coregraphics/cgcontext/1455916-converttodevicespace) and [CGContextConvertPointToUserSpace](https://developer.apple.com/documentation/coregraphics/cgcontext/1456451-converttouserspace)
- [CGContextConvertSizeToDeviceSpace](https://developer.apple.com/documentation/coregraphics/1456619-cgcontextconvertsizetodevicespac)e and [CGContextConvertSizeToUserSpace](https://developer.apple.com/documentation/coregraphics/1456510-cgcontextconvertsizetouserspace)
- [CGContextConvertRectToDeviceSpace](https://developer.apple.com/documentation/coregraphics/1456017-cgcontextconvertrecttodevicespac) and [CGContextConvertRectToUserSpace](https://developer.apple.com/documentation/coregraphics/cgcontext/1454165-converttouserspace)

When drawing images, the system needs to know about the source and destination resolution in order to apply the appropriate scaling. For that reason, you should use methods that provide information about the source rectangle.

When working with [NSImage](https://developer.apple.com/documentation/appkit/nsimage) objects, choose one of these methods, which allow you to specify a source rectangle. That method will then draw all or part of the image in the current coordinate system:

- [drawAtPoint:fromRect:operation:fraction:](https://developer.apple.com/documentation/appkit/nsimage/1519981-draw)
- [drawInRect:fromRect:operation:fraction:](https://developer.apple.com/documentation/appkit/nsimage/1520067-drawinrect)
- [drawInRect:fromRect:operation:fraction:respectFlipped:hints:](https://developer.apple.com/documentation/appkit/nsimage/1520043-drawinrect)

[NSImage](https://developer.apple.com/documentation/appkit/nsimage) drawing methods whose names do not begin with “draw” are deprecated (see [Deprecated APIs](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknltcmy)).

When working with a Core Image context, use the method [drawImage:inRect:fromRect:](https://developer.apple.com/documentation/coreimage/cicontext/1437786-drawimage) and specify the exact bounds of the destination. If the you create the [CIContext](https://developer.apple.com/documentation/coreimage/cicontext) object with a `CGContextRef`, the `inRect:` parameter is in points. If you create the [CIContext](https://developer.apple.com/documentation/coreimage/cicontext) object with a `CGLContext` object, the `inRect:` parameter is in pixels. The `fromRect:` parameter is always in pixel dimensions.

Do not use [drawImage:atPoint:fromRect:](https://developer.apple.com/documentation/coreimage/cicontext/1473521-drawimage) because this method is ambiguous as to the units of the dimensions, so it might not work as expected in a high-resolution environment.

The default behavior for `NSImage` is to choose the smallest image representation that has at least as many pixels as the destination rectangle on both the horizontal and vertical axes. The default works well for most cases. If you find the default doesn’t work well for your app, use the `matchesOnlyOnBestFittingAxis` property of the [NSImage](https://developer.apple.com/documentation/appkit/nsimage) class to adjust the image-choosing behavior.

**`-(BOOL)matchesOnlyOnBestFittingAxis`**
: Controls how `NSImage` chooses an image representation for a destination rectangle. Returns the current setting. The default setting is `NO`. When set to `YES`, `NSImage` chooses the smallest image representation that has at least as many pixels as the destination rectangle on either the horizontal or vertical axis.

**`setMatchesOnlyOnBestFittingAxis:`**
: Sets the property that controls how `NSImage` chooses an image representation for a destination rectangle.

Use the following to manage content and scale for custom Core Animation layers.

**`layerContentsForContentsScale:`**
: Provides the contents for a layer at a given scale.

**`recommendedLayerContentsScale:`**
: Provides the system with the optimal scaling to use for a layer.

For more details, see [Handle Dynamic Changes in Window Resolution Only When You Must](Advanced%20Optimization%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqmjqfvjvomrq) and [Manage Core Animation Layer Contents and Scale](Advanced%20Optimization%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqmjqfvjvomrx).

**`NSLayerDelegateContentsScaleUpdating`**
: This protocol defines an optional `CALayer` delegate method for handling resolution changes, allowing you to manage scale and contents for a layer hosted in a view.

**`layer:shouldInheritContentsScale:fromWindow:`**
: Invoked when a resolution changes occurs for the window that hosts the layer.

**`viewDidChangeBackingProperties`**
: Is invoked when the view’s backing properties change. The default implementation does nothing. Your app can provide an implementation if it needs to swap assets when a view’s backing properties change.

For more details, see [Handle Dynamic Changes in Window Resolution Only When You Must](Advanced%20Optimization%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqmjqfvjvomrq).

**`NSWindowDidChangeBackingPropertiesNotification`**
: Is sent when a window’s backing properties change.

**`windowDidChangeBackingProperties:`**
: Is invoked when the window’s backing properties change. The default implementation does nothing. Your app can provide an implementation if it needs to swap assets when a window’s backing properties change.

**`NSBackingPropertyOldColorSpaceKey`**
: Indicates the color space of the window prior to the change in backing store.

**`NSBackingPropertyOldScaleFactorKey`**
: Indicates the backing properties of the window prior to the change in backing store.

**`HIWindowGetBackingScaleFactor`**
: Replaces the `HIGetScaleFactor` function; see [Getting Scale Factors](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknltcni).

**`kHIWindowBitHighResolutionCapable`**
: Represents the bit that sets the high-resolution-capable attribute.

**`kWindowHighResolutionCapableAttribute`**
: Designates a window as being capable of supporting high-resolution content.

Use this method for offscreen drawing. See [Use the Block-Based Drawing Method for Offscreen Images](Advanced%20Optimization%20Techniques.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqmjqfvjvomzs).

**`+ (id)imageWithSize:(NSSize)size flipped:(BOOL)drawingHandlerShouldBeCalledWithFlippedContext drawingHandler:(BOOL (^)(NSRect dstRect))drawingHandler;`**
: The drawing handler is a block that can be invoked whenever the image is drawn to, and on whatever thread the drawing occurs. You should make sure that any state you access within the block is done in a thread-safe manner.

The code in the block is the same code that you would use between the [lockFocus](https://developer.apple.com/documentation/appkit/nsimage/1519891-lockfocus) and [unlockFocus](https://developer.apple.com/documentation/appkit/nsimage/1519853-unlockfocus) methods.

These functions return points (not pixels) as of OS X v10.8:

**`size_t CGDisplayModeGetWidth(CGDisplayModeRef mode);`**
: Returns the width in points of the specified display mode.

**`size_t CGDisplayModeGetHeight(CGDisplayModeRef mode);`**
: Returns the height in points of the specified display mode.

If your code uses any of the methods or constants listed in these sections, you need to replace them to allow your app to support high resolution.

The following methods of the [NSView](https://developer.apple.com/documentation/appkit/nsview) class are deprecated:

- [convertPointToBase:](https://developer.apple.com/documentation/appkit/nsview/1483362-convertpointtobase) and [convertPointFromBase:](https://developer.apple.com/documentation/appkit/nsview/1483778-convertpointfrombase)
- [convertSizeToBase:](https://developer.apple.com/documentation/appkit/nsview/1483349-convertsizetobase) and [convertSizeFromBase:](https://developer.apple.com/documentation/appkit/nsview/1483357-convertsizefrombase)
- [convertRectToBase:](https://developer.apple.com/documentation/appkit/nsview/1483331-convertrecttobase) and [convertRectFromBase:](https://developer.apple.com/documentation/appkit/nsview/1483591-convertrectfrombase)

The following methods of the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class are deprecated:

- [convertBaseToScreen:](https://developer.apple.com/documentation/appkit/nswindow/1419550-convertbasetoscreen) and [convertScreenToBase:](https://developer.apple.com/documentation/appkit/nswindow/1419414-convertscreentobase)

The appropriate replacement depends on the conversion you want to perform:

- To convert between view and layer coordinates, use the appropriate `convertXXXToLayer:` method. See [Converting to and from Layers](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknlto).
- To convert to window coordinates, use the appropriate `convertXXXToView:` method, specifying a `nil` view. See [Converting to and from Views](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknltc).

These are not compatible with the high-resolution model in OS X:

- The `userSpaceScaleFactor` methods of the [NSScreen](https://developer.apple.com/documentation/appkit/nsscreen) and [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) classes
- The `HIGetScaleFactor` function; use `HIWindowGetBackingScaleFactor` instead

The [NSUnscaledWindowMask](https://developer.apple.com/documentation/appkit/nsunscaledwindowmask) constant of the [NSWindow](https://developer.apple.com/documentation/appkit/nswindow) class is deprecated. This mask currently does nothing. The scale factor for a window backing store is dynamic and is dependent on the screen on which the window is placed. If you currently use this mask to achieve pixel-precise rendering, you should replace it with the backing store conversion methods (see [Converting to and from the Backing Store](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgezdgmbsfvbuqnjnknltk)).

The [NSImage](https://developer.apple.com/documentation/appkit/nsimage) class methods `compositeToPoint:...` and `dissolveToPoint:...` operate on the base coordinate system. The behavior of these methods is not compatible with high resolution in OS X because there is no way to specify the source rectangle.

Instead, you should use one of the methods that begin with `draw`, such as:

- [drawAtPoint:fromRect:operation:fraction:](https://developer.apple.com/documentation/appkit/nsimage/1519981-draw)
- [drawInRect:fromRect:operation:fraction:](https://developer.apple.com/documentation/appkit/nsimage/1520067-drawinrect)
- [drawInRect:fromRect:operation:fraction:respectFlipped:hints:](https://developer.apple.com/documentation/appkit/nsimage/1520043-drawinrect)

These methods allow you to specify a source rectangle, and they draw all or part of the image in the current coordinate system.

[Next](Testing%20and%20Troubleshooting%20High-Resolution%20Content.md)[Previous](Advanced%20Optimization%20Techniques.md)


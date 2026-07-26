---
title: 'UIGraphicsBeginImageContextWithOptions(_:_:_:)'
framework: UIKit
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 4.0+（27.0 起废弃）, iPadOS 4.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uigraphicsbeginimagecontextwithoptions(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uigraphicsbeginimagecontextwithoptions(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uigraphicsbeginimagecontextwithoptions%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:e63ecadcff05eb4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIGraphicsBeginImageContextWithOptions(_:_:_:)

<sub>Function</sub>

Creates a bitmap-based graphics context with the specified options.

> [!warning] Deprecated
> Use [UIGraphicsImageRenderer](uigraphicsimagerenderer.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```swift
func UIGraphicsBeginImageContextWithOptions(_ size: CGSize, _ opaque: Bool, _ scale: CGFloat)
```

## Parameters

- `size` — The size (measured in points) of the new bitmap context. This represents the size of the image returned by the [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) function. To get the size of the bitmap in pixels, you must multiply the width and height values by the value in the `scale` parameter.

- `opaque` — A Boolean flag indicating whether the bitmap is opaque. If you know the bitmap is fully opaque, specify [true](../swift/true.md) to ignore the alpha channel and optimize the bitmap’s storage. Specifying [false](../swift/false.md) means that the bitmap must include an alpha channel to handle any partially transparent pixels.

- `scale` — The scale factor to apply to the bitmap. If you specify a value of `0.0`, the scale factor is set to the scale factor of the device’s main screen.

## Discussion

You use this function to configure the drawing environment for rendering into a bitmap. The format for the bitmap is a ARGB 32-bit integer pixel format using host-byte order. If the opaque parameter is [true](../swift/true.md), the alpha channel is ignored and the bitmap is treated as fully opaque ([CGImageAlphaInfo.noneSkipFirst](../coregraphics/cgimagealphainfo/noneskipfirst.md) | [kCGBitmapByteOrder32Host](../coregraphics/kcgbitmapbyteorder32host.md)). Otherwise, each pixel uses a premultipled ARGB format ([CGImageAlphaInfo.premultipliedFirst](../coregraphics/cgimagealphainfo/premultipliedfirst.md) | [kCGBitmapByteOrder32Host](../coregraphics/kcgbitmapbyteorder32host.md)).

The environment also uses the default coordinate system for UIKit views, where the origin is in the upper-left corner and the positive axes extend down and to the right of the origin. The supplied scale factor is also applied to the coordinate system and resulting images. The drawing environment is pushed onto the graphics context stack immediately.

While the context created by this function is the current context, you can call the [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) function to retrieve an image object based on the current contents of the context. When you are done modifying the context, you must call the [UIGraphicsEndImageContext](<uigraphicsendimagecontext().md>) function to clean up the bitmap drawing environment and remove the graphics context from the top of the context stack. You should not use the [UIGraphicsPopContext](<uigraphicspopcontext().md>) function to remove this type of context from the stack.

In most other respects, the graphics context created by this function behaves like any other graphics context. You can change the context by pushing and popping other graphics contexts. You can also get the bitmap context using the [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) function.

This function may be called from any thread of your app.

## See Also

### Related Documentation

- [UIGraphicsEndImageContext](<uigraphicsendimagecontext().md>) — Removes the current bitmap-based graphics context from the top of the stack. _(deprecated)_
- [UIGraphicsGetImageFromCurrentImageContext](<uigraphicsgetimagefromcurrentimagecontext().md>) — Returns an image from the contents of the current bitmap-based graphics context. _(deprecated)_

### Graphics context primitives

- [UIGraphicsGetCurrentContext](<uigraphicsgetcurrentcontext().md>) — Returns the current graphics context.
- [UIGraphicsPushContext](<uigraphicspushcontext(__).md>) — Makes the specified graphics context the current context.
- [UIGraphicsPopContext](<uigraphicspopcontext().md>) — Removes the current graphics context from the top of the stack, restoring the previous context.
- [UIRectClip](<uirectclip(__).md>) — Modifies the current clipping path by intersecting it with the specified rectangle.

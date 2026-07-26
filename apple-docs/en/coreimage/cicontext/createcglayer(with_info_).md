---
title: 'createCGLayer(with:info:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.4+（10.11 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/createcglayer(with:info:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/createcglayer(with:info:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/createcglayer%28with%3Ainfo%3A%29.json'
content_hash: 'sha256:ffb7d18ef66ce2d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# createCGLayer(with:info:)

<sub>Instance Method</sub>

Creates a CGLayer object from the provided parameters.

<sub>macOS</sub>

```swift
func createCGLayer(with size: CGSize, info: CFDictionary?) -> CGLayer?
```

## Parameters

- `size` — The size, in default user space units, of the layer relative to the graphics context.

- `info` — A dictionary, which is passed to `CGLayerCreateWithContext` as the `auxiliaryInfo` parameter. Pass `NULL` because this parameter is reserved for future use.

## Return Value

A CGLayer object.

## Discussion

After calling this method, Core Image draws content into the CGLayer object. Core Image creates a CGLayer object by calling the Quartz 2D function [init(_:size:auxiliaryInfo:)](<../../coregraphics/cglayer/init(__size_auxiliaryinfo_).md>), whose prototype is:

```objc
CGLayerRef CGLayerCreateWithContext (
   CGContextRef context,
   CGSize size,
   CFDictionaryRef auxiliaryInfo
);
```

Core Image passes the [CIContext](../cicontext.md) object as the `context` parameter, the size as the `size` parameter, and the dictionary as the `auxiliaryInfo` parameter. For more information on CGLayer objects, see [Quartz 2D Programming Guide](https://developer.apple.com/library/archive/documentation/GraphicsImaging/Conceptual/drawingwithquartz2d/Introduction/Introduction.html#//apple_ref/doc/uid/TP30001066) and [CGLayer](../../coregraphics/cglayer.md).

## See Also

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [+ contextWithEAGLContext:options:](<init(eaglcontext_options_)-6uyqj.md>) — Creates a Core Image context from an EAGL context using the specified options. _(deprecated)_
- [init(forOfflineGPUAtIndex:)](<init(forofflinegpuatindex_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display. _(deprecated)_
- [init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_

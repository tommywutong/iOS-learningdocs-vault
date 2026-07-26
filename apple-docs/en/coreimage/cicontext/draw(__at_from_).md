---
title: 'draw(_:at:from:)'
framework: Core Image
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（6.0 起废弃）, iPadOS 5.0+（6.0 起废弃）, tvOS, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/draw(_:at:from:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/draw(_:at:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/draw%28_%3Aat%3Afrom%3A%29.json'
content_hash: 'sha256:cc378297d1fe378e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# draw(_:at:from:)

<sub>Instance Method</sub>

Renders a region of an image to a point in the context destination.

> [!warning] Deprecated
> Instead use [- drawImage:inRect:fromRect:](<draw(__in_from_).md>).

<sub>tvOS, visionOS</sub>

```swift
func draw(_ image: CIImage, at atPoint: CGPoint, from fromRect: CGRect)
```

## Parameters

- `image` — A Core Image image object.

- `atPoint` — The point in the context destination to draw to.

- `fromRect` — The region of the image to draw.

## Discussion

This method because it is ambiguous as to the units of the dimensions and won’t work as expected in a high-resolution environment which is why you should use `drawImage:inRect:fromRect:` instead.

On iOS platforms, this method draws the image onto a render buffer for the OpenGL ES context. Use this method only if the [CIContext](../cicontext.md) object is created with `contextWithEAGLContext:`, and hence, you are rendering to a CAEAGLLayer.

## See Also

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [+ contextWithEAGLContext:options:](<init(eaglcontext_options_)-6uyqj.md>) — Creates a Core Image context from an EAGL context using the specified options. _(deprecated)_
- [init(forOfflineGPUAtIndex:)](<init(forofflinegpuatindex_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display. _(deprecated)_
- [init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options. _(deprecated)_
- [- createCGLayerWithSize:info:](<createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_

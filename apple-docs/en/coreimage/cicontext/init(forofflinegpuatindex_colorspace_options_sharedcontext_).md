---
title: 'init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+（10.14 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(forofflinegpuatindex:colorspace:options:sharedcontext:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28forofflinegpuatindex%3Acolorspace%3Aoptions%3Asharedcontext%3A%29.json'
content_hash: 'sha256:374c526b3af09f51'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)

<sub>Initializer</sub>

Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options.

<sub>macOS</sub>

```swift
init?(forOfflineGPUAtIndex index: UInt32, colorSpace: CGColorSpace?, options: [CIContextOption : Any]? = nil, sharedContext: CGLContextObj?)
```

## Parameters

- `index` — The index of the offline GPU with which to create the context; a number between zero and the value returned by the [+ offlineGPUCount](<offlinegpucount().md>) method.

- `colorSpace` — A color space object encapsulating color space information that is used to specify how color values are interpreted.

- `options` — A dictionary that contains options for creating a [CIContext](../cicontext.md) object. You can pass any of the keys defined in [CIContextOption](../cicontextoption.md) along with the appropriate value.

- `sharedContext` — A CGL context with which to share OpenGL resources, obtained by calling the CGL function `CGLCreateContext(_:_:_:)`. Pass `NULL` to use a context that does not share OpenGL resources.

## Return Value

A Core Image context.

## Discussion

GPU devices that are not currently being used to drive a display can be used for Core Image rendering. Use the [+ offlineGPUCount](<offlinegpucount().md>) method to determine whether any such GPUs are available.

To create a Metal-based Core Image context using an offline GPU, use the [MTLCopyAllDevices()](<../../metal/mtlcopyalldevices().md>) function to list Metal devices, then choose a device without a display to pass to the [+ contextWithMTLDevice:](<init(mtldevice_)-swey.md>) method.

## See Also

### Deprecated

- [+ contextWithCGLContext:pixelFormat:colorSpace:options:](<init(cglcontext_pixelformat_colorspace_options_)-6rp6d.md>) — Creates a Core Image context from a CGL context, using the specified options, color space, and pixel format object. _(deprecated)_
- [+ contextWithEAGLContext:](<init(eaglcontext_)-8ajef.md>) — Creates a Core Image context from an EAGL context. _(deprecated)_
- [+ contextWithEAGLContext:options:](<init(eaglcontext_options_)-6uyqj.md>) — Creates a Core Image context from an EAGL context using the specified options. _(deprecated)_
- [init(forOfflineGPUAtIndex:)](<init(forofflinegpuatindex_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display. _(deprecated)_
- [- createCGLayerWithSize:info:](<createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_

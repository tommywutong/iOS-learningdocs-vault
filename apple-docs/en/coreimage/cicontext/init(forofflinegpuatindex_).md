---
title: 'init(forOfflineGPUAtIndex:)'
framework: Core Image
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.10+（10.14 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/coreimage/cicontext/init(forofflinegpuatindex:)'
source_url: 'https://developer.apple.com/documentation/coreimage/cicontext/init(forofflinegpuatindex:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coreimage/cicontext/init%28forofflinegpuatindex%3A%29.json'
content_hash: 'sha256:4b123528521c89d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Image](../../coreimage.md) · [CIContext](../cicontext.md)

# init(forOfflineGPUAtIndex:)

<sub>Initializer</sub>

Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display.

<sub>macOS</sub>

```swift
init?(forOfflineGPUAtIndex index: UInt32)
```

## Parameters

- `index` — The index of the offline GPU with which to create the context; a number between zero and the value returned by the [+ offlineGPUCount](<offlinegpucount().md>) method.

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
- [init(forOfflineGPUAtIndex:colorSpace:options:sharedContext:)](<init(forofflinegpuatindex_colorspace_options_sharedcontext_).md>) — Creates an OpenGL-based Core Image context using a GPU that is not currently driving a display, with the specified options. _(deprecated)_
- [- createCGLayerWithSize:info:](<createcglayer(with_info_).md>) — Creates a CGLayer object from the provided parameters. _(deprecated)_
- [- drawImage:atPoint:fromRect:](<draw(__at_from_).md>) — Renders a region of an image to a point in the context destination. _(deprecated)_

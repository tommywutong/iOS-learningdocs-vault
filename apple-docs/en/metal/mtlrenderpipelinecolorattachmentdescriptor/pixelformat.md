---
title: pixelFormat
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/pixelformat
source_url: 'https://developer.apple.com/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/pixelformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrenderpipelinecolorattachmentdescriptor/pixelformat.json'
content_hash: 'sha256:8e706b88a695fc70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderPipelineColorAttachmentDescriptor](../mtlrenderpipelinecolorattachmentdescriptor.md)

# pixelFormat

<sub>Instance Property</sub>

The pixel format of the color attachment’s texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var pixelFormat: MTLPixelFormat { get set }
```

## Discussion

The pixel format of the rendering pipeline state needs to be set to match the pixel format of the texture used by the selected color attachment; otherwise, an error occurs.

## See Also

### Related Documentation

- [Metal Shading Language Guide](https://developer.apple.com/library/archive/documentation/Metal/Reference/MetalShadingLanguageGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014364)
- [Metal Programming Guide](https://developer.apple.com/library/archive/documentation/Miscellaneous/Conceptual/MetalProgrammingGuide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40014221)

### Configuring render pipeline states

- [writeMask](writemask.md) — A bitmask that restricts which color channels are written into the texture.
- [MTLColorWriteMask](../mtlcolorwritemask.md) — Values used to specify a mask to permit or restrict writing to color channels of a color value.

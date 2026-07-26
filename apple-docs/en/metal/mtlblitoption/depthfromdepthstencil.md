---
title: depthFromDepthStencil
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitoption/depthfromdepthstencil
source_url: 'https://developer.apple.com/documentation/metal/mtlblitoption/depthfromdepthstencil'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitoption/depthfromdepthstencil.json'
content_hash: 'sha256:a07b692427c1a504'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitOption](../mtlblitoption.md)

# depthFromDepthStencil

<sub>Type Property</sub>

A blit option that copies the depth portion of a combined depth and stencil texture to or from a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var depthFromDepthStencil: MTLBlitOption { get }
```

## Discussion

You can pass this option to some methods that copy data between a buffer and a texture, including the following:

- [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](<../mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_options_).md>)
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](<../mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>)

## See Also

### Depth and stencil buffer options

- [MTLBlitOptionStencilFromDepthStencil](stencilfromdepthstencil.md) — A blit option that copies the stencil portion of a combined depth and stencil texture to or from a buffer.

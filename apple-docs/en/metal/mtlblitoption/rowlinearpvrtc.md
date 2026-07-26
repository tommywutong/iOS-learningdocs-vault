---
title: rowLinearPVRTC
framework: Metal
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlblitoption/rowlinearpvrtc
source_url: 'https://developer.apple.com/documentation/metal/mtlblitoption/rowlinearpvrtc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitoption/rowlinearpvrtc.json'
content_hash: 'sha256:412867836e1bb90a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitOption](../mtlblitoption.md)

# rowLinearPVRTC

<sub>Type Property</sub>

A blit option that copies PVRTC data between a texture and a buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static var rowLinearPVRTC: MTLBlitOption { get }
```

## Discussion

The PowerVR Texture Compression (PVRTC) format arranges blocks linearly in memory in row-major order, similar to other compressed texture formats. You can pass this option to some methods that copy data between a buffer and a texture, including the following:

- [- copyFromBuffer:sourceOffset:sourceBytesPerRow:sourceBytesPerImage:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:options:](<../mtlblitcommandencoder/copy(from_sourceoffset_sourcebytesperrow_sourcebytesperimage_sourcesize_to_destinationslice_destinationlevel_destinationorigin_options_).md>)
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toBuffer:destinationOffset:destinationBytesPerRow:destinationBytesPerImage:options:](<../mtlblitcommandencoder/copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationoffset_destinationbytesperrow_destinationbytesperimage_options_).md>)

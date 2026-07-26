---
title: 'copy(from:to:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlblitcommandencoder/copy(from:to:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlblitcommandencoder/copy(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlblitcommandencoder/copy%28from%3Ato%3A%29.json'
content_hash: 'sha256:2f81a6c12cb8dd79'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLBlitCommandEncoder](../mtlblitcommandencoder.md)

# copy(from:to:)

<sub>Instance Method</sub>

Encodes a command that copies data from one texture to another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(from sourceTexture: any MTLTexture, to destinationTexture: any MTLTexture)
```

## Parameters

- `sourceTexture` — A texture the command copies data from.

- `destinationTexture` — Another texture the command copies the data to that has the same pixel format and sample count as `sourceTexture`.

## Discussion

The textures can be different sizes as long as the larger texture has a mipmap level that’s the same size as the smaller texture’s level `0` mipmap.

The command copies all identical mipmap sizes. If both textures are arrays, the command copies as many texture slices (array elements) as possible.

## See Also

### Copying texture data to another texture

- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<copy(from_sourceslice_sourcelevel_to_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to another texture’s slices.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<copy(from_sourceslice_sourcelevel_sourceorigin_sourcesize_to_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a texture’s slice into another slice.
- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<copy(from_sourceorigin_sourcedimensions_to_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.

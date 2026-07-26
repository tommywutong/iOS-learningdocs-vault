---
title: 'copy(sourceTexture:destinationTexture:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:destinationtexture:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:destinationtexture:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourcetexture%3Adestinationtexture%3A%29.json'
content_hash: 'sha256:bbb9fd2de7b709b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceTexture:destinationTexture:)

<sub>Instance Method</sub>

Encodes a command that copies data from a texture to another.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceTexture: any MTLTexture, destinationTexture: any MTLTexture)
```

## Parameters

- `sourceTexture` — An [MTLTexture](../mtltexture.md) instance the command copies data from.

- `destinationTexture` — Another [MTLTexture](../mtltexture.md) instance the command copies the data into that has the same [pixelFormat](../mtltexture/pixelformat.md) and [sampleCount](../mtltexture/samplecount.md) as `sourceTexture`.

## See Also

### Encoding texture copy commands

- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<copy(sourcetensor_sourceorigin_sourcedimensions_destinationtensor_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<copy(sourcetexture_sourceslice_sourcelevel_destinationtexture_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to slices of another texture.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a slice of a texture into a slice of another texture.

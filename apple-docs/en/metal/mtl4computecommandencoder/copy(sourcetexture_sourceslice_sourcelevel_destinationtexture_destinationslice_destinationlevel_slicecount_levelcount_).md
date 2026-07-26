---
title: 'copy(sourceTexture:sourceSlice:sourceLevel:destinationTexture:destinationSlice:destinationLevel:sliceCount:levelCount:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetexture:sourceslice:sourcelevel:destinationtexture:destinationslice:destinationlevel:slicecount:levelcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourcetexture%3Asourceslice%3Asourcelevel%3Adestinationtexture%3Adestinationslice%3Adestinationlevel%3Aslicecount%3Alevelcount%3A%29.json'
content_hash: 'sha256:3a23967e048542d5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceTexture:sourceSlice:sourceLevel:destinationTexture:destinationSlice:destinationLevel:sliceCount:levelCount:)

<sub>Instance Method</sub>

Encodes a command that copies slices of a texture to slices of another texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceTexture: any MTLTexture, sourceSlice: Int, sourceLevel: Int, destinationTexture: any MTLTexture, destinationSlice: Int, destinationLevel: Int, sliceCount: Int, levelCount: Int)
```

## Parameters

- `sourceTexture` — A [MTLTexture](../mtltexture.md) texture that the command copies data from. To read the source texture contents, you need to set its [framebufferOnly](../mtltexture/isframebufferonly.md) property to [false](../../swift/false.md) prior to drawing into it.

- `sourceSlice` — A slice within `sourceTexture` the command uses as a starting point to copy data from. Set this to `0` if `sourceTexture` isn’t a texture array or a cube texture.

- `sourceLevel` — A mipmap level within `sourceTexture`.

- `destinationTexture` — Another [MTLTexture](../mtltexture.md) the command copies the data to that has the same [pixelFormat](../mtltexture/pixelformat.md) and [sampleCount](../mtltexture/samplecount.md) as `sourceTexture`. To write the contents into this texture, you need to set its [framebufferOnly](../mtltexture/isframebufferonly.md) property to [false](../../swift/false.md).

- `destinationSlice` — A slice within `destinationTexture` the command uses as its starting point for copying data to. Set this to `0` if `destinationTexture` isn’t a texture array or a cube texture.

- `destinationLevel` — A mipmap level within `destinationTexture`. The mipmap level you reference needs to have the same size as the `sourceTexture` slice’s mipmap at `sourceLevel`.

- `sliceCount` — The number of slices the command copies so that it satisfies the conditions that the sum of `sourceSlice` and `sliceCount` doesn’t exceed the number of slices in `sourceTexture` and the sum of `destinationSlice` and `sliceCount` doesn’t exceed the number of slices in `destinationTexture`.

- `levelCount` — The number of mipmap levels the command copies so that it satisfies the conditions that the sum of `sourceLevel` and `levelCount` doesn’t exceed the number of mipmap levels in `sourceTexture` and the sum of `destinationLevel` and `levelCount` doesn’t exceed the number of mipmap levels in `destinationTexture`.

## See Also

### Encoding texture copy commands

- [- copyFromTensor:sourceOrigin:sourceDimensions:toTensor:destinationOrigin:destinationDimensions:](<copy(sourcetensor_sourceorigin_sourcedimensions_destinationtensor_destinationorigin_destinationdimensions_).md>) — Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.
- [- copyFromTexture:toTexture:](<copy(sourcetexture_destinationtexture_).md>) — Encodes a command that copies data from a texture to another.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a slice of a texture into a slice of another texture.

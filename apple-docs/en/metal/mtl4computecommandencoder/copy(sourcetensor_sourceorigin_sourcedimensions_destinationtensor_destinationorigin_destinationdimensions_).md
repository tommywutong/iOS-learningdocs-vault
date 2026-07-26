---
title: 'copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:destinationtensor:destinationorigin:destinationdimensions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourcetensor%3Asourceorigin%3Asourcedimensions%3Adestinationtensor%3Adestinationorigin%3Adestinationdimensions%3A%29.json'
content_hash: 'sha256:dce0416196111433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceTensor:sourceOrigin:sourceDimensions:destinationTensor:destinationOrigin:destinationDimensions:)

<sub>Instance Method</sub>

Encodes a command to copy data from a slice of the data plane of a tensor into a slice of the data plane of another tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents)
```

## Parameters

- `sourceTensor` — A tensor instance the method copies data from.

- `sourceOrigin` — An array of per-dimension offsets that together locate the first element to copy in `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `sourceDimensions` — An array of per-dimension sizes that together define the extent of the slice to copy from `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sourceOrigin`.

- `destinationTensor` — A tensor instance the method copies data to.

- `destinationOrigin` — An array of per-dimension offsets that together locate the first element to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `destinationDimensions` — An array of per-dimension sizes that together define the extent of the slice to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `destinationOrigin`.

## Discussion

If `sourceTensor` and `destinationTensor` are not aliasable, this command applies a reshape operation.

Ensure the first dimension of `sourceOrigin`, `sourceDimensions`, `destinationOrigin`, and `destinationDimensions` is byte aligned.

## See Also

### Encoding texture copy commands

- [- copyFromTexture:toTexture:](<copy(sourcetexture_destinationtexture_).md>) — Encodes a command that copies data from a texture to another.
- [- copyFromTexture:sourceSlice:sourceLevel:toTexture:destinationSlice:destinationLevel:sliceCount:levelCount:](<copy(sourcetexture_sourceslice_sourcelevel_destinationtexture_destinationslice_destinationlevel_slicecount_levelcount_).md>) — Encodes a command that copies slices of a texture to slices of another texture.
- [- copyFromTexture:sourceSlice:sourceLevel:sourceOrigin:sourceSize:toTexture:destinationSlice:destinationLevel:destinationOrigin:](<copy(sourcetexture_sourceslice_sourcelevel_sourceorigin_sourcesize_destinationtexture_destinationslice_destinationlevel_destinationorigin_).md>) — Encodes a command that copies image data from a slice of a texture into a slice of another texture.

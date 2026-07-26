---
title: 'copy(sourceTensor:sourceOrigin:sourceDimensions:sourcePlane:destinationTensor:destinationOrigin:destinationDimensions:destinationPlane:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:sourceplane:destinationtensor:destinationorigin:destinationdimensions:destinationplane:)'
source_url: 'https://developer.apple.com/documentation/metal/mtl4computecommandencoder/copy(sourcetensor:sourceorigin:sourcedimensions:sourceplane:destinationtensor:destinationorigin:destinationdimensions:destinationplane:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtl4computecommandencoder/copy%28sourcetensor%3Asourceorigin%3Asourcedimensions%3Asourceplane%3Adestinationtensor%3Adestinationorigin%3Adestinationdimensions%3Adestinationplane%3A%29.json'
content_hash: 'sha256:560bb05e1d5ace70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTL4ComputeCommandEncoder](../mtl4computecommandencoder.md)

# copy(sourceTensor:sourceOrigin:sourceDimensions:sourcePlane:destinationTensor:destinationOrigin:destinationDimensions:destinationPlane:)

<sub>Instance Method</sub>

Encodes a command to copy data from a slice of a plane of a tensor into a slice of a plane of another tensor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func copy(sourceTensor: any MTLTensor, sourceOrigin: MTLTensorExtents, sourceDimensions: MTLTensorExtents, sourcePlane: MTLTensorPlaneType, destinationTensor: any MTLTensor, destinationOrigin: MTLTensorExtents, destinationDimensions: MTLTensorExtents, destinationPlane: MTLTensorPlaneType)
```

## Parameters

- `sourceTensor` — A tensor instance the method copies data from.

- `sourceOrigin` — An array of per-dimension offsets that together locate the first element to copy in `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `sourceDimensions` — An array of per-dimension sizes that together define the extent of the slice to copy from `sourceTensor`. Each element in this array corresponds to the dimension at the same index in `sourceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sourceOrigin`.

- `sourcePlane` — The plane the method copies data from.

- `destinationTensor` — A tensor instance the method copies data to.

- `destinationOrigin` — An array of per-dimension offsets that together locate the first element to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `destinationDimensions` — An array of per-dimension sizes that together define the extent of the slice to write in `destinationTensor`. Each element in this array corresponds to the dimension at the same index in `destinationOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `destinationOrigin`.

- `destinationPlane` — The plane the method copies data to.

## Discussion

If `sourceTensor` and `destinationTensor` are not aliasable, this command applies a reshape operation. For auxiliary planes, specify origin and dimensions in plane coordinates by applying the corresponding auxiliary plane’s block factors.

Ensure the first dimension of `sourceOrigin`, `sourceDimensions`, `destinationOrigin`, and `destinationDimensions` is byte aligned.

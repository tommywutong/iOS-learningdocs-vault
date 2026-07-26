---
title: 'getBytes(_:strides:sliceOrigin:sliceDimensions:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/getbytes(_:strides:sliceorigin:slicedimensions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/getbytes%28_%3Astrides%3Asliceorigin%3Aslicedimensions%3A%29.json'
content_hash: 'sha256:97502f92cdad2308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# getBytes(_:strides:sliceOrigin:sliceDimensions:)

<sub>Instance Method</sub>

Copies data from a slice of the data plane of this tensor into a pointer you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func getBytes(_ bytes: UnsafeMutableRawPointer, strides: MTLTensorExtents, sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents)
```

## Parameters

- `bytes` — A pointer to bytes of data that this method copies the slice into.

- `strides` — An array of strides, in elements, that describes the layout of the data in `bytes`.

- `sliceOrigin` — An array of per-dimension offsets that together locate the first element to copy in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `sliceDimensions` — An array of per-dimension sizes that together define the extent of the slice to copy from the tensor. Each element in this array corresponds to the dimension at the same index in `sliceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sliceOrigin`.

## Discussion

Create the tensor with [MTLResourceStorageModeShared](../mtlresourceoptions/storagemodeshared.md) for CPU access via this method.

Strides need to be monotonically non-decreasing: for any `i > 0`, `strides[i] >= strides[i-1] * dimensions[i-1]`.

The first dimension of `sliceOrigin` and `sliceDimensions` needs to be byte aligned.

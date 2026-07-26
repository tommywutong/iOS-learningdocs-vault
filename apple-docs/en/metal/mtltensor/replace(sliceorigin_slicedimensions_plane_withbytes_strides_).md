---
title: 'replace(sliceOrigin:sliceDimensions:plane:withBytes:strides:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, occ]
beta: true
deprecated: false
doc_path: '/documentation/metal/mtltensor/replace(sliceorigin:slicedimensions:plane:withbytes:strides:)'
source_url: 'https://developer.apple.com/documentation/metal/mtltensor/replace(sliceorigin:slicedimensions:plane:withbytes:strides:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtltensor/replace%28sliceorigin%3Aslicedimensions%3Aplane%3Awithbytes%3Astrides%3A%29.json'
content_hash: 'sha256:7a94b8ad98ec1f20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLTensor](../mtltensor.md)

# replace(sliceOrigin:sliceDimensions:plane:withBytes:strides:)

<sub>Instance Method</sub>

Replaces a slice of a plane of this tensor with data from a pointer you provide.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func replace(sliceOrigin: MTLTensorExtents, sliceDimensions: MTLTensorExtents, plane: MTLTensorPlaneType, withBytes bytes: UnsafeRawPointer, strides: MTLTensorExtents)
```

## Parameters

- `sliceOrigin` — An array of per-dimension offsets that together locate the first element to write to in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceDimensions`. Each offset value represents the number of elements from the start of that dimension.

- `sliceDimensions` — An array of per-dimension sizes that together define the extent of the slice to write to in the tensor. Each element in this array corresponds to the dimension at the same index in `sliceOrigin`. Each size value represents the number of elements to include along that dimension, starting from the corresponding offset in `sliceOrigin`.

- `plane` — The plane the method writes data to.

- `bytes` — A pointer to bytes of data to copy into the slice.

- `strides` — An array of strides, in elements, that describes the layout of the data in `bytes`.

## Discussion

When writing to auxiliary planes, specify `sliceOrigin` and `sliceDimensions` in plane coordinates by applying the auxiliary plane’s block factors.

Create the tensor with [MTLResourceStorageModeShared](../mtlresourceoptions/storagemodeshared.md) for CPU access via this method.

Strides need to be monotonically non-decreasing: for any `i > 0`, `strides[i] >= strides[i-1] * dimensions[i-1]`.

The first dimension of `sliceOrigin` and `sliceDimensions` needs to be byte aligned.

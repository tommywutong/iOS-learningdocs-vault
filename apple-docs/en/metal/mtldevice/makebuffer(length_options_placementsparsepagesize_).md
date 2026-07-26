---
title: 'makeBuffer(length:options:placementSparsePageSize:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makebuffer(length:options:placementsparsepagesize:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makebuffer(length:options:placementsparsepagesize:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makebuffer%28length%3Aoptions%3Aplacementsparsepagesize%3A%29.json'
content_hash: 'sha256:83a3d6acdb85915f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeBuffer(length:options:placementSparsePageSize:)

<sub>Instance Method</sub>

Creates a new placement sparse buffer of a specific length.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = [], placementSparsePageSize: MTLSparsePageSize) -> (any MTLBuffer)?
```

## Parameters

- `length` — The size of the [MTLBuffer](../mtlbuffer.md), in bytes.

- `options` — A [MTLResourceOptions](../mtlresourceoptions.md) instance that establishes the buffer’s storage modes.

- `placementSparsePageSize` — [MTLSparsePageSize](../mtlsparsepagesize.md) to use for the placement sparse buffer.

## Return Value

A [MTLBuffer](../mtlbuffer.md) instance, or `nil` if the function failed.

## Discussion

This method creates a new placement sparse [MTLBuffer](../mtlbuffer.md) of a specific length. You assign memory to placement sparse buffers using a [MTLHeap](../mtlheap.md) of type [MTLHeapTypePlacement](../mtlheaptype/placement.md).

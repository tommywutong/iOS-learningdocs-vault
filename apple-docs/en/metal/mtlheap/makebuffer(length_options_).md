---
title: 'makeBuffer(length:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/makebuffer(length:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/makebuffer%28length%3Aoptions%3A%29.json'
content_hash: 'sha256:d992ea02f33eac4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# makeBuffer(length:options:)

<sub>Instance Method</sub>

Creates a buffer on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

## Parameters

- `length` — The size, in bytes, of the buffer.

- `options` — Options that describe the properties of the buffer.

## Return Value

A new buffer object backed by heap memory, or `nil` if the heap memory is full.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [MTLHeapTypeAutomatic](../mtlheaptype/automatic.md)
- The buffer’s storage mode option needs to match the heap’s [storageMode](storagemode.md) property
- The buffer’s CPU cache mode option needs to match the heap’s [cpuCacheMode](cpucachemode.md) property

## See Also

### Creating buffers from a heap

- [- newBufferWithLength:options:offset:](<makebuffer(length_options_offset_).md>) — Creates a buffer at a specified offset on the heap.

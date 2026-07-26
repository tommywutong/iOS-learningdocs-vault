---
title: 'makeBuffer(length:options:offset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlheap/makebuffer(length:options:offset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlheap/makebuffer(length:options:offset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlheap/makebuffer%28length%3Aoptions%3Aoffset%3A%29.json'
content_hash: 'sha256:59f063dbee9e4f15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLHeap](../mtlheap.md)

# makeBuffer(length:options:offset:)

<sub>Instance Method</sub>

Creates a buffer at a specified offset on the heap.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = [], offset: Int) -> (any MTLBuffer)?
```

## Parameters

- `length` — The size of the buffer, in bytes.

- `options` — Options that describe the properties of the buffer.

- `offset` — The distance, in bytes, to place the buffer relative to the start of the heap.

## Return Value

A new buffer, or `nil` if the heap is not a placement heap.

## Discussion

You can call the method with the following restrictions:

- The heap’s type needs to be [MTLHeapTypePlacement](../mtlheaptype/placement.md)
- The buffer’s storage mode option needs to match the heap’s [storageMode](storagemode.md) property
- The buffer’s CPU cache mode option needs to match the heap’s [cpuCacheMode](cpucachemode.md) property

Use the [- heapBufferSizeAndAlignWithLength:options:](<../mtldevice/heapbuffersizeandalign(length_options_).md>) method to determine the required size and alignment. If you don’t align the buffer correctly or it extends past the end of the heap, the behavior is undefined.

> [!note] Note
> The new buffer can implicitly alias the underlying memory of other resources already in the heap within the overlapping half-open range of `[offset, offset + requiredSize)`.

## See Also

### Creating buffers from a heap

- [- newBufferWithLength:options:](<makebuffer(length_options_).md>) — Creates a buffer on the heap.

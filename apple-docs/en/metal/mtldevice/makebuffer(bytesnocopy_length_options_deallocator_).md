---
title: 'makeBuffer(bytesNoCopy:length:options:deallocator:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makebuffer(bytesnocopy:length:options:deallocator:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makebuffer(bytesnocopy:length:options:deallocator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makebuffer%28bytesnocopy%3Alength%3Aoptions%3Adeallocator%3A%29.json'
content_hash: 'sha256:2c1506e42ed5f034'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeBuffer(bytesNoCopy:length:options:deallocator:)

<sub>Instance Method</sub>

Creates a buffer that wraps an existing contiguous memory allocation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(bytesNoCopy pointer: UnsafeMutableRawPointer, length: Int, options: MTLResourceOptions = [], deallocator: (@Sendable (UnsafeMutableRawPointer, Int) -> Void)? = nil) -> (any MTLBuffer)?
```

## Parameters

- `pointer` — A page-aligned pointer to the starting memory address.

- `length` — The size of the new buffer, in bytes, that results in a page-aligned region of memory.

- `options` — An [MTLResourceOptions](../mtlresourceoptions.md) instance that sets the buffer’s storage and hazard-tracking modes. See [Resource fundamentals](../resource-fundamentals.md) and [Setting resource storage modes](../setting-resource-storage-modes.md) for more information.

- `deallocator` — A block the framework invokes when it deallocates the buffer so that your app can release the underlying memory; otherwise `nil` to opt out.

## Return Value

A new [MTLBuffer](../mtlbuffer.md) instance if the method completes successfully; otherwise `nil`.

## Discussion

> [!important] Important
> The existing memory allocation needs to exist within a single virtual memory (VM) region.

## See Also

### Creating buffers

- [maxBufferLength](maxbufferlength.md) — The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [- newBufferWithLength:options:](<makebuffer(length_options_).md>) — Creates a buffer the method clears with zero values.
- [- newBufferWithBytes:length:options:](<makebuffer(bytes_length_options_).md>) — Allocates a new buffer of a given length and initializes its contents by copying existing data into it.

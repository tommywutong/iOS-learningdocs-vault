---
title: 'makeBuffer(bytes:length:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makebuffer(bytes:length:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makebuffer(bytes:length:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makebuffer%28bytes%3Alength%3Aoptions%3A%29.json'
content_hash: 'sha256:b439c64e9f11fc5a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeBuffer(bytes:length:options:)

<sub>Instance Method</sub>

Allocates a new buffer of a given length and initializes its contents by copying existing data into it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(bytes pointer: UnsafeRawPointer, length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

## Parameters

- `pointer` — A pointer to the starting memory address the method copies the initialization data from.

- `length` — The size of the new buffer, in bytes, and the number of bytes the method copies from `pointer`.

- `options` — An [MTLResourceOptions](../mtlresourceoptions.md) instance that sets the buffer’s storage and hazard-tracking modes. See [Resource fundamentals](../resource-fundamentals.md) and [Setting resource storage modes](../setting-resource-storage-modes.md) for more information.

## Return Value

A new [MTLBuffer](../mtlbuffer.md) instance if the method completes successfully; otherwise `nil`.

## See Also

### Creating buffers

- [maxBufferLength](maxbufferlength.md) — The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [- newBufferWithLength:options:](<makebuffer(length_options_).md>) — Creates a buffer the method clears with zero values.
- [- newBufferWithBytesNoCopy:length:options:deallocator:](<makebuffer(bytesnocopy_length_options_deallocator_).md>) — Creates a buffer that wraps an existing contiguous memory allocation.

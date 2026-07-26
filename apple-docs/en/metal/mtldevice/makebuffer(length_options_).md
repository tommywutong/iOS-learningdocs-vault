---
title: 'makeBuffer(length:options:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtldevice/makebuffer(length:options:)'
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/makebuffer(length:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/makebuffer%28length%3Aoptions%3A%29.json'
content_hash: 'sha256:9fd48ca02b950df3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# makeBuffer(length:options:)

<sub>Instance Method</sub>

Creates a buffer the method clears with zero values.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func makeBuffer(length: Int, options: MTLResourceOptions = []) -> (any MTLBuffer)?
```

## Parameters

- `length` — The size of the new buffer, in bytes.

- `options` — An [MTLResourceOptions](../mtlresourceoptions.md) instance that sets the buffer’s storage and hazard-tracking modes. See [Resource fundamentals](../resource-fundamentals.md) and [Setting resource storage modes](../setting-resource-storage-modes.md) for more information.

## Return Value

A new [MTLBuffer](../mtlbuffer.md) instance if the method completed successfully; otherwise `nil`.

## See Also

### Creating buffers

- [maxBufferLength](maxbufferlength.md) — The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.
- [- newBufferWithBytes:length:options:](<makebuffer(bytes_length_options_).md>) — Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [- newBufferWithBytesNoCopy:length:options:deallocator:](<makebuffer(bytesnocopy_length_options_deallocator_).md>) — Creates a buffer that wraps an existing contiguous memory allocation.

---
title: maxBufferLength
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/maxbufferlength
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/maxbufferlength'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/maxbufferlength.json'
content_hash: 'sha256:cb7b02dbe7bfa2ca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# maxBufferLength

<sub>Instance Property</sub>

The largest amount of memory, in bytes, that a GPU device can allocate to a buffer instance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var maxBufferLength: Int { get }
```

## Discussion

The property’s value is at least 256 MB (268,435,456 bytes).

## See Also

### Creating buffers

- [- newBufferWithLength:options:](<makebuffer(length_options_).md>) — Creates a buffer the method clears with zero values.
- [- newBufferWithBytes:length:options:](<makebuffer(bytes_length_options_).md>) — Allocates a new buffer of a given length and initializes its contents by copying existing data into it.
- [- newBufferWithBytesNoCopy:length:options:deallocator:](<makebuffer(bytesnocopy_length_options_deallocator_).md>) — Creates a buffer that wraps an existing contiguous memory allocation.

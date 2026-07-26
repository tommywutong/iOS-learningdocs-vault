---
title: 'setFragmentBuffer(_:offset:index:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentbuffer(_:offset:index:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbuffer(_:offset:index:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentbuffer%28_%3Aoffset%3Aindex%3A%29.json'
content_hash: 'sha256:8d3e7a56cde317ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentBuffer(_:offset:index:)

<sub>Instance Method</sub>

Assigns a buffer to an entry in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentBuffer(_ buffer: (any MTLBuffer)?, offset: Int, index: Int)
```

## Parameters

- `buffer` — An [MTLBuffer](../mtlbuffer.md) instance the command assigns to an entry in the fragment shader argument table for buffers.

- `offset` — An integer that represents the location, in bytes, from the start of `buffer` where the fragment shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `index` — An integer that represents the entry in the fragment shader argument table for buffers that stores a record of `buffer` and `offset`.

## Discussion

By default, the buffer at each index is `nil`.

## See Also

### Assigning buffers

- [setFragmentBuffers(_:offsets:range:)](<setfragmentbuffers(__offsets_range_).md>) — Assigns multiple buffers to a range of entries in the fragment shader argument table.
- [- setFragmentBytes:length:atIndex:](<setfragmentbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [- setFragmentBufferOffset:atIndex:](<setfragmentbufferoffset(__index_).md>) — Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.

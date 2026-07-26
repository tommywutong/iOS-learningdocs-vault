---
title: 'setFragmentBuffers(_:offsets:range:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.11+, tvOS 8.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlrendercommandencoder/setfragmentbuffers(_:offsets:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlrendercommandencoder/setfragmentbuffers%28_%3Aoffsets%3Arange%3A%29.json'
content_hash: 'sha256:95ba1429684071f7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLRenderCommandEncoder](../mtlrendercommandencoder.md)

# setFragmentBuffers(_:offsets:range:)

<sub>Instance Method</sub>

Assigns multiple buffers to a range of entries in the fragment shader argument table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func setFragmentBuffers(_ buffers: [(any MTLBuffer)?], offsets: [Int], range: Range<Int>)
```

## Parameters

- `buffers` — An array of [MTLBuffer](../mtlbuffer.md) instances the command assigns to entries in the fragment shader argument table for buffers.

- `offsets` — An array of integers. Each element represents the location, in bytes, from the start of the corresponding [MTLBuffer](../mtlbuffer.md) element in `buffers` where the fragment shader argument data begins. See the [Metal feature set tables (PDF)](https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf) to check for offset alignment requirements for buffers in `device` and `constant` address space.

- `range` — A span of integers that represent the entries in the fragment shader argument table for buffers. Each entry stores a record of the corresponding element in `buffers` and `offsets`.

## Discussion

By default, the buffer at each index is `nil`.

> [!note] Note
> The Objective-C version of this method is [setFragmentBuffers:offsets:withRange:](setfragmentbuffers_offsets_withrange_.md).

## See Also

### Assigning buffers

- [- setFragmentBuffer:offset:atIndex:](<setfragmentbuffer(__offset_index_).md>) — Assigns a buffer to an entry in the fragment shader argument table.
- [- setFragmentBytes:length:atIndex:](<setfragmentbytes(__length_index_).md>) — Creates a buffer from bytes and assigns it to an entry in the fragment shader argument table.
- [- setFragmentBufferOffset:atIndex:](<setfragmentbufferoffset(__index_).md>) — Updates an entry in the fragment shader argument table with a new location within the entry’s current buffer.

---
title: 'loadBytes(_:size:sourceHandle:sourceHandleOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/loadbytes(_:size:sourcehandle:sourcehandleoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/loadbytes%28_%3Asize%3Asourcehandle%3Asourcehandleoffset%3A%29.json'
content_hash: 'sha256:98a45ce0075171ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# loadBytes(_:size:sourceHandle:sourceHandleOffset:)

<sub>Instance Method</sub>

Encodes a command that loads data from a file handle into CPU-accessible memory buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func loadBytes(_ pointer: UnsafeMutableRawPointer, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

## Parameters

- `pointer` — A pointer to memory the method loads data into.

- `size` — The number of bytes the method loads from the file.

- `sourceHandle` — A handle to a source file.

- `sourceHandleOffset` — A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

### Loading assets

- [- loadBuffer:offset:size:sourceHandle:sourceHandleOffset:](<load(__offset_size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU buffer.
- [- loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:](<load(__slice_level_size_sourcebytesperrow_sourcebytesperimage_destinationorigin_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU texture.

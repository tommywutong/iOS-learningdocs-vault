---
title: 'load(_:offset:size:sourceHandle:sourceHandleOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/load(_:offset:size:sourcehandle:sourcehandleoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/load%28_%3Aoffset%3Asize%3Asourcehandle%3Asourcehandleoffset%3A%29.json'
content_hash: 'sha256:1a273f32b689b344'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# load(_:offset:size:sourceHandle:sourceHandleOffset:)

<sub>Instance Method</sub>

Encodes a command that loads data from a file handle into a GPU buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func load(_ buffer: any MTLBuffer, offset: Int, size: Int, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

## Parameters

- `buffer` — A buffer instance the method loads data into.

- `offset` — A starting location relative to the beginning of the buffer, in bytes, the method copies data to.

- `size` — The number of bytes the method loads from the file into the buffer.

- `sourceHandle` — A handle to a source file.

- `sourceHandleOffset` — A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

### Loading assets

- [- loadTexture:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:](<load(__slice_level_size_sourcebytesperrow_sourcebytesperimage_destinationorigin_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU texture.
- [- loadBytes:size:sourceHandle:sourceHandleOffset:](<loadbytes(__size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into CPU-accessible memory buffer.

---
title: 'load(_:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:)'
framework: Metal
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocommandbuffer/load(_:slice:level:size:sourcebytesperrow:sourcebytesperimage:destinationorigin:sourcehandle:sourcehandleoffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocommandbuffer/load%28_%3Aslice%3Alevel%3Asize%3Asourcebytesperrow%3Asourcebytesperimage%3Adestinationorigin%3Asourcehandle%3Asourcehandleoffset%3A%29.json'
content_hash: 'sha256:bcf87c9d358fdaf2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLIOCommandBuffer](../mtliocommandbuffer.md)

# load(_:slice:level:size:sourceBytesPerRow:sourceBytesPerImage:destinationOrigin:sourceHandle:sourceHandleOffset:)

<sub>Instance Method</sub>

Encodes a command that loads data from a file handle into a GPU texture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func load(_ texture: any MTLTexture, slice: Int, level: Int, size: MTLSize, sourceBytesPerRow: Int, sourceBytesPerImage: Int, destinationOrigin: MTLOrigin, sourceHandle: any MTLIOFileHandle, sourceHandleOffset: Int)
```

## Parameters

- `texture` — A texture instance the method loads data into.

- `slice` — A slice within the texture.

- `level` — A level within the texture.

- `size` — The region of the texture the method copies to.

- `sourceBytesPerRow` — The number of bytes in a row of data from the source file.

- `sourceBytesPerImage` — The number of bytes in an image from the source file.

- `destinationOrigin` — A starting location within the texture the method copies data to.

- `sourceHandle` — A handle to a source file.

- `sourceHandleOffset` — A starting location relative to the beginning of the file, in bytes, the method copies data from.

## See Also

### Loading assets

- [- loadBuffer:offset:size:sourceHandle:sourceHandleOffset:](<load(__offset_size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into a GPU buffer.
- [- loadBytes:size:sourceHandle:sourceHandleOffset:](<loadbytes(__size_sourcehandle_sourcehandleoffset_).md>) — Encodes a command that loads data from a file handle into CPU-accessible memory buffer.

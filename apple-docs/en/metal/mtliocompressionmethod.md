---
title: MTLIOCompressionMethod
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocompressionmethod
source_url: 'https://developer.apple.com/documentation/metal/mtliocompressionmethod'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocompressionmethod.json'
content_hash: 'sha256:0e5b37b4c9aecf1f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCompressionMethod

<sub>Enumeration</sub>

The compression codecs that Metal supports for input/output handles.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLIOCompressionMethod
```

## Overview

For more information on the individual codecs, see the [Algorithm](../compression/algorithm.md) enumeration in the [Compression](../compression.md) framework.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Compression codecs

- [MTLIOCompressionMethodZlib](mtliocompressionmethod/zlib.md) — Indicates that a file uses the zlib compression algorithm codec.
- [MTLIOCompressionMethodLZFSE](mtliocompressionmethod/lzfse.md) — Indicates that a file uses the LZFSE compression algorithm codec.
- [MTLIOCompressionMethodLZ4](mtliocompressionmethod/lz4.md) — Indicates that a file uses the LZ4 compression algorithm codec.
- [MTLIOCompressionMethodLZMA](mtliocompressionmethod/lzma.md) — Indicates that a file uses the LZMA compression algorithm codec.
- [MTLIOCompressionMethodLZBitmap](mtliocompressionmethod/lzbitmap.md) — Indicates that a file uses the LZBitmap compression algorithm codec.

### Initializers

- [init(rawValue:)](<mtliocompressionmethod/init(rawvalue_).md>)

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

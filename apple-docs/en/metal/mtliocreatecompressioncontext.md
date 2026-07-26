---
title: MTLIOCreateCompressionContext
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocreatecompressioncontext
source_url: 'https://developer.apple.com/documentation/metal/mtliocreatecompressioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocreatecompressioncontext.json'
content_hash: 'sha256:6f678b42a7cceb58'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCreateCompressionContext

<sub>Function</sub>

Creates a compression context that you use to compress data into a single file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```objc
extern MTLIOCompressionContextMTLIOCreateCompressionContext(const char *path, MTLIOCompressionMethod type, size_t chunkSize);
```

## Parameters

- `path` — A location in the file system where the function creates the new, compressed file.

- `type` — A compression codec the function uses to compress data resource file’s compression format.

- `chunkSize` — The number of uncompressed bytes the compression codec compresses at a time.

## See Also

### Asset compression

- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

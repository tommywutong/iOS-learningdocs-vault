---
title: 'MTLIOCreateCompressionContext(_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocreatecompressioncontext(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocreatecompressioncontext(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocreatecompressioncontext%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:5b64a1e5216263c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCreateCompressionContext(_:_:_:)

<sub>Function</sub>

Creates a compression context that you use to compress data into a single file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLIOCreateCompressionContext(_ path: String, _ type: MTLIOCompressionMethod, _ chunkSize: Int) -> MTLIOCompressionContext?
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

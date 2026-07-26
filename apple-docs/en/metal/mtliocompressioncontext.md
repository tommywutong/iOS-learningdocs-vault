---
title: MTLIOCompressionContext
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocompressioncontext
source_url: 'https://developer.apple.com/documentation/metal/mtliocompressioncontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocompressioncontext.json'
content_hash: 'sha256:92b2bc5ac14a9253'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCompressionContext

<sub>Type Alias</sub>

A pointer that represents the state of a file compression session in progress.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
typealias MTLIOCompressionContext = UnsafeMutableRawPointer
```

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

---
title: MTLIOCompressionContextDefaultChunkSize()
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocompressioncontextdefaultchunksize()
source_url: 'https://developer.apple.com/documentation/metal/mtliocompressioncontextdefaultchunksize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocompressioncontextdefaultchunksize%28%29.json'
content_hash: 'sha256:e395b5384383fef5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCompressionContextDefaultChunkSize()

<sub>Function</sub>

Returns a compression chunk size you can use as a default for creating a compression context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLIOCompressionContextDefaultChunkSize() -> Int
```

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

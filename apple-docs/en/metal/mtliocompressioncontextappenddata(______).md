---
title: 'MTLIOCompressionContextAppendData(_:_:_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtliocompressioncontextappenddata(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtliocompressioncontextappenddata(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocompressioncontextappenddata%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:d8c2012c18203031'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCompressionContextAppendData(_:_:_:)

<sub>Function</sub>

Adds data to a compression context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLIOCompressionContextAppendData(_ context: MTLIOCompressionContext, _ data: UnsafeRawPointer, _ size: Int)
```

## Parameters

- `context` — An [MTLIOCompressionContext](mtliocompressioncontext.md) instance that you create with the [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) function.

- `data` — A pointer to memory that contains the data the function adds to the compression context.

- `size` — The number of bytes the function adds to the compression context from the data pointer.

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

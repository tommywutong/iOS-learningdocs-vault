---
title: 'MTLIOFlushAndDestroyCompressionContext(_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlioflushanddestroycompressioncontext(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlioflushanddestroycompressioncontext(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlioflushanddestroycompressioncontext%28_%3A%29.json'
content_hash: 'sha256:647a6a7109005735'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOFlushAndDestroyCompressionContext(_:)

<sub>Function</sub>

Finishes compressing and saves the file that a compression context represents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func MTLIOFlushAndDestroyCompressionContext(_ context: MTLIOCompressionContext) -> MTLIOCompressionStatus
```

## Parameters

- `context` — A compression context that you create with the [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) function.

## Return Value

An [MTLIOCompressionStatus](mtliocompressionstatus.md) instance.

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOCompressionStatus](mtliocompressionstatus.md) — Represents the final state of a compression context.

---
title: MTLIOCompressionStatus
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtliocompressionstatus
source_url: 'https://developer.apple.com/documentation/metal/mtliocompressionstatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtliocompressionstatus.json'
content_hash: 'sha256:6f8a779d863298c7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLIOCompressionStatus

<sub>Enumeration</sub>

Represents the final state of a compression context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum MTLIOCompressionStatus
```

## Overview

The [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) returns an [MTLIOCompressionStatus](mtliocompressionstatus.md) instance to reflect the final state of a compression context.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Compression result states

- [MTLIOCompressionStatusComplete](mtliocompressionstatus/complete.md) — Indicates the compression API successfully flushed and destroyed a compression context.
- [MTLIOCompressionStatusError](mtliocompressionstatus/error.md) — Indicates the compression API had an error while flushing and destroying a compression context.

### Initializers

- [init(rawValue:)](<mtliocompressionstatus/init(rawvalue_).md>)

## See Also

### Asset compression

- [MTLIOCreateCompressionContext(_:_:_:)](<mtliocreatecompressioncontext(______).md>) — Creates a compression context that you use to compress data into a single file.
- [MTLIOCompressionMethod](mtliocompressionmethod.md) — The compression codecs that Metal supports for input/output handles.
- [MTLIOCompressionContextDefaultChunkSize](<mtliocompressioncontextdefaultchunksize().md>) — Returns a compression chunk size you can use as a default for creating a compression context.
- [MTLIOCompressionContext](mtliocompressioncontext.md) — A pointer that represents the state of a file compression session in progress.
- [MTLIOCompressionContextAppendData](<mtliocompressioncontextappenddata(______).md>) — Adds data to a compression context.
- [MTLIOFlushAndDestroyCompressionContext](<mtlioflushanddestroycompressioncontext(__).md>) — Finishes compressing and saves the file that a compression context represents.

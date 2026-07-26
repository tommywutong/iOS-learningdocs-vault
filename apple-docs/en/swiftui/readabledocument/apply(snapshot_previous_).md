---
title: 'apply(snapshot:previous:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/readabledocument/apply(snapshot:previous:)'
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument/apply(snapshot:previous:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument/apply%28snapshot%3Aprevious%3A%29.json'
content_hash: 'sha256:798dabed9a1e4c23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReadableDocument](../readabledocument.md)

# apply(snapshot:previous:)

<sub>Instance Method</sub>

Applies a loaded snapshot to the document model.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@MainActor func apply(snapshot: sending Self.Reader.Snapshot, previous: sending Self.Reader.Snapshot?) async throws
```

## Parameters

- `snapshot` — The content loaded from disk.

- `previous` — The previously loaded snapshot, or `nil` on the first read. Use it to apply incremental updates.

## Discussion

SwiftUI calls this on the main actor after the reader’s [read(from:progress:)](<../documentreader/read(from_progress_).md>) completes. Update your model properties here. Keep this method lightweight — all deserialization should happen in the reader.

## See Also

### Reading a document

- [readableContentTypes](readablecontenttypes.md) — The content types this document can open. _(beta)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [Reader](reader.md) — A type that implements reading from disk. _(beta)_
- [reader(configuration:)](<reader(configuration_).md>) — Creates a reader to load this document from disk. _(beta)_
- [writableContentTypes](writablecontenttypes.md) — By default, a document that supports reading also supports writing the same content types. _(beta)_

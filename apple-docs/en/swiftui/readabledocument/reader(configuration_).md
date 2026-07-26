---
title: 'reader(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/readabledocument/reader(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument/reader(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument/reader%28configuration%3A%29.json'
content_hash: 'sha256:5c2f54acd149ec0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReadableDocument](../readabledocument.md)

# reader(configuration:)

<sub>Instance Method</sub>

Creates a reader to load this document from disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func reader(configuration: sending Self.ReadConfiguration) -> sending Self.Reader
```

## Parameters

- `configuration` — The content type of the file being read.

## Discussion

SwiftUI calls this method each time it needs to read or re-read the document (on open, or when another process changes the file). Return a [FileWrapperDocumentReader](../filewrapperdocumentreader.md) for cases that don’t require custom reading logic, or a [DocumentReader](../documentreader.md) for direct URL access.

## See Also

### Reading a document

- [readableContentTypes](readablecontenttypes.md) — The content types this document can open. _(beta)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [Reader](reader.md) — A type that implements reading from disk. _(beta)_
- [apply(snapshot:previous:)](<apply(snapshot_previous_).md>) — Applies a loaded snapshot to the document model. _(beta)_
- [writableContentTypes](writablecontenttypes.md) — By default, a document that supports reading also supports writing the same content types. _(beta)_

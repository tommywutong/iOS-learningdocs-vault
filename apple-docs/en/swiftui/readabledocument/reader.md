---
title: Reader
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/readabledocument/reader
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument/reader'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument/reader.json'
content_hash: 'sha256:1e898ba8992bb8b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReadableDocument](../readabledocument.md)

# Reader

<sub>Associated Type</sub>

A type that implements reading from disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Reader : DocumentReader
```

## See Also

### Reading a document

- [readableContentTypes](readablecontenttypes.md) — The content types this document can open. _(beta)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [reader(configuration:)](<reader(configuration_).md>) — Creates a reader to load this document from disk. _(beta)_
- [apply(snapshot:previous:)](<apply(snapshot_previous_).md>) — Applies a loaded snapshot to the document model. _(beta)_
- [writableContentTypes](writablecontenttypes.md) — By default, a document that supports reading also supports writing the same content types. _(beta)_

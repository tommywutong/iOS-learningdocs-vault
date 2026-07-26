---
title: writableContentTypes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/readabledocument/writablecontenttypes
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument/writablecontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument/writablecontenttypes.json'
content_hash: 'sha256:5ad0e67d8bc9643d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReadableDocument](../readabledocument.md)

# writableContentTypes

<sub>Type Property</sub>

By default, a document that supports reading also supports writing the same content types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var writableContentTypes: [UTType] { get }
```

## See Also

### Reading a document

- [readableContentTypes](readablecontenttypes.md) — The content types this document can open. _(beta)_
- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [Reader](reader.md) — A type that implements reading from disk. _(beta)_
- [reader(configuration:)](<reader(configuration_).md>) — Creates a reader to load this document from disk. _(beta)_
- [apply(snapshot:previous:)](<apply(snapshot_previous_).md>) — Applies a loaded snapshot to the document model. _(beta)_

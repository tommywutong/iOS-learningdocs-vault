---
title: readableContentTypes
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/readabledocument/readablecontenttypes
source_url: 'https://developer.apple.com/documentation/swiftui/readabledocument/readablecontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/readabledocument/readablecontenttypes.json'
content_hash: 'sha256:787a17eb9061c108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [ReadableDocument](../readabledocument.md)

# readableContentTypes

<sub>Type Property</sub>

The content types this document can open.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var readableContentTypes: [UTType] { get }
```

## Discussion

The document browser and open panel use this list to filter which files the person can select.

## See Also

### Reading a document

- [ReadConfiguration](readconfiguration.md) — The configuration for reading document contents. _(beta)_
- [Reader](reader.md) — A type that implements reading from disk. _(beta)_
- [reader(configuration:)](<reader(configuration_).md>) — Creates a reader to load this document from disk. _(beta)_
- [apply(snapshot:previous:)](<apply(snapshot_previous_).md>) — Applies a loaded snapshot to the document model. _(beta)_
- [writableContentTypes](writablecontenttypes.md) — By default, a document that supports reading also supports writing the same content types. _(beta)_

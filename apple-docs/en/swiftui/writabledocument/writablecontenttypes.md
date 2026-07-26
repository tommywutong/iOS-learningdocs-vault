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
doc_path: /documentation/swiftui/writabledocument/writablecontenttypes
source_url: 'https://developer.apple.com/documentation/swiftui/writabledocument/writablecontenttypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writabledocument/writablecontenttypes.json'
content_hash: 'sha256:714d97fb0d6bf24f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WritableDocument](../writabledocument.md)

# writableContentTypes

<sub>Type Property</sub>

The content types this document can save or export to.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static var writableContentTypes: [UTType] { get }
```

## Discussion

The save panel uses this list to offer format options. When a document also conforms to [ReadableDocument](../readabledocument.md), the default implementation returns [readableContentTypes](../readabledocument/readablecontenttypes.md).

## See Also

### Writing a document

- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(beta)_
- [Writer](writer.md) — A type that implements writing to disk. _(beta)_
- [writer(configuration:)](<writer(configuration_).md>) — Creates a writer to save this document to disk. _(beta)_
- [snapshot(contentType:)](<snapshot(contenttype_).md>) — Captures the document’s current state for saving. _(beta)_

---
title: Writer
framework: SwiftUI
symbol_kind: associatedtype
role: symbol
role_heading: Associated Type
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/writabledocument/writer
source_url: 'https://developer.apple.com/documentation/swiftui/writabledocument/writer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writabledocument/writer.json'
content_hash: 'sha256:8e746fe3412efb50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WritableDocument](../writabledocument.md)

# Writer

<sub>Associated Type</sub>

A type that implements writing to disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
associatedtype Writer : DocumentWriter
```

## See Also

### Writing a document

- [writableContentTypes](writablecontenttypes.md) — The content types this document can save or export to. _(beta)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(beta)_
- [writer(configuration:)](<writer(configuration_).md>) — Creates a writer to save this document to disk. _(beta)_
- [snapshot(contentType:)](<snapshot(contenttype_).md>) — Captures the document’s current state for saving. _(beta)_

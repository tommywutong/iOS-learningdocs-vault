---
title: 'writer(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/writabledocument/writer(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/writabledocument/writer(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writabledocument/writer%28configuration%3A%29.json'
content_hash: 'sha256:c427207fb8948f0e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [WritableDocument](../writabledocument.md)

# writer(configuration:)

<sub>Instance Method</sub>

Creates a writer to save this document to disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func writer(configuration: sending Self.WriteConfiguration) -> sending Self.Writer
```

## Parameters

- `configuration` — The content type of the file being written.

## Discussion

Return a [FileWrapperDocumentWriter](../filewrapperdocumentwriter.md) for cases that don’t require custom writing logic, or a [DocumentWriter](../documentwriter.md) for direct URL access or streaming writes.

## See Also

### Writing a document

- [writableContentTypes](writablecontenttypes.md) — The content types this document can save or export to. _(beta)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(beta)_
- [Writer](writer.md) — A type that implements writing to disk. _(beta)_
- [snapshot(contentType:)](<snapshot(contenttype_).md>) — Captures the document’s current state for saving. _(beta)_

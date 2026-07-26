---
title: 'init(viewer:makeReadableDocument:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/documentgroup/init(viewer:makereadabledocument:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(viewer:makereadabledocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28viewer%3Amakereadabledocument%3A%29.json'
content_hash: 'sha256:3c8c7affd42d528b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(viewer:makeReadableDocument:)

<sub>Initializer</sub>

Creates a document group capable of opening and viewing read-only documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(@ContentBuilder viewer: @escaping (Document) -> Content, makeReadableDocument: @escaping @MainActor (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

## Parameters

- `viewer` — The viewing UI for the provided document.

## See Also

### Creating a document group

- [init(allowCreating:editor:makeDocument:)](<init(allowcreating_editor_makedocument_).md>) — Creates a document group capable of creating, viewing, and editing documents. _(beta)_

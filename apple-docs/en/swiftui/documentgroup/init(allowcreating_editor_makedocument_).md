---
title: 'init(allowCreating:editor:makeDocument:)'
framework: SwiftUI
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/documentgroup/init(allowcreating:editor:makedocument:)'
source_url: 'https://developer.apple.com/documentation/swiftui/documentgroup/init(allowcreating:editor:makedocument:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/documentgroup/init%28allowcreating%3Aeditor%3Amakedocument%3A%29.json'
content_hash: 'sha256:a996474ecb95c0f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [DocumentGroup](../documentgroup.md)

# init(allowCreating:editor:makeDocument:)

<sub>Initializer</sub>

Creates a document group capable of creating, viewing, and editing documents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated init(allowCreating: Bool = true, @ContentBuilder editor: @escaping (Document) -> Content, makeDocument: @escaping @MainActor (URLDocumentConfiguration, DocumentCreationContext) async throws -> Document)
```

## Parameters

- `allowCreating` — Whether the document group supports creating new documents in addition to opening and editing existing ones.

- `editor` — The editing UI for the provided document.

- `makeDocument` — A closure that creates the document instance. Throw `CancellationError` to indicate that document creation was cancelled.

## See Also

### Creating a document group

- [init(viewer:makeReadableDocument:)](<init(viewer_makereadabledocument_).md>) — Creates a document group capable of opening and viewing read-only documents. _(beta)_

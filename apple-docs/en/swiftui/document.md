---
title: Document
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/document
source_url: 'https://developer.apple.com/documentation/swiftui/document'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/document.json'
content_hash: 'sha256:87249130677f1a78'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# Document

<sub>Protocol</sub>

A document that supports both reading and writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol Document : ReadableDocument, WritableDocument
```

## Overview

`Document` is a convenience protocol that combines [ReadableDocument](readabledocument.md) and [WritableDocument](writabledocument.md). Conform to it when your document can both open and save files:

```swift
@Observable
final class TextDocument: Document {
    static let readableContentTypes = [UTType.plainText]

    var text: String = ""

    func reader(configuration: sending ReadConfiguration) -> sending FileWrapperDocumentReader<String> {
        FileWrapperDocumentReader(configuration) { fileWrapper in
            guard let data =
                fileWrapper.regularFileContents else {
                throw CocoaError(.fileReadCorruptFile)
            }
            return String(decoding: data, as: UTF8.self)
        }
    }

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String { text }

    @MainActor
    func apply(snapshot: sending String, previous: sending String?) async throws {
        text = snapshot
    }
}
```

Use [DocumentGroup](documentgroup.md) as your app’s first scene to opt into the document infrastructure (autosaving, file coordination, undo management, conflict resolution):

```swift
@main
struct MyApp: App {
    var body: some Scene {
        DocumentGroup { document in
            TextEditorView(document: document)
        } makeDocument: { configuration, context in
            TextDocument()
        }
    }
}
```

For a read-only document, conform only to [ReadableDocument](readabledocument.md).

The document can be `@MainActor` or nonisolated, `Sendable` or not — use whichever works best for the app.

## Relationships

- **Inherits From**: [ReadableDocument](readabledocument.md), [WritableDocument](writabledocument.md)

## See Also

### Storing document data in a reference type instance

- [ReadableDocument](readabledocument.md) — A document type that supports reading from file. _(beta)_
- [WritableDocument](writabledocument.md) — A document type that supports writing to file. _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — The configuration of an open document that stores its file URL, last modification date, and related metadata. _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — Context about how a document was created. _(beta)_
- [DocumentBaseBox](documentbasebox.md) — A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.

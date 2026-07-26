---
title: WritableDocument
framework: SwiftUI
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/swiftui/writabledocument
source_url: 'https://developer.apple.com/documentation/swiftui/writabledocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/writabledocument.json'
content_hash: 'sha256:99dccd6b5f8dffc0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# WritableDocument

<sub>Protocol</sub>

A document type that supports writing to file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
protocol WritableDocument : AnyObject
```

## Overview

Conform to `WritableDocument` to add save and export capabilities. Most documents also conform to [ReadableDocument](readabledocument.md) — use the [Document](document.md) protocol as a shorthand for both.

The document saving has three steps:

1. SwiftUI calls [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>) on the main actor.
2. SwiftUI calls [writer(configuration:)](<writabledocument/writer(configuration_).md>) to get a writer.
3. The writer’s `DocumentWriter/write(content:to:previous:progress:)` runs in the background with coordinated file access.

> [!important] Important
> Without registered undo actions, SwiftUI won’t trigger autosave. Register undo actions with the undo manager from the `View` environment for every user-facing change.

Example using [FileWrapperDocumentWriter](filewrapperdocumentwriter.md):

```swift
@Observable
final class NoteDocument: WritableDocument {
    static let writableContentTypes: [UTType] = [.markdown]

    var text = ""

    func writer(configuration: sending WriteConfiguration) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(
                regularFileWithContents: Data(snapshot.utf8)
            )
        }
    }

    @MainActor
    func snapshot(contentType: UTType) async throws -> sending String { text }
}
```

Register undo actions in the view using the environment’s `UndoManager`. This ensures SwiftUI detects unsaved changes and triggers autosave:

```swift
struct NoteEditorView: View {
    @Bindable var document: NoteDocument
    @Environment(\.undoManager) private var undoManager

    var body: some View {
        TextEditor(text: $document.text)
            .onChange(of: document.text) { oldValue, _ in
                undoManager?.registerUndo(
                    withTarget: document
                ) { document in
                    document.text = oldValue
                }
            }
    }
}
```

## Relationships

- **Inherited By**: [Document](document.md)

## Topics

### Writing a document

- [writableContentTypes](writabledocument/writablecontenttypes.md) — The content types this document can save or export to. _(beta)_
- [WriteConfiguration](writabledocument/writeconfiguration.md) — The configuration for writing document contents. _(beta)_
- [Writer](writabledocument/writer.md) — A type that implements writing to disk. _(beta)_
- [writer(configuration:)](<writabledocument/writer(configuration_).md>) — Creates a writer to save this document to disk. _(beta)_
- [snapshot(contentType:)](<writabledocument/snapshot(contenttype_).md>) — Captures the document’s current state for saving. _(beta)_

## See Also

### Storing document data in a reference type instance

- [Document](document.md) — A document that supports both reading and writing. _(beta)_
- [ReadableDocument](readabledocument.md) — A document type that supports reading from file. _(beta)_
- [URLDocumentConfiguration](urldocumentconfiguration.md) — The configuration of an open document that stores its file URL, last modification date, and related metadata. _(beta)_
- [DocumentCreationContext](documentcreationcontext.md) — Context about how a document was created. _(beta)_
- [DocumentBaseBox](documentbasebox.md) — A Box that allows setting its Document base not requiring the caller to know the exact types of the box and its base.

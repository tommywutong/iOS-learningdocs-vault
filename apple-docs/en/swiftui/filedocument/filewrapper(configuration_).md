---
title: 'fileWrapper(configuration:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+（27.0 起废弃）, iPadOS 14.0+（27.0 起废弃）, Mac Catalyst 14.0+（27.0 起废弃）, macOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/filedocument/filewrapper(configuration:)'
source_url: 'https://developer.apple.com/documentation/swiftui/filedocument/filewrapper(configuration:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedocument/filewrapper%28configuration%3A%29.json'
content_hash: 'sha256:2df2782ff5cc2e9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDocument](../filedocument.md)

# fileWrapper(configuration:)

<sub>Instance Method</sub>

Serializes a document snapshot to a file wrapper.

> [!warning] Deprecated
> Conform your type to Document instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func fileWrapper(configuration: Self.WriteConfiguration) throws -> FileWrapper
```

## Parameters

- `configuration` — Information about a file that already exists for the document, if any.

## Return Value

The destination to serialize the document contents to. The value can be a newly created [FileWrapper](../../foundation/filewrapper.md) or an update of the one provided in the `configuration` input.

## Discussion

To store a document — for example, in response to a Save command — SwiftUI calls this method. Use it to serialize the document’s data and create or modify a file wrapper with the serialized data:

```swift
func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
    let data = try JSONEncoder().encode(model)
    return FileWrapper(regularFileWithContents: data)
}
```

To store a document as a package — a directory containing multiple files — track which parts of the model changed and reuse `WriteConfiguration/existingFile` as the base directory wrapper to avoid rewriting unchanged files. The example below stores collection metadata in a file and each note in its own `<uuid>.json` file at the package root and only rewrites the files that changed:

```swift
struct NoteCollection: FileDocument {
    var metadata: Metadata
    var notes: [Note] = []

    // ...

    func fileWrapper(configuration: WriteConfiguration) throws -> FileWrapper {
        let documentPackage = configuration.existingFile
            ?? FileWrapper(directoryWithFileWrappers: [:])
        let encoder = JSONEncoder()

        // Update the metadata if it changed.
        if metadata.isChanged {
            if let old = documentPackage.fileWrappers?[Metadata.fileName] {
                documentPackage.removeFileWrapper(old)
            }
            documentPackage.addRegularFile(
                withContents: try encoder.encode(metadata),
                preferredFilename: Metadata.fileName)
        }

        // Sync note wrappers with the notes collection.
        let currentNotes = Set(notes.map(\.filename))
        let notesFiles = documentPackage.fileWrappers ?? [:]

        // Remove notes no longer in the collection.
        for (filename, wrapper) in notesFiles {
            if !currentNotes.contains(filename)
                && filename != Metadata.fileName {
                documentPackage.removeFileWrapper(wrapper)
            }
        }

        // Write notes that are new or changed.
        for note in notes where note.isChanged {
            if let old = documentPackage.fileWrappers?[note.filename] {
                documentPackage.removeFileWrapper(old)
            }
            documentPackage.addRegularFile(
                withContents: try encoder.encode(note),
                preferredFilename: note.filename)
        }
        return documentPackage
    }
}
```

> [!note] Note
> SwiftUI calls this method on a background thread. Don’t make user interface changes from that thread.

## See Also

### Writing a document

- [writableContentTypes](writablecontenttypes.md) — The file types that the document supports saving or exporting to. _(deprecated)_
- [WriteConfiguration](writeconfiguration.md) — The configuration for writing document contents. _(deprecated)_

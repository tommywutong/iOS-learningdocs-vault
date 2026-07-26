---
title: 'fileExporterFilenameLabel(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fileexporterfilenamelabel(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileexporterfilenamelabel(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileexporterfilenamelabel%28_%3A%29.json'
content_hash: 'sha256:3f8b9198baa7bdd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileExporterFilenameLabel(_:)

<sub>Instance Method</sub>

On macOS, configures the `fileExporter` with a label for the file name field.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
@export(implementation) nonisolated func fileExporterFilenameLabel(_ label: LocalizedStringResource) -> some View

```

## Parameters

- `label` — The localized string resource to display.

## See Also

### Exporting to file

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk. _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk. _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.

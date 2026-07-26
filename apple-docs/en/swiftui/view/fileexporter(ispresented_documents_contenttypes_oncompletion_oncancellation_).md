---
title: 'fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileexporter%28ispresented%3Adocuments%3Acontenttypes%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:d7a2cf2a16652b04'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileExporter<C>(isPresented: Binding<Bool>, documents: C, contentTypes: [UTType] = [], onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: (() -> Void)? = nil) -> some View where C : Collection, C.Element : WritableDocument, C.Element.Writer.Destination == URL

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `documents` — The in-memory documents to export.

- `contentTypes` — The content types to export to. If not provided, `WritableDocument.writableContentTypes` are used.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `documents` must be non-empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

```swift
@MainActor
final class TextDocument: WritableDocument {
    static let writableContentTypes: [UTType] = [.utf8PlainText]

    var text: String = ""

    nonisolated func writer(
        configuration: sending WriteConfiguration
    ) -> sending FileWrapperDocumentWriter<String> {
        FileWrapperDocumentWriter(configuration) { snapshot, _ in
            FileWrapper(regularFileWithContents: Data(snapshot.utf8))
        }
    }

    func snapshot(contentType: UTType) async throws -> String {
        text
    }
}

struct ExportView: View {
    @Binding var documents: [TextDocument]
    @State private var isExporting = false

    var body: some View {
        Button("Export…") { isExporting = true }
            .fileExporter(
                isPresented: $isExporting,
                documents: documents
            ) { _ in }
    }
}
```

## See Also

### Exporting to file

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk. _(beta)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk. _(deprecated)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [fileExporterFilenameLabel(_:)](<fileexporterfilenamelabel(__).md>) — On macOS, configures the `fileExporter` with a label for the file name field.

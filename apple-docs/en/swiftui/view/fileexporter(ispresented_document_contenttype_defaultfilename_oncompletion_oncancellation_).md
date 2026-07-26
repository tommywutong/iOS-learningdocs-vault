---
title: 'fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift, swift]
beta: true
deprecated: false
doc_path: '/documentation/swiftui/view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileexporter%28ispresented%3Adocument%3Acontenttype%3Adefaultfilename%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:5e05b16516c40da5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType? = nil, defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: (() -> Void)? = nil) -> some View where D : WritableDocument, D.Writer.Destination == URL

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `document` — The in-memory document to export.

- `contentType` — The content type to export to. If not provided, `WritableDocument.writableContentTypes` are used.

- `defaultFilename` — If provided, the default name to use for the exported file, which the user will have an opportunity to edit prior to the export.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `document` must be non-nil. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

Below is an example of a simple implementation of `WritableDocument`. Instead of `String`, you can use `Data` or any other type as the snapshot.

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
    @State private var document = TextDocument()
    @State private var isExporting = false

    var body: some View {
        Button("Export…") { isExporting = true }
            .fileExporter(
                isPresented: $isExporting,
                document: document,
                defaultFilename: "Untitled"
            ) { _ in }
    }
}
```

## See Also

### Exporting to file

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk. _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [fileExporterFilenameLabel(_:)](<fileexporterfilenamelabel(__).md>) — On macOS, configures the `fileExporter` with a label for the file name field.

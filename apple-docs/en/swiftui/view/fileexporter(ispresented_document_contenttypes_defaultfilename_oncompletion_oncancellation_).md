---
title: 'fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+（27.0 起废弃）, iPadOS 17.0+（27.0 起废弃）, Mac Catalyst 17.0+（27.0 起废弃）, macOS 14.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swiftui/view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileexporter%28ispresented%3Adocument%3Acontenttypes%3Adefaultfilename%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:f2a0ca40883171b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.

> [!warning] Deprecated
> Conform your type to WritableDocument or Transferable instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentTypes: [UTType] = [], defaultFilename: String? = nil, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void = {}) -> some View where D : FileDocument

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `document` — The in-memory document to export.

- `contentTypes` — The list of supported content types which can be exported. If not provided, `FileDocument.writableContentTypes` are used.

- `defaultFilename` — If provided, the default name to use for the exported file, which the user will have an opportunity to edit prior to the export.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCancellation` will be called.

For example, a button that exports a document and handles cancellation might look like this:

```swift
struct ExportButton: View {
    @State private var isExporterPresented = false
    var document: TextFile?

    var body: some View {
        Button("Export") {
            isExporterPresented = true
        }
        .fileExporter(
            isPresented: $isExporterPresented,
            document: document,
            contentTypes: [.utf8PlainText],
            defaultFilename: "Exported Document"
        ) { result in
            switch result {
            case .success(let url):
                print("Saved to \(url)")
            case .failure(let error):
                print(error)
            }
        } onCancellation: {
            print("Export cancelled")
        }
    }
}
```

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileExporterFilenameLabel(_:)](<fileexporterfilenamelabel(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

## See Also

### Exporting to file

- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_).md>) — Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk. _(deprecated)_
- [fileExporter(isPresented:documents:contentType:onCompletion:)](<fileexporter(ispresented_documents_contenttype_oncompletion_).md>) — Presents a system dialog for exporting a collection of value type documents to files on disk. _(deprecated)_
- [fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_document_contenttype_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk. _(beta)_
- [fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_documents_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk. _(beta)_
- [fileExporter(isPresented:item:contentTypes:defaultFilename:onCompletion:onCancellation:)](<fileexporter(ispresented_item_contenttypes_defaultfilename_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [fileExporter(isPresented:items:contentTypes:onCompletion:onCancellation:)](<fileexporter(ispresented_items_contenttypes_oncompletion_oncancellation_).md>) — Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [fileExporterFilenameLabel(_:)](<fileexporterfilenamelabel(__).md>) — On macOS, configures the `fileExporter` with a label for the file name field.

---
title: 'fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileimporter%28ispresented%3Aallowedcontenttypes%3Aallowsmultipleselection%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:4d24e725c77553c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to import multiple files.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `allowedContentTypes` — The list of supported content types which can be imported.

- `allowsMultipleSelection` — Whether the importer allows the user to select more than one file to import.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to choose multiple PDF files for the application to combine them later, might look like this:

```swift
   struct PickPDFsButton: View {
       @State private var showFileImporter = false
       var handlePickedPDF: (URL) -> Void

       var body: some View {
           Button {
               showFileImporter = true
           } label: {
               Label("Choose PDFs to combine", systemImage: "doc.circle")
           }
           .fileImporter(
               isPresented: $showFileImporter,
               allowedContentTypes: [.pdf],
               allowsMultipleSelection: true
           ) { result in
               switch result {
               case .success(let files):
                   files.forEach { file in
                       // gain access to the directory
                       let gotAccess = file.startAccessingSecurityScopedResource()
                       if !gotAccess { return }
                       // access the directory URL
                       // (read templates in the directory, make a bookmark, etc.)
                       handlePickedPDF(file)
                       // release access
                       file.stopAccessingSecurityScopedResource()
                   }
               case .failure(let error):
                   // handle error
                   print(error)
               }
           }
       }
   }
```

> [!note] Note
> Changing `allowedContentTypes` or `allowsMultipleSelection` while the file importer is presented will have no immediate effect, however will apply the next time it is presented.

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>), [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

## See Also

### Importing from file

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — Presents a system dialog for allowing the user to import multiple files.
- [fileImporter(isPresented:allowedContentTypes:onCompletion:)](<fileimporter(ispresented_allowedcontenttypes_oncompletion_).md>) — Presents a system dialog for allowing the user to import an existing file.

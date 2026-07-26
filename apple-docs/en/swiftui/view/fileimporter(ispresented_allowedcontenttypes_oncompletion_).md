---
title: 'fileImporter(isPresented:allowedContentTypes:onCompletion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/fileimporter(ispresented:allowedcontenttypes:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/fileimporter(ispresented:allowedcontenttypes:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/fileimporter%28ispresented%3Aallowedcontenttypes%3Aoncompletion%3A%29.json'
content_hash: 'sha256:a7af9ee15879ff20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileImporter(isPresented:allowedContentTypes:onCompletion:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to import an existing file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `allowedContentTypes` — The list of supported content types which can be imported.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`. - **result** — A `Result` indicating whether the operation succeeded or failed.

## Discussion

In order for the dialog to appear, `isPresented` must be `true`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, an application can have a button that allows the user to choose the default directory with document templates loaded on every launch. Such a button might look like this:

```swift
 struct PickTemplatesDirectoryButton: View {
     @State private var showFileImporter = false
     var onTemplatesDirectoryPicked: (URL) -> Void

     var body: some View {
         Button {
             showFileImporter = true
         } label: {
             Label("Choose templates directory", systemImage: "folder.circle")
         }
         .fileImporter(
             isPresented: $showFileImporter,
             allowedContentTypes: [.directory]
         ) { result in
              switch result {
              case .success(let directory):
                  // gain access to the directory
                  let gotAccess = directory.startAccessingSecurityScopedResource()
                  if !gotAccess { return }
                  // access the directory URL
                  // (read templates in the directory, make a bookmark, etc.)
                  onTemplatesDirectoryPicked(directory)
                  // release access
                  directory.stopAccessingSecurityScopedResource()
              case .failure(let error):
                  // handle error
                  print(error)
              }
         }
     }
 }
```

> [!note] Note
> Changing `allowedContentTypes` while the file importer is presented will have no immediate effect, however will apply the next time it is presented.

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>), [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

## See Also

### Importing from file

- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:)](<fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_).md>) — Presents a system dialog for allowing the user to import multiple files.
- [fileImporter(isPresented:allowedContentTypes:allowsMultipleSelection:onCompletion:onCancellation:)](<fileimporter(ispresented_allowedcontenttypes_allowsmultipleselection_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to import multiple files.

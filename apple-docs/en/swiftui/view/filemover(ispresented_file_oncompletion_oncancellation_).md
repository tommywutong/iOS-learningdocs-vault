---
title: 'fileMover(isPresented:file:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filemover(ispresented:file:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:file:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filemover%28ispresented%3Afile%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:055d7b985e4f8c1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileMover(isPresented:file:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to move an existing file to a new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: @escaping (Result<URL, any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `file` — The URL of the file to be moved.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move a file might look like this:

```swift
  struct MoveFileButton: View {
      @State private var showFileMover = false
      var file: URL
      var onCompletion: (URL) -> Void
      var onCancellation: (() -> Void)?

      var body: some View {
          Button {
              showFileMover = true
          } label: {
              Label("Choose destination", systemImage: "folder.circle")
          }
          .fileMover(isPresented: $showFileMover, file: file) { result in
              switch result {
              case .success(let url):
                  guard url.startAccessingSecurityScopedResource() else {
                      return
                  }
                  onCompletion(url)
                  url.stopAccessingSecurityScopedResource()
              case .failure(let error):
                  print(error)
                  // handle error
              }
          } onCancellation: {
              onCancellation?()
          }
      }
  }
```

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>), [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

## See Also

### Moving a file

- [fileMover(isPresented:file:onCompletion:)](<filemover(ispresented_file_oncompletion_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:)](<filemover(ispresented_files_oncompletion_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<filemover(ispresented_files_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.

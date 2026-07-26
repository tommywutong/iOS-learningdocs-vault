---
title: 'fileMover(isPresented:files:onCompletion:onCancellation:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filemover(ispresented:files:oncompletion:oncancellation:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:files:oncompletion:oncancellation:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filemover%28ispresented%3Afiles%3Aoncompletion%3Aoncancellation%3A%29.json'
content_hash: 'sha256:412c843e87c72d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileMover(isPresented:files:onCompletion:onCancellation:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to move a collection of existing files to a new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void, onCancellation: @escaping () -> Void) -> some View where C : Collection, C.Element == URL

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `files` — A collection of URLs for the files to be moved.

- `onCompletion` — A callback that will be invoked when the operation has succeeded or failed. The `result` indicates whether the operation succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`.

- `onCancellation` — A callback that will be invoked if the user cancels the operation.

## Discussion

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

For example, a button that allows the user to move files might look like this:

```swift
  struct MoveFilesButton: View {
      @Binding var files: [URL]
      @State private var showFileMover = false
      var onCompletion: (URL) -> Void
      var onCancellation: (() -> Void)?

      var body: some View {
          Button {
              showFileMover = true
          } label: {
              Label("Choose destination", systemImage: "folder.circle")
          }
          .fileMover(isPresented: $showFileMover, files: files) { result in
              switch result {
              case .success(let urls):
                  urls.forEach { url in
                      guard url.startAccessingSecurityScopedResource() else {
                          return
                      }
                      onCompletion(url)
                      url.stopAccessingSecurityScopedResource()
                  }
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
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<filemover(ispresented_file_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.

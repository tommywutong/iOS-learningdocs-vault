---
title: 'fileMover(isPresented:files:onCompletion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filemover(ispresented:files:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:files:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filemover%28ispresented%3Afiles%3Aoncompletion%3A%29.json'
content_hash: 'sha256:563a0c9ffeed227c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileMover(isPresented:files:onCompletion:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to move a collection of existing files to a new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: @escaping (Result<[URL], any Error>) -> Void) -> some View where C : Collection, C.Element == URL

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `files` — A collection of `URL`s for the files to be moved.

- `onCompletion` — A callback that will be invoked when the operation has has succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`. - **result** — A `Result` indicating whether the operation succeeded or failed.

## Discussion

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>), [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

In order for the dialog to appear, both `isPresented` must be `true` and `files` must not be empty. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

## See Also

### Moving a file

- [fileMover(isPresented:file:onCompletion:)](<filemover(ispresented_file_oncompletion_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<filemover(ispresented_file_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<filemover(ispresented_files_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.

---
title: 'fileMover(isPresented:file:onCompletion:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filemover(ispresented:file:oncompletion:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filemover(ispresented:file:oncompletion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filemover%28ispresented%3Afile%3Aoncompletion%3A%29.json'
content_hash: 'sha256:dea3a2dbabcbdfee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileMover(isPresented:file:onCompletion:)

<sub>Instance Method</sub>

Presents a system dialog for allowing the user to move an existing file to a new location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: @escaping (Result<URL, any Error>) -> Void) -> some View

```

## Parameters

- `isPresented` — A binding to whether the dialog should be shown.

- `file` — The `URL` of the file to be moved.

- `onCompletion` — A callback that will be invoked when the operation has has succeeded or failed. To access the received URLs, call `startAccessingSecurityScopedResource`. When the access is no longer required, call `stopAccessingSecurityScopedResource`. - **result** — A `Result` indicating whether the operation succeeded or failed.

## Discussion

> [!note] Note
> This dialog provides security-scoped URLs. Call the `startAccessingSecurityScopedResource` method to access or bookmark the URLs, and the `stopAccessingSecurityScopedResource` method to release the access.

In order for the dialog to appear, both `isPresented` must be `true` and `file` must not be `nil`. When the operation is finished, `isPresented` will be set to `false` before `onCompletion` is called. If the user cancels the operation, `isPresented` will be set to `false` and `onCompletion` will not be called.

To further configure the dialog’s appearance and behavior, use these view modifiers: [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>), [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>), [fileDialogMessage(_:)](<filedialogmessage(__).md>), [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>), [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>), [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>), and [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>).

## See Also

### Moving a file

- [fileMover(isPresented:files:onCompletion:)](<filemover(ispresented_files_oncompletion_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [fileMover(isPresented:file:onCompletion:onCancellation:)](<filemover(ispresented_file_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move an existing file to a new location.
- [fileMover(isPresented:files:onCompletion:onCancellation:)](<filemover(ispresented_files_oncompletion_oncancellation_).md>) — Presents a system dialog for allowing the user to move a collection of existing files to a new location.

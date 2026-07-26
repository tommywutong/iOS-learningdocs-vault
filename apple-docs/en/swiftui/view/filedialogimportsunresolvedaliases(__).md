---
title: 'fileDialogImportsUnresolvedAliases(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filedialogimportsunresolvedaliases(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filedialogimportsunresolvedaliases(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filedialogimportsunresolvedaliases%28_%3A%29.json'
content_hash: 'sha256:17cef61bba1f92bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileDialogImportsUnresolvedAliases(_:)

<sub>Instance Method</sub>

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileDialogImportsUnresolvedAliases(_ imports: Bool) -> some View

```

## Parameters

- `imports` — A Boolean value that indicates if the application receives unresolved or resolved URLs when a user chooses aliases.

## Discussion

By default, file dialogs resolve aliases and provide the URL of the item referred to by the chosen alias. This modifier allows control of this behavior: pass `true` if the application doesn’t want file dialog to resolve aliases.

## See Also

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>) — Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogMessage(_:)](<filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [FileDialogBrowserOptions](../filedialogbrowseroptions.md) — The way that file dialogs present the file system.

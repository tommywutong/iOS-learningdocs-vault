---
title: 'fileDialogDefaultDirectory(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filedialogdefaultdirectory(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filedialogdefaultdirectory(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filedialogdefaultdirectory%28_%3A%29.json'
content_hash: 'sha256:5459b9d8a338df8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileDialogDefaultDirectory(_:)

<sub>Instance Method</sub>

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View

```

## Parameters

- `defaultDirectory` — The directory to show when the system file dialog launches. If the given file dialog has a `fileDialogCustomizationID` if stores the user-chosen directory and subsequently opens with it, ignoring the default value provided in this modifier.

## See Also

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](<filedialogcustomizationid(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](<filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [FileDialogBrowserOptions](../filedialogbrowseroptions.md) — The way that file dialogs present the file system.

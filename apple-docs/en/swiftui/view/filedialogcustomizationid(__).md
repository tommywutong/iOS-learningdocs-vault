---
title: 'fileDialogCustomizationID(_:)'
framework: SwiftUI
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swiftui/view/filedialogcustomizationid(_:)'
source_url: 'https://developer.apple.com/documentation/swiftui/view/filedialogcustomizationid(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/view/filedialogcustomizationid%28_%3A%29.json'
content_hash: 'sha256:f76e9550d574832d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [View](../view.md)

# fileDialogCustomizationID(_:)

<sub>Instance Method</sub>

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
nonisolated func fileDialogCustomizationID(_ id: String) -> some View

```

## Parameters

- `id` — An identifier of the configuration.

## Discussion

Among other parameters, it stores the current directory, view style (e.g., Icons, List, Columns), recent places, and expanded window size. It enables a refined user experience; for example, when importing an image, the user might switch to the Icons view, but the List view could be more convenient in another context. The file dialog stores these settings and applies them every time before presenting the panel. If not provided, on every launch, the file dialog uses the default configuration.

## See Also

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](<filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogDefaultDirectory(_:)](<filedialogdefaultdirectory(__).md>) — Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogImportsUnresolvedAliases(_:)](<filedialogimportsunresolvedaliases(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](<filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [FileDialogBrowserOptions](../filedialogbrowseroptions.md) — The way that file dialogs present the file system.

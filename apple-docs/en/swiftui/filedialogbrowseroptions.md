---
title: FileDialogBrowserOptions
framework: SwiftUI
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/filedialogbrowseroptions
source_url: 'https://developer.apple.com/documentation/swiftui/filedialogbrowseroptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedialogbrowseroptions.json'
content_hash: 'sha256:20c47edbc3fe024e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [SwiftUI](../swiftui.md)

# FileDialogBrowserOptions

<sub>Structure</sub>

The way that file dialogs present the file system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
struct FileDialogBrowserOptions
```

## Overview

Apply the options using the [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) modifier.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Getting browser options

- [displayFileExtensions](filedialogbrowseroptions/displayfileextensions.md) — On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show or hide file extensions. Default behavior is to hide them. On macOS, this option has no effect.
- [enumeratePackages](filedialogbrowseroptions/enumeratepackages.md) — Allows enumerating packages contents in contrast to the default behavior when packages are represented flatly, similar to files.
- [includeHiddenFiles](filedialogbrowseroptions/includehiddenfiles.md) — Displays the files that are hidden by default.

## See Also

### Configuring a file dialog

- [fileDialogBrowserOptions(_:)](<view/filedialogbrowseroptions(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [fileDialogConfirmationLabel(_:)](<view/filedialogconfirmationlabel(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [fileDialogCustomizationID(_:)](<view/filedialogcustomizationid(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [fileDialogDefaultDirectory(_:)](<view/filedialogdefaultdirectory(__).md>) — Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [fileDialogImportsUnresolvedAliases(_:)](<view/filedialogimportsunresolvedaliases(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [fileDialogMessage(_:)](<view/filedialogmessage(__).md>) — On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [fileDialogURLEnabled(_:)](<view/filedialogurlenabled(__).md>) — On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.

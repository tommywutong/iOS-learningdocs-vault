---
title: displayFileExtensions
framework: SwiftUI
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swiftui/filedialogbrowseroptions/displayfileextensions
source_url: 'https://developer.apple.com/documentation/swiftui/filedialogbrowseroptions/displayfileextensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swiftui/filedialogbrowseroptions/displayfileextensions.json'
content_hash: 'sha256:6a586e8f0258340e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [SwiftUI](../../swiftui.md) · [FileDialogBrowserOptions](../filedialogbrowseroptions.md)

# displayFileExtensions

<sub>Type Property</sub>

On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show or hide file extensions. Default behavior is to hide them. On macOS, this option has no effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let displayFileExtensions: FileDialogBrowserOptions
```

## See Also

### Getting browser options

- [enumeratePackages](enumeratepackages.md) — Allows enumerating packages contents in contrast to the default behavior when packages are represented flatly, similar to files.
- [includeHiddenFiles](includehiddenfiles.md) — Displays the files that are hidden by default.

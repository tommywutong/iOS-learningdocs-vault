---
title: skipsSubdirectoryDescendants
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerationoptions/skipssubdirectorydescendants
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerationoptions/skipssubdirectorydescendants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerationoptions/skipssubdirectorydescendants.json'
content_hash: 'sha256:a2f49b8ebeca1810'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [DirectoryEnumerationOptions](../directoryenumerationoptions.md)

# skipsSubdirectoryDescendants

<sub>Type Property</sub>

An option to perform a shallow enumeration that doesn’t descend into directories.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var skipsSubdirectoryDescendants: FileManager.DirectoryEnumerationOptions { get }
```

## See Also

### Directory Enumeration Options

- [NSDirectoryEnumerationSkipsPackageDescendants](skipspackagedescendants.md) — An option to treat packages like files and not descend into their contents.
- [NSDirectoryEnumerationSkipsHiddenFiles](skipshiddenfiles.md) — An option to skip hidden files.

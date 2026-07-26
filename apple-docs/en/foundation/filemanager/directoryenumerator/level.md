---
title: level
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerator/level
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/level'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerator/level.json'
content_hash: 'sha256:b3ca1bca3ff7e5ac'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [DirectoryEnumerator](../directoryenumerator.md)

# level

<sub>Instance Property</sub>

The number of levels deep the current object is in the directory hierarchy being enumerated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var level: Int { get }
```

## Discussion

The number of levels, with the directory passed to [enumeratorAtURL:includingPropertiesForKeys:options:errorHandler:](../../nsfilemanager/enumeratoraturl_includingpropertiesforkeys_options_errorhandler_.md) (`NSFileManager`) considered to be level `0`.

## See Also

### Getting File and Directory Attributes

- [directoryAttributes](directoryattributes.md) — A dictionary with the attributes of the directory at which enumeration started.
- [fileAttributes](fileattributes.md) — A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).

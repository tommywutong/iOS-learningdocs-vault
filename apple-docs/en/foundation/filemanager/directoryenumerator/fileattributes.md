---
title: fileAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerator/fileattributes
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/fileattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerator/fileattributes.json'
content_hash: 'sha256:e869e36ed4838418'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [DirectoryEnumerator](../directoryenumerator.md)

# fileAttributes

<sub>Instance Property</sub>

A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileAttributes: [FileAttributeKey : Any]? { get }
```

## Discussion

See the description of the [- fileAttributesAtPath:traverseLink:](<../fileattributes(atpath_traverselink_).md>) method of [FileManager](../../filemanager.md) for details on obtaining the attributes from the dictionary.

## See Also

### Getting File and Directory Attributes

- [directoryAttributes](directoryattributes.md) — A dictionary with the attributes of the directory at which enumeration started.
- [level](level.md) — The number of levels deep the current object is in the directory hierarchy being enumerated.

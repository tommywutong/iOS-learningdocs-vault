---
title: directoryAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/directoryenumerator/directoryattributes
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/directoryenumerator/directoryattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/directoryenumerator/directoryattributes.json'
content_hash: 'sha256:9e5ca0268ebdd69c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [DirectoryEnumerator](../directoryenumerator.md)

# directoryAttributes

<sub>Instance Property</sub>

A dictionary with the attributes of the directory at which enumeration started.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var directoryAttributes: [FileAttributeKey : Any]? { get }
```

## Discussion

See the description of the [- fileAttributesAtPath:traverseLink:](<../fileattributes(atpath_traverselink_).md>) method of [FileManager](../../filemanager.md) for details on obtaining the attributes from the dictionary.

## See Also

### Related Documentation

- [- createDirectoryAtPath:attributes:](<../createdirectory(atpath_attributes_).md>) — Creates a directory (without contents) at a given path with given attributes. _(deprecated)_

### Getting File and Directory Attributes

- [fileAttributes](fileattributes.md) — A dictionary with the attributes of the most recently returned file or subdirectory (as referenced by the pathname).
- [level](level.md) — The number of levels deep the current object is in the directory hierarchy being enumerated.

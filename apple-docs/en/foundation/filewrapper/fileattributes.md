---
title: fileAttributes
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/fileattributes
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/fileattributes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/fileattributes.json'
content_hash: 'sha256:de4713ee9918909b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# fileAttributes

<sub>Instance Property</sub>

A dictionary of file attributes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileAttributes: [String : Any] { get set }
```

## Discussion

The file attributes’ dictionary is the same format as that returned by [- attributesOfItemAtPath:error:](<../filemanager/attributesofitem(atpath_).md>) (`NSFileManager`).

## See Also

### Accessing Files

- [filename](filename.md) — The filename of the file wrapper object
- [preferredFilename](preferredfilename.md) — The preferred filename for the file wrapper object.
- [regularFileContents](regularfilecontents.md) — The contents of the file-system node associated with a regular-file file wrapper.

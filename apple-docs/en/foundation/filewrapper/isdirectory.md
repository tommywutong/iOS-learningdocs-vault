---
title: isDirectory
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/isdirectory
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/isdirectory'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/isdirectory.json'
content_hash: 'sha256:482b9c979b182b87'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# isDirectory

<sub>Instance Property</sub>

This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isDirectory: Bool { get }
```

## Discussion

This property will contain YES when the file wrapper is a directory file wrapper, otherwise it contains NO.

> [!note] Note
> Invocations of [- readFromURL:options:error:](<read(from_options_).md>) may change the value of this property, if the type of the file on disk has changed.

## See Also

### Querying File Wrappers

- [regularFile](isregularfile.md) — This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [symbolicLink](issymboliclink.md) — A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.

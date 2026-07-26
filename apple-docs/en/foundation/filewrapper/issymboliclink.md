---
title: isSymbolicLink
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filewrapper/issymboliclink
source_url: 'https://developer.apple.com/documentation/foundation/filewrapper/issymboliclink'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filewrapper/issymboliclink.json'
content_hash: 'sha256:9578eea5e05afe4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileWrapper](../filewrapper.md)

# isSymbolicLink

<sub>Instance Property</sub>

A boolean that indicates whether the file wrapper object is a symbolic-link file wrapper.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isSymbolicLink: Bool { get }
```

## Discussion

This property contains [true](../../swift/true.md) when the file wrapper object is a symbolic-link file wrapper, [false](../../swift/false.md) otherwise.

Invocations of [- readFromURL:options:error:](<read(from_options_).md>) may change the value contained by this property, if the type of the file on disk has changed.

## See Also

### Querying File Wrappers

- [regularFile](isregularfile.md) — This property contains a boolean value that indicates whether the file wrapper object is a regular-file.
- [directory](isdirectory.md) — This property contains a boolean value indicating whether the file wrapper is a directory file wrapper.

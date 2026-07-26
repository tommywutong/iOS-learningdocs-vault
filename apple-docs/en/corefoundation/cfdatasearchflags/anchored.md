---
title: anchored
framework: Core Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cfdatasearchflags/anchored
source_url: 'https://developer.apple.com/documentation/corefoundation/cfdatasearchflags/anchored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfdatasearchflags/anchored.json'
content_hash: 'sha256:f2cc34c7a3b7970d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Foundation](../../corefoundation.md) · [CFDataSearchFlags](../cfdatasearchflags.md)

# anchored

<sub>Type Property</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var anchored: CFDataSearchFlags { get }
```

## Discussion

Performs searching only on bytes at the beginning or, if `kCFDataSearchBackwards` is also specified, at the end of the search range. No match at the beginning or end means nothing is found, even if a matching sequence of bytes occurs elsewhere in the data object.

## See Also

### Constants

- [kCFDataSearchBackwards](backwards.md)

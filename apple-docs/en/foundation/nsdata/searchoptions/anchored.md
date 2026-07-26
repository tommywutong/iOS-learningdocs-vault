---
title: anchored
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/searchoptions/anchored
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/searchoptions/anchored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/searchoptions/anchored.json'
content_hash: 'sha256:444fda0b7caeb28d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSData](../../nsdata.md) · [SearchOptions](../searchoptions.md)

# anchored

<sub>Type Property</sub>

Search is limited to start (or end, if searching backwards) of the data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var anchored: NSData.SearchOptions { get }
```

## Discussion

This option performs searching only on bytes at the beginning of the range (or the end when using [NSDataSearchBackwards](backwards.md)). No match at the beginning or end means nothing is found, even if a matching sequence of bytes occurs elsewhere in the data object.

## See Also

### Constants

- [NSDataSearchBackwards](backwards.md) — Search from the end of the data object.

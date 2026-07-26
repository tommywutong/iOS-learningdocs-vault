---
title: inverted
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nscharacterset/inverted
source_url: 'https://developer.apple.com/documentation/foundation/nscharacterset/inverted'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nscharacterset/inverted.json'
content_hash: 'sha256:27a870609ac3d575'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSCharacterSet](../nscharacterset.md)

# inverted

<sub>Instance Property</sub>

A character set containing only characters that don’t exist in the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var inverted: CharacterSet { get }
```

## Discussion

Using the inverse of an immutable character set is much more efficient than inverting a mutable character set.

## See Also

### Related Documentation

- [- invert](<../nsmutablecharacterset/invert().md>) — Replaces all the characters in the receiver with all the characters it didn’t previously contain.

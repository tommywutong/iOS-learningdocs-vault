---
title: object
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorderedcollectionchange/object
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectionchange/object'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectionchange/object.json'
content_hash: 'sha256:c44a0d9ecc8abee4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionChange](../nsorderedcollectionchange.md)

# object

<sub>Instance Property</sub>

An object the change inserts or removes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var object: Any? { get }
```

## See Also

### Accessing the Change

- [changeType](changetype.md) — The type of change.
- [index](index.md) — The index location of the change.
- [associatedIndex](associatedindex.md) — When this property is set to a value other than [NSNotFound](../nsnotfound-9t5v2.md), the receiver is one half of a move, and this value is the index of the change’s counterpart of the opposite type in the diff.

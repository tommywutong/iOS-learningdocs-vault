---
title: comparator
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nssortdescriptor/comparator
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/comparator'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/comparator.json'
content_hash: 'sha256:d7e424067c0d6a53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# comparator

<sub>Instance Property</sub>

The comparator for the sort descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var comparator: Comparator { get }
```

## Discussion

Call this property only for sort descriptors initialized with [- initWithKey:ascending:comparator:](<init(key_ascending_comparator_).md>).

## See Also

### Getting Information About a Sort Descriptor

- [ascending](ascending.md) — A Boolean value that indicates whether the receiver specifies sorting in ascending order.
- [key](key.md) — The key that specifies the property to compare during sorting.
- [keyPath](keypath.md) — The key path that specifies the property to compare during sorting.
- [selector](selector.md) — The selector for comparing objects.

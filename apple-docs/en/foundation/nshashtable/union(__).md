---
title: 'union(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/union(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/union%28_%3A%29.json'
content_hash: 'sha256:906e5c226d4dcfdc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# union(_:)

<sub>Instance Method</sub>

Adds each element in another given hash table to the receiving hash table, if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ other: NSHashTable<ObjectType>)
```

## Parameters

- `other` — The hash table of elements to add to the receiving hash table.

## Discussion

The equality test used for members depends on the personality option selected. For instance, choosing the [NSPointerFunctionsObjectPersonality](../nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [Options](../nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## See Also

### Set Functions

- [- minusHashTable:](<minus(__).md>) — Removes each element in another given hash table from the receiving hash table, if present.

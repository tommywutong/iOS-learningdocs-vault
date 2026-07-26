---
title: 'exchangeObject(at:withObjectAt:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutablearray/exchangeobject(at:withobjectat:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutablearray/exchangeobject(at:withobjectat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutablearray/exchangeobject%28at%3Awithobjectat%3A%29.json'
content_hash: 'sha256:07f3a5507e945e02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableArray](../nsmutablearray.md)

# exchangeObject(at:withObjectAt:)

<sub>Instance Method</sub>

Exchanges the objects in the array at given indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func exchangeObject(at idx1: Int, withObjectAt idx2: Int)
```

## Parameters

- `idx1` — The index of the object with which to replace the object at index `idx2`.

- `idx2` — The index of the object with which to replace the object at index `idx1`.

## See Also

### Rearranging Content

- [- sortUsingDescriptors:](<sort(using_)-4eh07.md>) — Sorts the receiver using a given array of sort descriptors.
- [- sortUsingComparator:](<sort(comparator_).md>) — Sorts the receiver in ascending order using the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortWithOptions:usingComparator:](<sort(options_usingcomparator_).md>) — Sorts the receiver in ascending order using the specified options and the comparison method specified by a given [Comparator](../comparator.md) block.
- [- sortUsingFunction:context:](<sort(__context_).md>) — Sorts the receiver in ascending order as defined by the comparison function `compare`.
- [- sortUsingSelector:](<sort(using_)-537vs.md>) — Sorts the receiver in ascending order, as determined by the comparison method specified by a given selector.

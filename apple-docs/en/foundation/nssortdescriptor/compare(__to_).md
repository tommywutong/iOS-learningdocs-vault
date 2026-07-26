---
title: 'compare(_:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nssortdescriptor/compare(_:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nssortdescriptor/compare(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nssortdescriptor/compare%28_%3Ato%3A%29.json'
content_hash: 'sha256:21763f827f1c9361'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSortDescriptor](../nssortdescriptor.md)

# compare(_:to:)

<sub>Instance Method</sub>

Returns a comparison result value that indicates the sort order of two objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func compare(_ object1: Any, to object2: Any) -> ComparisonResult
```

## Parameters

- `object1` — The object to compare with `object2`. This object must have a property accessible using the key-path specified by [key](key.md).

- `object2` — The object to compare with `object1`. This object must have a property accessible using the key-path specified by [key](key.md).

## Return Value

[NSOrderedAscending](../comparisonresult/orderedascending.md) if `object1` is less than `object2`, [NSOrderedDescending](../comparisonresult/ordereddescending.md) if `object1` is greater than `object2`, or [NSOrderedSame](../comparisonresult/orderedsame.md) if `object1` is equal to `object2`.

## Discussion

The ordering is determined by comparing the values specified by [key](key.md) of `object1` and `object2` using the selector specified by [selector](selector.md).

## See Also

### Using Sort Descriptors

- [reversedSortDescriptor](reversedsortdescriptor.md) — Returns a sort descriptor that reverses the sort order.
- [- allowEvaluation](<allowevaluation().md>) — Forces a securely decoded sort descriptor to allow evaluation.

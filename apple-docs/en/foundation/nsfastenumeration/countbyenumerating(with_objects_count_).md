---
title: 'countByEnumerating(with:objects:count:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsfastenumeration/countbyenumerating(with:objects:count:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsfastenumeration/countbyenumerating(with:objects:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsfastenumeration/countbyenumerating%28with%3Aobjects%3Acount%3A%29.json'
content_hash: 'sha256:e9aa6139d4390b95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSFastEnumeration](../nsfastenumeration.md)

# countByEnumerating(with:objects:count:)

<sub>Instance Method</sub>

Returns by reference a C array of objects over which the sender should iterate, and as the return value the number of objects in the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func countByEnumerating(with state: UnsafeMutablePointer<NSFastEnumerationState>, objects buffer: AutoreleasingUnsafeMutablePointer<AnyObject?>, count len: Int) -> Int
```

## Parameters

- `state` — Context information that is used in the enumeration to, in addition to other possibilities, ensure that the collection has not been mutated.

- `buffer` — A C array of objects over which the sender is to iterate.

- `len` — The maximum number of objects to return in `stackbuf`.

## Return Value

The number of objects returned in `stackbuf`. Returns `0` when the iteration is finished.

## Discussion

The state structure is assumed to be of stack local memory, so you can recast the passed in state structure to one more suitable for your iteration.

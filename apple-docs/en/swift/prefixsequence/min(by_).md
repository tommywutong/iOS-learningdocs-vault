---
title: 'min(by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/prefixsequence/min(by:)'
source_url: 'https://developer.apple.com/documentation/swift/prefixsequence/min(by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/prefixsequence/min%28by%3A%29.json'
content_hash: 'sha256:88b75a0685c4c4a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [PrefixSequence](../prefixsequence.md)

# min(by:)

<sub>Instance Method</sub>

Returns the minimum element in the sequence, using the given predicate as the comparison between elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@warn_unqualified_access func min(by areInIncreasingOrder: (Self.Element, Self.Element) throws -> Bool) rethrows -> Self.Element?
```

## Parameters

- `areInIncreasingOrder` — A predicate that returns `true` if its first argument should be ordered before its second argument; otherwise, `false`.

## Return Value

The sequence’s minimum element, according to `areInIncreasingOrder`. If the sequence has no elements, returns `nil`.

## Discussion

The predicate must be a _strict weak ordering_ over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areInIncreasingOrder(a, a)` is always `false`. (Irreflexivity)
- If `areInIncreasingOrder(a, b)` and `areInIncreasingOrder(b, c)` are both `true`, then `areInIncreasingOrder(a, c)` is also `true`. (Transitive comparability)
- Two elements are _incomparable_ if neither is ordered before the other according to the predicate. If `a` and `b` are incomparable, and `b` and `c` are incomparable, then `a` and `c` are also incomparable. (Transitive incomparability)

This example shows how to use the `min(by:)` method on a dictionary to find the key-value pair with the lowest value.

```swift
let hues = ["Heliotrope": 296, "Coral": 16, "Aquamarine": 156]
let leastHue = hues.min { a, b in a.value < b.value }
print(leastHue)
// Prints "Optional((key: "Coral", value: 16))"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

---
title: 'starts(with:by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anyrandomaccesscollection/starts(with:by:)'
source_url: 'https://developer.apple.com/documentation/swift/anyrandomaccesscollection/starts(with:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anyrandomaccesscollection/starts%28with%3Aby%3A%29.json'
content_hash: 'sha256:9e39e1d255573b49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyRandomAccessCollection](../anyrandomaccesscollection.md)

# starts(with:by:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func starts<PossiblePrefix>(with possiblePrefix: PossiblePrefix, by areEquivalent: (Self.Element, PossiblePrefix.Element) throws -> Bool) rethrows -> Bool where PossiblePrefix : Sequence
```

## Parameters

- `possiblePrefix` — A sequence to compare to this sequence.

- `areEquivalent` — A predicate that returns `true` if its two arguments are equivalent; otherwise, `false`.

## Return Value

`true` if the initial elements of the sequence are equivalent to the elements of `possiblePrefix`; otherwise, `false`. If `possiblePrefix` has no elements, the return value is `true`.

## Discussion

The predicate must be an _equivalence relation_ over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areEquivalent(a, a)` is always `true`. (Reflexivity)
- `areEquivalent(a, b)` implies `areEquivalent(b, a)`. (Symmetry)
- If `areEquivalent(a, b)` and `areEquivalent(b, c)` are both `true`, then `areEquivalent(a, c)` is also `true`. (Transitivity)

> [!abstract] Complexity
> O(_m_), where _m_ is the lesser of the length of the sequence and the length of `possiblePrefix`.

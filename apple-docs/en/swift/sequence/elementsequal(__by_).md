---
title: 'elementsEqual(_:by:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/elementsequal(_:by:)'
source_url: 'https://developer.apple.com/documentation/swift/sequence/elementsequal(_:by:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/elementsequal%28_%3Aby%3A%29.json'
content_hash: 'sha256:0ebdb222901ca7c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# elementsEqual(_:by:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence, by areEquivalent: (Self.Element, OtherSequence.Element) throws -> Bool) rethrows -> Bool where OtherSequence : Sequence
```

## Parameters

- `other` — A sequence to compare to this sequence.

- `areEquivalent` — A predicate that returns `true` if its two arguments are equivalent; otherwise, `false`.

## Return Value

`true` if this sequence and `other` contain equivalent items, using `areEquivalent` as the equivalence test; otherwise, `false.`

## Discussion

At least one of the sequences must be finite.

The predicate must be an _equivalence relation_ over the elements. That is, for any elements `a`, `b`, and `c`, the following conditions must hold:

- `areEquivalent(a, a)` is always `true`. (Reflexivity)
- `areEquivalent(a, b)` implies `areEquivalent(b, a)`. (Symmetry)
- If `areEquivalent(a, b)` and `areEquivalent(b, c)` are both `true`, then `areEquivalent(a, c)` is also `true`. (Transitivity)

> [!abstract] Complexity
> O(_m_), where _m_ is the lesser of the length of the sequence and the length of `other`.

## See Also

### Comparing Sequences

- [elementsEqual(_:)](<elementsequal(__).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.
- [starts(with:)](<starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

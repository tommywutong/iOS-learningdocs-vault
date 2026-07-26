---
title: 'elementsEqual(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/array/elementsequal(_:)'
source_url: 'https://developer.apple.com/documentation/swift/array/elementsequal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/elementsequal%28_%3A%29.json'
content_hash: 'sha256:a66205c2d47bf418'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# elementsEqual(_:)

<sub>Instance Method</sub>

Returns a Boolean value indicating whether this sequence and another sequence contain the same elements in the same order.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func elementsEqual<OtherSequence>(_ other: OtherSequence) -> Bool where OtherSequence : Sequence, Self.Element == OtherSequence.Element
```

## Parameters

- `other` — A sequence to compare to this sequence.

## Return Value

`true` if this sequence and `other` contain the same elements in the same order.

## Discussion

At least one of the sequences must be finite.

This example tests whether one countable range shares the same elements as another countable range and an array.

```swift
let a = 1...3
let b = 1...10

print(a.elementsEqual(b))
// Prints "false"
print(a.elementsEqual([1, 2, 3]))
// Prints "true"
```

> [!abstract] Complexity
> O(_m_), where _m_ is the lesser of the length of the sequence and the length of `other`.

## See Also

### Comparing Arrays

- [==(_:_:)](<==(____).md>) — Returns a Boolean value indicating whether two arrays contain the same elements in the same order.
- [!=(_:_:)](<!=(____).md>) — Returns a Boolean value indicating whether two values are not equal.
- [elementsEqual(_:by:)](<elementsequal(__by_).md>) — Returns a Boolean value indicating whether this sequence and another sequence contain equivalent elements in the same order, using the given predicate as the equivalence test.
- [starts(with:)](<starts(with_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are the same as the elements in another sequence.
- [starts(with:by:)](<starts(with_by_).md>) — Returns a Boolean value indicating whether the initial elements of the sequence are equivalent to the elements in another sequence, using the given predicate as the equivalence test.
- [lexicographicallyPrecedes(_:)](<lexicographicallyprecedes(__).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the less-than operator (`<`) to compare elements.
- [lexicographicallyPrecedes(_:by:)](<lexicographicallyprecedes(__by_).md>) — Returns a Boolean value indicating whether the sequence precedes another sequence in a lexicographical (dictionary) ordering, using the given predicate to compare elements.

---
title: 'joined(separator:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/sequence/joined(separator:)-7w47r'
source_url: 'https://developer.apple.com/documentation/swift/sequence/joined(separator:)-7w47r'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/sequence/joined%28separator%3A%29-7w47r.json'
content_hash: 'sha256:c43f1646cd101c64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Sequence](../sequence.md)

# joined(separator:)

<sub>Instance Method</sub>

Returns the concatenated elements of this sequence of sequences, inserting the given separator between each element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func joined<Separator>(separator: Separator) -> JoinedSequence<Self> where Separator : Sequence, Separator.Element == Self.Element.Element
```

## Parameters

- `separator` — A sequence to insert between each of this sequence’s elements.

## Return Value

The joined sequence of elements.

## Discussion

This example shows how an array of `[Int]` instances can be joined, using another `[Int]` instance as the separator:

```swift
let nestedNumbers = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
let joined = nestedNumbers.joined(separator: [-1, -2])
print(Array(joined))
// Prints "[1, 2, 3, -1, -2, 4, 5, 6, -1, -2, 7, 8, 9]"
```

## See Also

### Splitting and Joining Elements

- [split(maxSplits:omittingEmptySubsequences:whereSeparator:)](<split(maxsplits_omittingemptysubsequences_whereseparator_).md>) — Returns the longest possible subsequences of the sequence, in order, that don’t contain elements satisfying the given predicate. Elements that are used to split the sequence are not returned as part of any subsequence.
- [split(separator:maxSplits:omittingEmptySubsequences:)](<split(separator_maxsplits_omittingemptysubsequences_).md>) — Returns the longest possible subsequences of the sequence, in order, around elements equal to the given element.
- [joined()](<joined().md>) — Returns the elements of this sequence of sequences, concatenated.
- [joined(separator:)](<joined(separator_)-5zjyj.md>) — Returns a new string by concatenating the elements of the sequence, adding the given separator between each element.

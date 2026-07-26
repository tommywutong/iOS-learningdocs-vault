---
title: '+(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/unicodescalarview/+(_:_:)-1c1pd'
source_url: 'https://developer.apple.com/documentation/swift/substring/unicodescalarview/+(_:_:)-1c1pd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/unicodescalarview/%2B%28_%3A_%3A%29-1c1pd.json'
content_hash: 'sha256:43b5acd1a59dd460'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UnicodeScalarView](../unicodescalarview.md)

# +(_:_:)

<sub>Operator</sub>

Creates a new collection by concatenating the elements of a sequence and a collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func + <Other>(lhs: Other, rhs: Self) -> Self where Other : Sequence, Self.Element == Other.Element
```

## Parameters

- `lhs` — A collection or finite sequence.

- `rhs` — A range-replaceable collection.

## Discussion

The two arguments must have the same `Element` type. For example, you can concatenate the elements of a `Range<Int>` instance and an integer array.

```swift
let numbers = [7, 8, 9, 10]
let moreNumbers = (1...6) + numbers
print(moreNumbers)
// Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

The resulting collection has the type of argument on the right-hand side. In the example above, `moreNumbers` has the same type as `numbers`, which is `[Int]`.

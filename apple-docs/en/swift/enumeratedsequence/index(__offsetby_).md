---
title: 'index(_:offsetBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/enumeratedsequence/index(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/index(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/index%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:1198fe495c69a909'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# index(_:offsetBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ i: EnumeratedSequence<Base>.Index, offsetBy distance: Int) -> EnumeratedSequence<Base>.Index
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.

## Return Value

An index offset by `distance` from the index `i`. If `distance` is positive, this is the same value as the result of `distance` calls to `index(after:)`. If `distance` is negative, this is the same value as the result of `abs(distance)` calls to `index(before:)`.

## Discussion

The following example obtains an index advanced four positions from a string’s starting index and then prints the character at that position.

```swift
let s = "Swift"
let i = s.index(s.startIndex, offsetBy: 4)
print(s[i])
// Prints "t"
```

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the absolute value of `distance`.

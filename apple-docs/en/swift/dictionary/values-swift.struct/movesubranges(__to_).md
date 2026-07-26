---
title: 'moveSubranges(_:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/dictionary/values-swift.struct/movesubranges(_:to:)'
source_url: 'https://developer.apple.com/documentation/swift/dictionary/values-swift.struct/movesubranges(_:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/dictionary/values-swift.struct/movesubranges%28_%3Ato%3A%29.json'
content_hash: 'sha256:a89ee7672ea28bd6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Dictionary](../../dictionary.md) · [Values](../values-swift.struct.md)

# moveSubranges(_:to:)

<sub>Instance Method</sub>

Moves the elements in the given subranges to just before the element at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func moveSubranges(_ subranges: RangeSet<Self.Index>, to insertionPoint: Self.Index) -> Range<Self.Index>
```

## Parameters

- `subranges` — The subranges of the elements to move.

- `insertionPoint` — The index to use as the destination of the elements.

## Return Value

The new bounds of the moved elements.

## Discussion

This example finds all the uppercase letters in the array and then moves them to between `"i"` and `"j"`.

```swift
var letters = Array("ABCdeFGhijkLMNOp")
let uppercaseRanges = letters.indices(where: { $0.isUppercase })
let rangeOfUppercase = letters.moveSubranges(uppercaseRanges, to: 10)
// String(letters) == "dehijABCFGLMNOkp"
// rangeOfUppercase == 5..<14
```

> [!abstract] Complexity
> O(_n_ log _n_) where _n_ is the length of the collection.

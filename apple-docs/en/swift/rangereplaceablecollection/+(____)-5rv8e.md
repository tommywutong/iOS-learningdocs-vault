---
title: '+(_:_:)'
framework: Swift
symbol_kind: op
role: symbol
role_heading: Operator
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/rangereplaceablecollection/+(_:_:)-5rv8e'
source_url: 'https://developer.apple.com/documentation/swift/rangereplaceablecollection/+(_:_:)-5rv8e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/rangereplaceablecollection/%2B%28_%3A_%3A%29-5rv8e.json'
content_hash: 'sha256:b2f32e15010a1e8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [RangeReplaceableCollection](../rangereplaceablecollection.md)

# +(_:_:)

<sub>Operator</sub>

Creates a new collection by concatenating the elements of two collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func + <Other>(lhs: Self, rhs: Other) -> Self where Other : RangeReplaceableCollection, Self.Element == Other.Element
```

## Parameters

- `lhs` — A range-replaceable collection.

- `rhs` — Another range-replaceable collection.

## Discussion

The two arguments must have the same `Element` type. For example, you can concatenate the elements of two integer arrays.

```swift
let lowerNumbers = [1, 2, 3, 4]
let higherNumbers: ContiguousArray = [5, 6, 7, 8, 9, 10]
let allNumbers = lowerNumbers + higherNumbers
print(allNumbers)
// Prints "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"
```

The resulting collection has the type of the argument on the left-hand side. In the example above, `moreNumbers` has the same type as `numbers`, which is `[Int]`.

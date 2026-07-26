---
title: 'move(fromOffsets:toOffset:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/move(fromoffsets:tooffset:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/move(fromoffsets:tooffset:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/move%28fromoffsets%3Atooffset%3A%29.json'
content_hash: 'sha256:e3aaae318f2317ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# move(fromOffsets:toOffset:)

<sub>Instance Method</sub>

Moves all the elements at the specified offsets to the specified destination offset, preserving ordering.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func move(fromOffsets source: IndexSet, toOffset destination: Int)
```

## Parameters

- `source` — An index set representing the offsets of all elements that should be moved.

- `destination` — The offset of the element before which to insert the moved elements. `destination` must be in the closed range `0...count`.

## Discussion

Pass an offset as `destination` to indicate where in the collection the moved elements should be inserted. Of the elements that are not represented by the offsets in `source`, those before `destination` are moved toward the beginning of the collection to make room for the moved elements, while those at or after `destination` are moved toward the end.

In this example, demonstrating moving several elements to different destination offsets, `lowercaseOffsets` represents the offsets of the lowercase elements in `letters`:

```swift
var letters = Array("ABcDefgHIJKlmNO")
let lowercaseOffsets = IndexSet(...)
letters.move(fromOffsets: lowercaseOffsets, toOffset: 2)
// String(letters) == "ABcefglmDHIJKNO"

// Reset the `letters` array.
letters = Array("ABcDefgHIJKlmNO")
letters.move(fromOffsets: lowercaseOffsets, toOffset: 15)
// String(letters) == "ABDHIJKNOcefglm"
```

If `source` represents a single element, calling this method with its own offset, or the offset of the following element, as `destination` has no effect.

```swift
letters = Array("ABcDefgHIJKlmNO")
letters.move(fromOffsets: IndexSet(integer: 2), toOffset: 2)
// String(letters) == "ABcDefgHIJKlmNO"
```

> [!abstract] Complexity
> O(_n_ log _n_), where _n_ is the length of the collection.

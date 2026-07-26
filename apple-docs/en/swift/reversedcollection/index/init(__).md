---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/reversedcollection/index/init(_:)'
source_url: 'https://developer.apple.com/documentation/swift/reversedcollection/index/init(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/reversedcollection/index/init%28_%3A%29.json'
content_hash: 'sha256:6a8f7799efad72c3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [ReversedCollection](../../reversedcollection.md) · [Index](../index.md)

# init(_:)

<sub>Initializer</sub>

Creates a new index into a reversed collection for the position before the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ base: Base.Index)
```

## Parameters

- `base` — The position after the element to create an index for.

## Discussion

When you create an index into a reversed collection using `base`, an index from the underlying collection, the resulting index is the position of the element _before_ the element referenced by `base`. The following example creates a new `ReversedIndex` from the index of the `"a"` character in a string’s character view.

```swift
let name = "Horatio"
let aIndex = name.firstIndex(of: "a")!
// name[aIndex] == "a"

let reversedName = name.reversed()
let i = ReversedCollection<String>.Index(aIndex)
// reversedName[i] == "r"
```

The element at the position created using `ReversedIndex<...>(aIndex)` is `"r"`, the character before `"a"` in the `name` string.

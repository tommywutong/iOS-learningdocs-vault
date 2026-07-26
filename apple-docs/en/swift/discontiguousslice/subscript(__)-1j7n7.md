---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/discontiguousslice/subscript(_:)-1j7n7'
source_url: 'https://developer.apple.com/documentation/swift/discontiguousslice/subscript(_:)-1j7n7'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/discontiguousslice/subscript%28_%3A%29-1j7n7.json'
content_hash: 'sha256:161ed231719e2161'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [DiscontiguousSlice](../discontiguousslice.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: DiscontiguousSlice<Base>.Index) -> Base.Element { get set }
```

## Parameters

- `i` — The position of the element to access. `i` must be a valid index of the collection that is not equal to the `endIndex` property.

## Overview

For example, you can replace an element of an array by using its subscript.

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
streets[1] = "Butler"
print(streets[1])
// Prints "Butler"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> [!abstract] Complexity
> O(1)

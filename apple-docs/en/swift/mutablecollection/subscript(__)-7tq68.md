---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/subscript(_:)-7tq68'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/subscript(_:)-7tq68'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/subscript%28_%3A%29-7tq68.json'
content_hash: 'sha256:692b4fc0596a301b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
override subscript(position: Self.Index) -> Self.Element { get set }
```

## Parameters

- `position` — The position of the element to access. `position` must be a valid index of the collection that is not equal to the `endIndex` property.

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

## Default Implementations

### MutableCollection Implementations

- [subscript(_:)](<subscript(__)-1wd4v.md>)
- [subscript(_:)](<subscript(__)-2qem1.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<subscript(__)-37d4d.md>)

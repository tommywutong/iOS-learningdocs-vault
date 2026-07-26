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
doc_path: '/documentation/swift/collection/subscript(_:)-887tm'
source_url: 'https://developer.apple.com/documentation/swift/collection/subscript(_:)-887tm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collection/subscript%28_%3A%29-887tm.json'
content_hash: 'sha256:949d7997fae4d632'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Collection](../collection.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: Self.Index) -> Self.Element { get }
```

## Parameters

- `position` — The position of the element to access. `position` must be a valid index of the collection that is not equal to the `endIndex` property.

## Overview

The following example accesses an element of an array through its subscript to print its value:

```swift
var streets = ["Adams", "Bryant", "Channing", "Douglas", "Evarts"]
print(streets[1])
// Prints "Bryant"
```

You can subscript a collection with any valid index other than the collection’s end index. The end index refers to the position one past the last element of a collection, so it doesn’t correspond with an element.

> [!abstract] Complexity
> O(1)

## Default Implementations

### Collection Implementations

- [subscript(_:)](<subscript(__)-2ew5d.md>) — Accesses the contiguous subrange of the collection’s elements specified by a range expression.
- [subscript(_:)](<subscript(__)-593m9.md>)
- [subscript(_:)](<subscript(__)-6dbv1.md>) — Accesses a view of this collection with the elements at the given indices.
- [subscript(_:)](<subscript(__)-6nizk.md>) — Accesses a contiguous subrange of the collection’s elements.

### MutableCollection Implementations

- [subscript(_:)](<../mutablecollection/subscript(__)-1wd4v.md>)
- [subscript(_:)](<../mutablecollection/subscript(__)-2qem1.md>) — Accesses a contiguous subrange of the collection’s elements.
- [subscript(_:)](<../mutablecollection/subscript(__)-37d4d.md>)

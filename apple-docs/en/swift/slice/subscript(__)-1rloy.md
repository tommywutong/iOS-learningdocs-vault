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
doc_path: '/documentation/swift/slice/subscript(_:)-1rloy'
source_url: 'https://developer.apple.com/documentation/swift/slice/subscript(_:)-1rloy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/subscript%28_%3A%29-1rloy.json'
content_hash: 'sha256:eef684ce3140b7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(index: Slice<Base>.Index) -> Base.Element { get }
```

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

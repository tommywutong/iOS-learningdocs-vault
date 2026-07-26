---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/enumeratedsequence/subscript(_:)'
source_url: 'https://developer.apple.com/documentation/swift/enumeratedsequence/subscript(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/enumeratedsequence/subscript%28_%3A%29.json'
content_hash: 'sha256:23902221da540436'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [EnumeratedSequence](../enumeratedsequence.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(position: EnumeratedSequence<Base>.Index) -> EnumeratedSequence<Base>.Element { get }
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

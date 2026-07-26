---
title: 'remove(at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/remove(at:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/remove%28at%3A%29.json'
content_hash: 'sha256:541b850cad095edf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# remove(at:)

<sub>Instance Method</sub>

Removes and returns the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(at position: Self.Index) -> Self.Element
```

## Parameters

- `position` — The position of the element to remove. `position` must be a valid index of the collection that is not equal to the collection’s end index.

## Return Value

The removed element.

## Discussion

All the elements following the specified position are moved to close the gap. This example removes the middle element from an array of measurements.

```swift
var measurements = [1.2, 1.5, 2.9, 1.2, 1.6]
let removed = measurements.remove(at: 2)
print(measurements)
// Prints "[1.2, 1.5, 1.2, 1.6]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

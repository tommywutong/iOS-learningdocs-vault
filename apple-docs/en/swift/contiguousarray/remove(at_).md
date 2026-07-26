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
doc_path: '/documentation/swift/contiguousarray/remove(at:)'
source_url: 'https://developer.apple.com/documentation/swift/contiguousarray/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/contiguousarray/remove%28at%3A%29.json'
content_hash: 'sha256:94f7ca70107d6101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ContiguousArray](../contiguousarray.md)

# remove(at:)

<sub>Instance Method</sub>

Removes and returns the element at the specified position.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(at index: Int) -> Element
```

## Parameters

- `index` — The position of the element to remove. `index` must be a valid index of the array.

## Return Value

The element at the specified index.

## Discussion

All the elements following the specified position are moved up to close the gap.

```swift
var measurements: [Double] = [1.1, 1.5, 2.9, 1.2, 1.5, 1.3, 1.2]
let removed = measurements.remove(at: 2)
print(measurements)
// Prints "[1.1, 1.5, 1.2, 1.5, 1.3, 1.2]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the array.

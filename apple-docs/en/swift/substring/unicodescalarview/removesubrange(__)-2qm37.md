---
title: 'removeSubrange(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/unicodescalarview/removesubrange(_:)-2qm37'
source_url: 'https://developer.apple.com/documentation/swift/substring/unicodescalarview/removesubrange(_:)-2qm37'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/unicodescalarview/removesubrange%28_%3A%29-2qm37.json'
content_hash: 'sha256:e92e103eeb8e64b0'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Substring](../../substring.md) · [UnicodeScalarView](../unicodescalarview.md)

# removeSubrange(_:)

<sub>Instance Method</sub>

Removes the elements in the specified subrange from the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeSubrange<R>(_ bounds: R) where R : RangeExpression, Self.Index == R.Bound
```

## Parameters

- `bounds` — The range of the collection to be removed. The bounds of the range must be valid indices of the collection.

## Discussion

All the elements following the specified position are moved to close the gap. This example removes three elements from the middle of an array of measurements.

```swift
var measurements = [1.2, 1.5, 2.9, 1.2, 1.5]
measurements.removeSubrange(1..<4)
print(measurements)
// Prints "[1.2, 1.5]"
```

Calling this method may invalidate any existing indices for use with this collection.

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the collection.

---
title: capacity
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/array/capacity
source_url: 'https://developer.apple.com/documentation/swift/array/capacity'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/array/capacity.json'
content_hash: 'sha256:f85ddd9c62befbf1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Array](../array.md)

# capacity

<sub>Instance Property</sub>

The total number of elements that the array can contain without allocating new storage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var capacity: Int { get }
```

## Discussion

Every array reserves a specific amount of memory to hold its contents. When you add elements to an array and that array begins to exceed its reserved capacity, the array allocates a larger region of memory and copies its elements into the new storage. The new storage is a multiple of the old storage’s size. This exponential growth strategy means that appending an element happens in constant time, averaging the performance of many append operations. Append operations that trigger reallocation have a performance cost, but they occur less and less often as the array grows larger.

The following example creates an array of integers from an array literal, then appends the elements of another collection. Before appending, the array allocates new storage that is large enough store the resulting elements.

```swift
var numbers = [10, 20, 30, 40, 50]
// numbers.count == 5
// numbers.capacity == 5

numbers.append(contentsOf: stride(from: 60, through: 100, by: 10))
// numbers.count == 10
// numbers.capacity == 10
```

## See Also

### Inspecting an Array

- [isEmpty](isempty.md) — A Boolean value indicating whether the collection is empty.
- [count](count.md) — The number of elements in the array.

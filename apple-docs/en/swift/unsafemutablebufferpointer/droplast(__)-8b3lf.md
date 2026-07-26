---
title: 'dropLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/droplast(_:)-8b3lf'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/droplast(_:)-8b3lf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/droplast%28_%3A%29-8b3lf.json'
content_hash: 'sha256:2bc61ae690ecc34c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# dropLast(_:)

<sub>Instance Method</sub>

Returns a sequence containing all but the given number of final elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func dropLast(_ k: Int = 1) -> [Self.Element]
```

## Return Value

A sequence leaving off the specified number of elements.

## Discussion

The sequence must be finite. If the number of elements to drop exceeds the number of elements in the sequence, the result is an empty sequence.

```swift
let numbers = [1, 2, 3, 4, 5]
print(numbers.dropLast(2))
// Prints "[1, 2, 3]"
print(numbers.dropLast(10))
// Prints "[]"
```

> [!abstract] Complexity
> O(_n_), where _n_ is the length of the sequence.

---
title: 'append(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/unicodescalarview/append(_:)-5uy8n'
source_url: 'https://developer.apple.com/documentation/swift/string/unicodescalarview/append(_:)-5uy8n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/unicodescalarview/append%28_%3A%29-5uy8n.json'
content_hash: 'sha256:edff9cc2d26e4696'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [String](../../string.md) · [UnicodeScalarView](../unicodescalarview.md)

# append(_:)

<sub>Instance Method</sub>

Adds an element to the end of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func append(_ newElement: Self.Element)
```

## Parameters

- `newElement` — The element to append to the collection.

## Discussion

If the collection does not have sufficient capacity for another element, additional storage is allocated before appending `newElement`. The following example adds a new number to an array of integers:

```swift
var numbers = [1, 2, 3, 4, 5]
numbers.append(100)

print(numbers)
// Prints "[1, 2, 3, 4, 5, 100]"
```

> [!abstract] Complexity
> O(1) on average, over many calls to `append(_:)` on the same collection.

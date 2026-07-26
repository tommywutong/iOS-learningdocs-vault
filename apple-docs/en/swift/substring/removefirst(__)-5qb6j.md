---
title: 'removeFirst(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/removefirst(_:)-5qb6j'
source_url: 'https://developer.apple.com/documentation/swift/substring/removefirst(_:)-5qb6j'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/removefirst%28_%3A%29-5qb6j.json'
content_hash: 'sha256:20385e8ad145f74f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# removeFirst(_:)

<sub>Instance Method</sub>

Removes the specified number of elements from the beginning of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeFirst(_ k: Int)
```

## Parameters

- `k` — The number of elements to remove. `k` must be greater than or equal to zero, and must be less than or equal to the number of elements in the collection.

## Discussion

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the specified number of elements.

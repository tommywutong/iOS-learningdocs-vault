---
title: 'removeLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/removelast%28_%3A%29.json'
content_hash: 'sha256:ee33b4634e7fa10d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# removeLast(_:)

<sub>Instance Method</sub>

Removes and discards the specified number of elements from the end of the array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ k: Int)
```

## Parameters

- `k` — The number of elements to remove from the array. `k` must be greater than or equal to zero and must not exceed the count of the array.

## Discussion

Attempting to remove more elements than exist in the array triggers a runtime error.

> [!abstract] Complexity
> O(`k`)

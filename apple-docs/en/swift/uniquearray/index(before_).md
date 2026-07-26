---
title: 'index(before:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/index(before:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/index(before:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/index%28before%3A%29.json'
content_hash: 'sha256:b0756fce65027acd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# index(before:)

<sub>Instance Method</sub>

Returns the position immediately before the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(before index: Int) -> Int
```

## Parameters

- `index` — A valid index of the array. `i` must be greater than `startIndex`.

## Return Value

The index immediately preceding `i`.

## Discussion

> [!note] Note
> To improve performance, this method does not validate that the index is valid before decrementing it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> [!abstract] Complexity
> O(1)

---
title: 'distance(from:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/distance(from:to:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/distance(from:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/distance%28from%3Ato%3A%29.json'
content_hash: 'sha256:c03fc83c8040e27b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# distance(from:to:)

<sub>Instance Method</sub>

Returns the distance between two indices.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func distance(from start: UniqueArray<Element>.Index, to end: UniqueArray<Element>.Index) -> Int
```

## Parameters

- `start` — A valid index of the collection.

- `end` — Another valid index of the collection. If end is equal to start, the result is zero.

## Return Value

The distance between `start` and `end`.

## Discussion

> [!note] Note
> To improve performance, this method does not validate that the given index is valid before offseting it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> [!abstract] Complexity
> O(1)

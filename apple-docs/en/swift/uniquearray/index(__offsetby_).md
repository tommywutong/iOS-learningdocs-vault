---
title: 'index(_:offsetBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/swift/uniquearray/index(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/swift/uniquearray/index(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uniquearray/index%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:48accc824fe2d57f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UniqueArray](../uniquearray.md)

# index(_:offsetBy:)

<sub>Instance Method</sub>

Returns an index that is the specified distance from the given index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func index(_ index: Int, offsetBy n: Int) -> Int
```

## Parameters

- `index` — A valid index of the array.

- `n` — The distance by which to offset `index`.

## Return Value

An index offset by distance from `index`. If `n` is positive, this is the same value as the result of `n` calls to `index(after:)`. If `n` is negative, this is the same value as the result of `abs(n)` calls to `index(before:)`.

## Discussion

The value passed as `n` must not offset `index` beyond the bounds of the array.

> [!note] Note
> To improve performance, this method does not validate that the given index is valid before offseting it. Index validation is deferred until the resulting index is used to access an element. This optimization may be removed in future versions; do not rely on it.

> [!abstract] Complexity
> O(1)

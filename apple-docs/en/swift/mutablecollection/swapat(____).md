---
title: 'swapAt(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/mutablecollection/swapat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/mutablecollection/swapat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/mutablecollection/swapat%28_%3A_%3A%29.json'
content_hash: 'sha256:46edabb020efde47'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [MutableCollection](../mutablecollection.md)

# swapAt(_:_:)

<sub>Instance Method</sub>

Exchanges the values at the specified indices of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func swapAt(_ i: Self.Index, _ j: Self.Index)
```

## Parameters

- `i` — The index of the first value to swap.

- `j` — The index of the second value to swap.

## Discussion

Both parameters must be valid indices of the collection and not equal to `endIndex`. Passing the same index as both `i` and `j` has no effect.

> [!abstract] Complexity
> O(1)

## Default Implementations

### MutableCollection Implementations

- [swapAt(_:_:)](<swapat(____)-479dx.md>) — Exchanges the values at the specified indices of the collection.

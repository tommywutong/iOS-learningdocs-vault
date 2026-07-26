---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/float80/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/float80/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/hash%28into%3A%29.json'
content_hash: 'sha256:32e725ff715f63c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>macOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> [!important] Important
> In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

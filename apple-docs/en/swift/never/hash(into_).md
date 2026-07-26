---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/never/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/never/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/never/hash%28into%3A%29.json'
content_hash: 'sha256:d12fabb2217439d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Never](../never.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## Discussion

Implement this method to conform to the `Hashable` protocol. The components used for hashing must be the same as the components compared in your type’s `==` operator implementation. Call `hasher.combine(_:)` with each of these components.

> [!important] Important
> In your implementation of `hash(into:)`, don’t call `finalize()` on the `hasher` instance provided, or replace it with a different instance. Doing so may become a compile-time error in the future.

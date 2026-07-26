---
title: 'reserveCapacity(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/reservecapacity(_:)'
source_url: 'https://developer.apple.com/documentation/swift/set/reservecapacity(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/reservecapacity%28_%3A%29.json'
content_hash: 'sha256:d02f213ae0d35c75'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# reserveCapacity(_:)

<sub>Instance Method</sub>

Reserves enough space to store the specified number of elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func reserveCapacity(_ minimumCapacity: Int)
```

## Parameters

- `minimumCapacity` — The requested number of elements to store.

## Discussion

If you are adding a known number of elements to a set, use this method to avoid multiple reallocations. This method ensures that the set has unique, mutable, contiguous storage, with space allocated for at least the requested number of elements.

Calling the `reserveCapacity(_:)` method on a set with bridged storage triggers a copy to contiguous storage even if the existing storage has room to store `minimumCapacity` elements.

## See Also

### Adding Elements

- [insert(_:)](<insert(__)-nads.md>) — Inserts the given element in the set if it is not already present.
- [insert(_:)](<insert(__)-yar4.md>)
- [update(with:)](<update(with_)-2n6tk.md>) — Inserts the given element into the set unconditionally.
- [update(with:)](<update(with_)-7r2g.md>)

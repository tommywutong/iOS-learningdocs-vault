---
title: 'update(with:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/update(with:)-7r2g'
source_url: 'https://developer.apple.com/documentation/swift/set/update(with:)-7r2g'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/update%28with%3A%29-7r2g.json'
content_hash: 'sha256:ee17716086e80890'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# update(with:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func update<ConcreteElement>(with newMember: ConcreteElement) -> ConcreteElement? where ConcreteElement : Hashable
```

## See Also

### Adding Elements

- [insert(_:)](<insert(__)-nads.md>) — Inserts the given element in the set if it is not already present.
- [insert(_:)](<insert(__)-yar4.md>)
- [update(with:)](<update(with_)-2n6tk.md>) — Inserts the given element into the set unconditionally.
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.

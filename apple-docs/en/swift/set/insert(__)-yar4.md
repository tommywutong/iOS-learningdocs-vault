---
title: 'insert(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/insert(_:)-yar4'
source_url: 'https://developer.apple.com/documentation/swift/set/insert(_:)-yar4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/insert%28_%3A%29-yar4.json'
content_hash: 'sha256:4c5cd30062b29bff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# insert(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert<ConcreteElement>(_ newMember: ConcreteElement) -> (inserted: Bool, memberAfterInsert: ConcreteElement) where ConcreteElement : Hashable
```

## See Also

### Adding Elements

- [insert(_:)](<insert(__)-nads.md>) — Inserts the given element in the set if it is not already present.
- [update(with:)](<update(with_)-2n6tk.md>) — Inserts the given element into the set unconditionally.
- [update(with:)](<update(with_)-7r2g.md>)
- [reserveCapacity(_:)](<reservecapacity(__).md>) — Reserves enough space to store the specified number of elements.

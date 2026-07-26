---
title: 'insert(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/indexset/insert(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/indexset/insert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/indexset/insert%28_%3A%29.json'
content_hash: 'sha256:2f0ec68d5834f1bd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [IndexSet](../indexset.md)

# insert(_:)

<sub>Instance Method</sub>

Insert an integer into the `IndexSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert(_ integer: IndexSet.Element) -> (inserted: Bool, memberAfterInsert: IndexSet.Element)
```

## See Also

### Inserting Elements

- [insert(integersIn:)](<insert(integersin_)-28eld.md>) — Insert a range of integers into the `IndexSet`.
- [update(with:)](<update(with_).md>) — Insert an integer into the `IndexSet`.

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
doc_path: '/documentation/foundation/characterset/insert(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/insert(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/insert%28_%3A%29.json'
content_hash: 'sha256:c449e154f7114648'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# insert(_:)

<sub>Instance Method</sub>

Insert a `Unicode.Scalar` representation of a character into the `CharacterSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func insert(_ character: Unicode.Scalar) -> (inserted: Bool, memberAfterInsert: Unicode.Scalar)
```

## Discussion

`Unicode.Scalar` values are available on `Swift.String.UnicodeScalarView`.

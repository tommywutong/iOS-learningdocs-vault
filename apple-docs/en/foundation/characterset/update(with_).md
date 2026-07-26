---
title: 'update(with:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/update(with:)'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/update(with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/update%28with%3A%29.json'
content_hash: 'sha256:ba00fa557ac5c12d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# update(with:)

<sub>Instance Method</sub>

Insert a `Unicode.Scalar` representation of a character into the `CharacterSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func update(with character: Unicode.Scalar) -> Unicode.Scalar?
```

## Discussion

`Unicode.Scalar` values are available on `Swift.String.UnicodeScalarView`.

---
title: 'remove(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/characterset/remove(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/characterset/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/characterset/remove%28_%3A%29.json'
content_hash: 'sha256:270ff3254e9983ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [CharacterSet](../characterset.md)

# remove(_:)

<sub>Instance Method</sub>

Remove a `Unicode.Scalar` representation of a character from the `CharacterSet`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(_ character: Unicode.Scalar) -> Unicode.Scalar?
```

## Discussion

`Unicode.Scalar` values are available on `Swift.String.UnicodeScalarView`.

---
title: 'replace(with:value:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/singleattributetransformer/replace(with:value:)-xg8b'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/singleattributetransformer/replace(with:value:)-xg8b'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/singleattributetransformer/replace%28with%3Avalue%3A%29-xg8b.json'
content_hash: 'sha256:dc73de59d71b4513'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [SingleAttributeTransformer](../singleattributetransformer.md)

# replace(with:value:)

<sub>Instance Method</sub>

Replaces an attribute with a different attribute that a key path identifies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency mutating func replace<U>(with keyPath: KeyPath<AttributeDynamicLookup, U>, value: U.Value) where U : AttributedStringKey, U.Value : Sendable
```

## Parameters

- `keyPath` — The key path that identifies the new attribute.

- `value` — The value of the new attribute.

## See Also

### Replacing Attributes

- [replace(with:value:)](<replace(with_value_)-6bn0e.md>) — Replaces an attribute with a different attribute.

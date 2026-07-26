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
doc_path: '/documentation/foundation/attributedstring/singleattributetransformer/replace(with:value:)-6bn0e'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/singleattributetransformer/replace(with:value:)-6bn0e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/singleattributetransformer/replace%28with%3Avalue%3A%29-6bn0e.json'
content_hash: 'sha256:a1cbf70bdf70168c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [AttributedString](../../attributedstring.md) · [SingleAttributeTransformer](../singleattributetransformer.md)

# replace(with:value:)

<sub>Instance Method</sub>

Replaces an attribute with a different attribute.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency mutating func replace<U>(with key: U.Type, value: U.Value) where U : AttributedStringKey, U.Value : Sendable
```

## Parameters

- `key` — The key of the new attribute.

- `value` — The value of the new attribute.

## See Also

### Replacing Attributes

- [replace(with:value:)](<replace(with_value_)-xg8b.md>) — Replaces an attribute with a different attribute that a key path identifies.

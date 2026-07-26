---
title: 'transformingAttributes(_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/transformingattributes(_:_:)-64qnl'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transformingattributes(_:_:)-64qnl'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transformingattributes%28_%3A_%3A%29-64qnl.json'
content_hash: 'sha256:31feb8ea27da4185'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transformingAttributes(_:_:)

<sub>Instance Method</sub>

Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func transformingAttributes<K>(_ k: KeyPath<AttributeDynamicLookup, K>, _ c: (inout AttributedString.SingleAttributeTransformer<K>) -> Void) -> AttributedString where K : AttributedStringKey, K.Value : Sendable
```

## Parameters

- `k` — The key path to the [AttributedStringKey](../attributedstringkey.md) that identifies the attribute to transform.

- `c` — The closure that receives an [SingleAttributeTransformer](singleattributetransformer.md) that you use to access and alter the attribute’s range and value.

## Return Value

An attributed string with the applied transformation to the specified attribute.

## See Also

### Transforming Attributes

- [transformingAttributes(_:_:)](<transformingattributes(____)-9prm2.md>) — Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [transformingAttributes(_:_:_:)](<transformingattributes(______)-7kw1o.md>) — Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.
- [transformingAttributes(_:_:_:)](<transformingattributes(______)-8gt2n.md>) — Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-4owv7.md>) — Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-5xmlf.md>) — Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-9uodg.md>) — Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-all0.md>) — Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-3i7ac.md>) — Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-9hppo.md>) — Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.
- [SingleAttributeTransformer](singleattributetransformer.md) — A type that transforms an attribute by altering its range or value, or by replacing it entirely.

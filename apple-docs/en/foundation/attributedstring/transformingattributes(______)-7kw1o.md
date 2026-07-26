---
title: 'transformingAttributes(_:_:_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/attributedstring/transformingattributes(_:_:_:)-7kw1o'
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/transformingattributes(_:_:_:)-7kw1o'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/transformingattributes%28_%3A_%3A_%3A%29-7kw1o.json'
content_hash: 'sha256:de7899a16fafba1a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# transformingAttributes(_:_:_:)

<sub>Instance Method</sub>

Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func transformingAttributes<K1, K2>(_ k: K1.Type, _ k2: K2.Type, _ c: (inout AttributedString.SingleAttributeTransformer<K1>, inout AttributedString.SingleAttributeTransformer<K2>) -> Void) -> AttributedString where K1 : AttributedStringKey, K2 : AttributedStringKey, K1.Value : Sendable, K2.Value : Sendable
```

## Parameters

- `k` — The [AttributedStringKey](../attributedstringkey.md) that identifies an attribute to transform.

- `k2` — The [AttributedStringKey](../attributedstringkey.md) that identifies a second attribute to transform.

- `c` — A closure that receives two [SingleAttributeTransformer](singleattributetransformer.md) instances that you use to access and alter the attributes’ ranges and values.

## Return Value

An attributed string with the applied transformations to the specified attributes.

## See Also

### Transforming Attributes

- [transformingAttributes(_:_:)](<transformingattributes(____)-9prm2.md>) — Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [transformingAttributes(_:_:)](<transformingattributes(____)-64qnl.md>) — Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.
- [transformingAttributes(_:_:_:)](<transformingattributes(______)-8gt2n.md>) — Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-4owv7.md>) — Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-5xmlf.md>) — Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-9uodg.md>) — Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-all0.md>) — Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-3i7ac.md>) — Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-9hppo.md>) — Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.
- [SingleAttributeTransformer](singleattributetransformer.md) — A type that transforms an attribute by altering its range or value, or by replacing it entirely.

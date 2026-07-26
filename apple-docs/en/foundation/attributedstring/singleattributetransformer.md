---
title: AttributedString.SingleAttributeTransformer
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/attributedstring/singleattributetransformer
source_url: 'https://developer.apple.com/documentation/foundation/attributedstring/singleattributetransformer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/attributedstring/singleattributetransformer.json'
content_hash: 'sha256:d67b24f9d5ab5f6a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [AttributedString](../attributedstring.md)

# AttributedString.SingleAttributeTransformer

<sub>Structure</sub>

A type that transforms an attribute by altering its range or value, or by replacing it entirely.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency struct SingleAttributeTransformer<T> where T : AttributedStringKey, T.Value : Sendable
```

## Overview

For simple transformations, the closure you provide to the `transformingAttributes(…)` methods of [AttributedString](../attributedstring.md) can use this instance to change the attribute’s value. You can also use this instance to change the range of the string that the attribute applies to. To completely replace the attribute with an attribute of a different type, use [replace(with:value:)](<singleattributetransformer/replace(with_value_)-6bn0e.md>).

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Accessing the Attribute’s Range

- [range](singleattributetransformer/range.md) — The range of the attribute in the attributed string.

### Accessing the Attribute’s Value

- [value](singleattributetransformer/value.md) — The value of the attribute.

### Replacing Attributes

- [replace(with:value:)](<singleattributetransformer/replace(with_value_)-6bn0e.md>) — Replaces an attribute with a different attribute.
- [replace(with:value:)](<singleattributetransformer/replace(with_value_)-xg8b.md>) — Replaces an attribute with a different attribute that a key path identifies.

## See Also

### Transforming Attributes

- [transformingAttributes(_:_:)](<transformingattributes(____)-9prm2.md>) — Returns an attributed string by calling a closure that transforms one attribute of a source attributed string.
- [transformingAttributes(_:_:)](<transformingattributes(____)-64qnl.md>) — Returns an attributed string by calling a closure that transforms one attribute, which a key path identifies, of a source attributed string.
- [transformingAttributes(_:_:_:)](<transformingattributes(______)-7kw1o.md>) — Returns an attributed string by calling a closure that transforms two attributes of a source attributed string.
- [transformingAttributes(_:_:_:)](<transformingattributes(______)-8gt2n.md>) — Returns an attributed string created by calling a closure that transforms two attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-4owv7.md>) — Returns an attributed string by calling a closure that transforms three attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:)](<transformingattributes(________)-5xmlf.md>) — Returns an attributed string by calling a closure that transforms three attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-9uodg.md>) — Returns an attributed string by calling a closure that transforms four attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:)](<transformingattributes(__________)-all0.md>) — Returns an attributed string created by calling a closure that transforms four attributes, which key paths identify, of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-3i7ac.md>) — Returns an attributed string created by calling a closure that transforms five attributes of a source attributed string.
- [transformingAttributes(_:_:_:_:_:_:)](<transformingattributes(____________)-9hppo.md>) — Returns an attributed string created by calling a closure that transforms five attributes, which key paths identify, of a source attributed string.

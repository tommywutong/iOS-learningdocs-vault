---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/description
source_url: 'https://developer.apple.com/documentation/swift/float80/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/description.json'
content_hash: 'sha256:b87bfc34001e4885'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# description

<sub>Instance Property</sub>

A textual representation of the value.

<sub>macOS</sub>

```swift
var description: String { get }
```

## Discussion

For any finite value, this property provides a string that can be converted back to an instance of `Float80` without rounding errors.  That is, if `x` is an instance of `Float80`, then `Float80(x.description) == x` is always true.  For any NaN value, the property’s value is “nan”, and for positive and negative infinity its value is “inf” and “-inf”.

---
title: isCanonical
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.10+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float80/iscanonical
source_url: 'https://developer.apple.com/documentation/swift/float80/iscanonical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float80/iscanonical.json'
content_hash: 'sha256:04fa1f7cb957d06d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float80](../float80.md)

# isCanonical

<sub>Instance Property</sub>

A Boolean value indicating whether the instance’s representation is in its canonical form.

<sub>macOS</sub>

```swift
var isCanonical: Bool { get }
```

## Discussion

The [IEEE 754 specification](http://ieeexplore.ieee.org/servlet/opac?punumber=4610933) defines a _canonical_, or preferred, encoding of a floating-point value. On platforms that fully support IEEE 754, every `Float` or `Double` value is canonical, but non-canonical values can exist on other platforms or for other types. Some examples:

- On platforms that flush subnormal numbers to zero (such as armv7 with the default floating-point environment), Swift interprets subnormal `Float` and `Double` values as non-canonical zeros. (In Swift 5.1 and earlier, `isCanonical` is `true` for these values, which is the incorrect value.)
- On i386 and x86_64, `Float80` has a number of non-canonical encodings. “Pseudo-NaNs”, “pseudo-infinities”, and “unnormals” are interpreted as non-canonical NaN encodings. “Pseudo-denormals” are interpreted as non-canonical encodings of subnormal values.
- Decimal floating-point types admit a large number of non-canonical encodings. Consult the IEEE 754 standard for additional details.

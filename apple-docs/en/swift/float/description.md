---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/float/description
source_url: 'https://developer.apple.com/documentation/swift/float/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/float/description.json'
content_hash: 'sha256:2538965f5d3aba5e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Float](../float.md)

# description

<sub>Instance Property</sub>

A textual representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

For any finite value, this property provides a string that can be converted back to an instance of `Float` without rounding errors.  That is, if `x` is an instance of `Float`, then `Float(x.description) == x` is always true.  For any NaN value, the property’s value is “nan”, and for positive and negative infinity its value is “inf” and “-inf”.

## See Also

### Describing a Float

- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.
- [debugDescription](debugdescription.md) — A textual representation of the value, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `Float` instance.
- [hashValue](hashvalue.md) — The hash value.

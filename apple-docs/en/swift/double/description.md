---
title: description
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/double/description
source_url: 'https://developer.apple.com/documentation/swift/double/description'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/double/description.json'
content_hash: 'sha256:67b50b6e4aa94693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Double](../double.md)

# description

<sub>Instance Property</sub>

A textual representation of the value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var description: String { get }
```

## Discussion

For any finite value, this property provides a string that can be converted back to an instance of `Double` without rounding errors.  That is, if `x` is an instance of `Double`, then `Double(x.description) == x` is always true.  For any NaN value, the property’s value is “nan”, and for positive and negative infinity its value is “inf” and “-inf”.

## See Also

### Describing a Double

- [debugDescription](debugdescription.md) — A textual representation of the value, suitable for debugging.
- [customMirror](custommirror.md) — A mirror that reflects the `Double` instance.
- [hash(into:)](<hash(into_).md>) — Hashes the essential components of this value by feeding them into the given hasher.

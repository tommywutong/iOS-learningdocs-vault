---
title: 'hash(into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/hash(into:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/hash(into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/hash%28into%3A%29.json'
content_hash: 'sha256:b3f3637e023e0d06'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# hash(into:)

<sub>Instance Method</sub>

Hashes the essential components of this value by feeding them into the given hasher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func hash(into hasher: inout Hasher)
```

## Parameters

- `hasher` — The hasher to use when combining the components of this instance.

## See Also

### Inspecting a Scalar

- [value](value.md) — A numeric representation of the Unicode scalar.
- [properties](properties-swift.property.md) — Properties of this scalar defined by the Unicode standard.
- [Properties](properties-swift.struct.md) — A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [isASCII](isascii.md) — A Boolean value indicating whether the Unicode scalar is an ASCII character.

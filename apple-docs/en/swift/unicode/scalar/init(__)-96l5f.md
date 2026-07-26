---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/scalar/init(_:)-96l5f'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-96l5f'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/init%28_%3A%29-96l5f.json'
content_hash: 'sha256:3c0153850237d7f6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# init(_:)

<sub>Initializer</sub>

Creates a Unicode scalar with the specified numeric value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ v: Int)
```

## Parameters

- `v` — The Unicode code point to use for the scalar. `v` must be a valid Unicode scalar value, in the ranges `0...0xD7FF` or `0xE000...0x10FFFF`. In case of an invalid unicode scalar value, nil is returned.

## Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of an emoji character:

```swift
let codepoint = 127881
let emoji = Unicode.Scalar(codepoint)!
print(emoji)
// Prints "🎉"
```

In case of an invalid input value, nil is returned.

```swift
let codepoint: UInt32 = extValue // This might be an invalid value.
if let emoji = Unicode.Scalar(codepoint) {
  print(emoji)
} else {
  // Do something else
}
```

## See Also

### Creating a Scalar

- [init(_:)](<init(__)-2oo2e.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-5d6us.md>) — Creates a duplicate of the given Unicode scalar.
- [init(_:)](<init(__)-9eo1y.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-18u1m.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral:)](<init(unicodescalarliteral_).md>) — Creates a Unicode scalar with the specified value.
- [init(_:)](<init(__)-4p868.md>) — Instantiates an instance of the conforming type from a string representation.

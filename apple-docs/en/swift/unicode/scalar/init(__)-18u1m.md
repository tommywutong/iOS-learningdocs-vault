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
doc_path: '/documentation/swift/unicode/scalar/init(_:)-18u1m'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-18u1m'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/init%28_%3A%29-18u1m.json'
content_hash: 'sha256:0c412cfd1f52819c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# init(_:)

<sub>Initializer</sub>

Creates a Unicode scalar with the specified numeric value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(_ v: UInt16)
```

## Parameters

- `v` — The Unicode code point to use for the scalar. The initializer succeeds if `v` is a valid Unicode scalar value, in the range `0...0xD7FF` or `0xE000...0x10FFFF`. If `v` is an invalid unicode scalar value, the result is `nil`.

## Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of `"밥"`, the Korean word for rice:

```swift
let codepoint: UInt16 = 48165
let bap = Unicode.Scalar(codepoint)
print(bap!)
// Prints "밥"
```

In case of an invalid input value, the result is `nil`.

```swift
let codepoint: UInt16 = extValue   // This might be an invalid value
if let bap = Unicode.Scalar(codepoint) {
    print(bap)
} else {
    // Do something else
}
```

## See Also

### Creating a Scalar

- [init(_:)](<init(__)-2oo2e.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-5d6us.md>) — Creates a duplicate of the given Unicode scalar.
- [init(_:)](<init(__)-9eo1y.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-96l5f.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral:)](<init(unicodescalarliteral_).md>) — Creates a Unicode scalar with the specified value.
- [init(_:)](<init(__)-4p868.md>) — Instantiates an instance of the conforming type from a string representation.

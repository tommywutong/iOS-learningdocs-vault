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
doc_path: '/documentation/swift/unicode/scalar/init(_:)-2oo2e'
source_url: 'https://developer.apple.com/documentation/swift/unicode/scalar/init(_:)-2oo2e'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/scalar/init%28_%3A%29-2oo2e.json'
content_hash: 'sha256:bed0bc351e8c0590'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [Scalar](../scalar.md)

# init(_:)

<sub>Initializer</sub>

Creates a Unicode scalar with the specified numeric value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(_ v: UInt8)
```

## Parameters

- `v` — The code point to use for the scalar.

## Discussion

For example, the following code sample creates a `Unicode.Scalar` instance with a value of `"7"`:

```swift
let codepoint: UInt8 = 55
let seven = Unicode.Scalar(codepoint)
print(seven)
// Prints "7"
```

## See Also

### Creating a Scalar

- [init(_:)](<init(__)-5d6us.md>) — Creates a duplicate of the given Unicode scalar.
- [init(_:)](<init(__)-9eo1y.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-18u1m.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(_:)](<init(__)-96l5f.md>) — Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral:)](<init(unicodescalarliteral_).md>) — Creates a Unicode scalar with the specified value.
- [init(_:)](<init(__)-4p868.md>) — Instantiates an instance of the conforming type from a string representation.

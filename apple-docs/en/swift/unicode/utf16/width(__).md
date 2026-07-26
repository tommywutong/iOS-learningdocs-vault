---
title: 'width(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf16/width(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf16/width(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf16/width%28_%3A%29.json'
content_hash: 'sha256:ffe2eb70ac663cf8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF16](../utf16.md)

# width(_:)

<sub>Type Method</sub>

Returns the number of code units required to encode the given Unicode scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func width(_ x: Unicode.Scalar) -> Int
```

## Parameters

- `x` — A Unicode scalar value.

## Return Value

The width of `x` when encoded in UTF-16, either `1` or `2`.

## Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-16 by a pair of 16-bit code units. The first and second code units of the pair, designated _leading_ and _trailing_ surrogates, make up a _surrogate pair_.

```swift
let anA: Unicode.Scalar = "A"
print(anA.value)
// Prints "65"
print(UTF16.width(anA))
// Prints "1"

let anApple: Unicode.Scalar = "🍎"
print(anApple.value)
// Prints "127822"
print(UTF16.width(anApple))
// Prints "2"
```

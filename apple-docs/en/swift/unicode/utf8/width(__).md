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
doc_path: '/documentation/swift/unicode/utf8/width(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/width(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/width%28_%3A%29.json'
content_hash: 'sha256:7163ed493af5c7ed'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF8](../utf8.md)

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

The width of `x` when encoded in UTF-8, from `1` to `4`.

## Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-8 by a sequence of up to 4 code units. The first code unit is designated a _lead_ byte and the rest are _continuation_ bytes.

```swift
let anA: Unicode.Scalar = "A"
print(anA.value)
// Prints "65"
print(UTF8.width(anA))
// Prints "1"

let anApple: Unicode.Scalar = "🍎"
print(anApple.value)
// Prints "127822"
print(UTF8.width(anApple))
// Prints "4"
```

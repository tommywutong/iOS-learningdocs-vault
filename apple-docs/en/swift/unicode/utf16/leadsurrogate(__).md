---
title: 'leadSurrogate(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf16/leadsurrogate(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf16/leadsurrogate(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf16/leadsurrogate%28_%3A%29.json'
content_hash: 'sha256:2cdfb5a4c8b28a48'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF16](../utf16.md)

# leadSurrogate(_:)

<sub>Type Method</sub>

Returns the high-surrogate code unit of the surrogate pair representing the specified Unicode scalar.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func leadSurrogate(_ x: Unicode.Scalar) -> UTF16.CodeUnit
```

## Parameters

- `x` — A Unicode scalar value. `x` must be represented by a surrogate pair when encoded in UTF-16. To check whether `x` is represented by a surrogate pair, use `UTF16.width(x) == 2`.

## Return Value

The leading surrogate code unit of `x` when encoded in UTF-16.

## Discussion

Because a Unicode scalar value can require up to 21 bits to store its value, some Unicode scalars are represented in UTF-16 by a pair of 16-bit code units. The first and second code units of the pair, designated _leading_ and _trailing_ surrogates, make up a _surrogate pair_.

```swift
let apple: Unicode.Scalar = "🍎"
print(UTF16.leadSurrogate(apple))
// Prints "55356"
```

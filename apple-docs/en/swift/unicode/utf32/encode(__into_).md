---
title: 'encode(_:into:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf32/encode(_:into:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf32/encode(_:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf32/encode%28_%3Ainto%3A%29.json'
content_hash: 'sha256:8684faff50cb3638'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF32](../utf32.md)

# encode(_:into:)

<sub>Type Method</sub>

Encodes a Unicode scalar as a UTF-32 code unit by calling the given closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encode(_ input: Unicode.Scalar, into processCodeUnit: (Unicode.UTF32.CodeUnit) -> Void)
```

## Parameters

- `input` — The Unicode scalar value to encode.

- `processCodeUnit` — A closure that processes one code unit argument at a time.

## Discussion

For example, like every Unicode scalar, the musical fermata symbol (“𝄐”) can be represented in UTF-32 as a single code unit. The following code encodes a fermata in UTF-32:

```swift
var codeUnit: UTF32.CodeUnit = 0
UTF32.encode("𝄐", into: { codeUnit = $0 })
print(codeUnit)
// Prints "119056"
```

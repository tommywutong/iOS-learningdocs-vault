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
doc_path: '/documentation/swift/unicodecodec/encode(_:into:)'
source_url: 'https://developer.apple.com/documentation/swift/unicodecodec/encode(_:into:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicodecodec/encode%28_%3Ainto%3A%29.json'
content_hash: 'sha256:f8e01461af1dd088'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnicodeCodec](../unicodecodec.md)

# encode(_:into:)

<sub>Type Method</sub>

Encodes a Unicode scalar as a series of code units by calling the given closure on each code unit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func encode(_ input: Unicode.Scalar, into processCodeUnit: (Self.CodeUnit) -> Void)
```

## Parameters

- `input` — The Unicode scalar value to encode.

- `processCodeUnit` — A closure that processes one code unit argument at a time.

## Discussion

For example, the musical fermata symbol (“𝄐”) is a single Unicode scalar value (`\u{1D110}`) but requires four code units for its UTF-8 representation. The following code uses the `UTF8` codec to encode a fermata in UTF-8:

```swift
var bytes: [UTF8.CodeUnit] = []
UTF8.encode("𝄐", into: { bytes.append($0) })
print(bytes)
// Prints "[240, 157, 132, 144]"
```

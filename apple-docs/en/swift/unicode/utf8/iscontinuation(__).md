---
title: 'isContinuation(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unicode/utf8/iscontinuation(_:)'
source_url: 'https://developer.apple.com/documentation/swift/unicode/utf8/iscontinuation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unicode/utf8/iscontinuation%28_%3A%29.json'
content_hash: 'sha256:137307978c88e1b3'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [Unicode](../../unicode.md) · [UTF8](../utf8.md)

# isContinuation(_:)

<sub>Type Method</sub>

Returns a Boolean value indicating whether the specified code unit is a UTF-8 continuation byte.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func isContinuation(_ byte: Unicode.UTF8.CodeUnit) -> Bool
```

## Parameters

- `byte` — A UTF-8 code unit.

## Return Value

`true` if `byte` is a continuation byte; otherwise, `false`.

## Discussion

Continuation bytes take the form `0b10xxxxxx`. For example, a lowercase “e” with an acute accent above it (`"é"`) uses 2 bytes for its UTF-8 representation: `0b11000011` (195) and `0b10101001` (169). The second byte is a continuation byte.

```swift
let eAcute = "é"
for codeUnit in eAcute.utf8 {
    print(codeUnit, UTF8.isContinuation(codeUnit))
}
// Prints "195 false"
// Prints "169 true"
```

---
title: isKnownASCII
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/utf8span/isknownascii
source_url: 'https://developer.apple.com/documentation/swift/utf8span/isknownascii'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/utf8span/isknownascii.json'
content_hash: 'sha256:428e123f67ca1dd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UTF8Span](../utf8span.md)

# isKnownASCII

<sub>Instance Property</sub>

Returns whether contents are known to be all-ASCII. A return value of `true` means that all code units are ASCII. A return value of `false` means there _may_ be non-ASCII content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isKnownASCII: Bool { get }
```

## Discussion

ASCII-ness is checked and remembered during UTF-8 validation, so this is often equivalent to is-ASCII, but there are some situations where we might return `false` even when the content happens to be all-ASCII.

For example, a UTF-8 span generated from a `String` that at some point contained non-ASCII content would report false for `isKnownASCII`, even if that String had subsequent mutation operations that removed any non-ASCII content.

> [!abstract] Complexity
> O(1)

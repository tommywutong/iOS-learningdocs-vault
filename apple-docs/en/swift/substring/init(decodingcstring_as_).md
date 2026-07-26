---
title: 'init(decodingCString:as:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/init(decodingcstring:as:)'
source_url: 'https://developer.apple.com/documentation/swift/substring/init(decodingcstring:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/init%28decodingcstring%3Aas%3A%29.json'
content_hash: 'sha256:646b0915817aa0c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# init(decodingCString:as:)

<sub>Initializer</sub>

Creates a string from the null-terminated sequence of bytes at the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Encoding>(decodingCString nullTerminatedCodeUnits: UnsafePointer<Encoding.CodeUnit>, as sourceEncoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

## Parameters

- `nullTerminatedCodeUnits` — A pointer to a sequence of contiguous code units in the encoding specified in `sourceEncoding`, ending just before the first zero code unit.

- `sourceEncoding` — The encoding in which the code units should be interpreted.

---
title: 'init(decoding:as:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/stringprotocol/init(decoding:as:)'
source_url: 'https://developer.apple.com/documentation/swift/stringprotocol/init(decoding:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stringprotocol/init%28decoding%3Aas%3A%29.json'
content_hash: 'sha256:8d5955d0e501a073'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StringProtocol](../stringprotocol.md)

# init(decoding:as:)

<sub>Initializer</sub>

Creates a string from the given Unicode code units in the specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<C, Encoding>(decoding codeUnits: C, as sourceEncoding: Encoding.Type) where C : Collection, Encoding : _UnicodeEncoding, C.Element == Encoding.CodeUnit
```

## Parameters

- `codeUnits` — A collection of code units encoded in the encoding specified in `sourceEncoding`.

- `sourceEncoding` — The encoding in which `codeUnits` should be interpreted.

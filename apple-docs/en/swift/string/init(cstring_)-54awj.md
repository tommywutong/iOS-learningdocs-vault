---
title: 'init(cString:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（6.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/init(cstring:)-54awj'
source_url: 'https://developer.apple.com/documentation/swift/string/init(cstring:)-54awj'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28cstring%3A%29-54awj.json'
content_hash: 'sha256:bc2787df64d38f27'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(cString:)

<sub>Initializer</sub>

Creates a new string by copying the null-terminated UTF-8 data referenced by the given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(cString nullTerminatedUTF8: [CChar])
```

## Parameters

- `nullTerminatedUTF8` — An array containing a null-terminated sequence of UTF-8 code units.

## Discussion

If `cString` contains ill-formed UTF-8 code unit sequences, this initializer replaces them with the Unicode replacement character (`"\u{FFFD}"`).

> [!note] Note
> This initializer is deprecated. Use the initializer `String.init(decoding: array, as: UTF8.self)` instead, remembering that “\\0” is a valid character in Swift.

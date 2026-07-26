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
doc_path: '/documentation/swift/string/init(decodingcstring:as:)-8yowf'
source_url: 'https://developer.apple.com/documentation/swift/string/init(decodingcstring:as:)-8yowf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28decodingcstring%3Aas%3A%29-8yowf.json'
content_hash: 'sha256:94aa0256f3f48d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(decodingCString:as:)

<sub>Initializer</sub>

Creates a new string by copying the null-terminated sequence of code units referenced by the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<Encoding>(decodingCString nullTerminatedCodeUnits: UnsafePointer<Encoding.CodeUnit>, as encoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

## Parameters

- `nullTerminatedCodeUnits` — A pointer to a null-terminated sequence of code units encoded in `encoding`.

- `encoding` — The encoding in which the code units should be interpreted.

## Discussion

If `nullTerminatedCodeUnits` contains ill-formed code unit sequences, this initializer replaces them with the Unicode replacement character (`"\u{FFFD}"`).

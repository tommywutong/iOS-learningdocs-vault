---
title: 'init(decoding:as:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(decoding:as:)'
source_url: 'https://developer.apple.com/documentation/swift/string/init(decoding:as:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28decoding%3Aas%3A%29.json'
content_hash: 'sha256:d255158838867547'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

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

## See Also

### Creating a String from Unicode Data

- [init(_:)](<init(__)-8ay23.md>)
- [init(data:encoding:)](<init(data_encoding_).md>) — Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init(validatingUTF8:)](<init(validatingutf8_)-208fn.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validating:as:)](<init(validating_as_)-84qr9.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(validating:as:)](<init(validating_as_)-5cw2c.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(utf8String:)](<init(utf8string_)-8qmaq.md>) — Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init(utf8String:)](<init(utf8string_)-3mcco.md>) — Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits:count:)](<init(utf16codeunits_count_).md>) — Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy:count:freeWhenDone:)](<init(utf16codeunitsnocopy_count_freewhendone_).md>) — Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units. _(deprecated)_

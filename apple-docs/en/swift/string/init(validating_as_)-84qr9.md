---
title: 'init(validating:as:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+, visionOS 2.0+, watchOS 11.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(validating:as:)-84qr9'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validating:as:)-84qr9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validating%3Aas%3A%29-84qr9.json'
content_hash: 'sha256:ed3d5d51f4575039'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validating:as:)

<sub>Initializer</sub>

Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?<Encoding>(validating codeUnits: some Sequence, as encoding: Encoding.Type) where Encoding : _UnicodeEncoding
```

## Parameters

- `codeUnits` — A sequence of code units that encode a `String`

- `encoding` — A conformer to `Unicode.Encoding` to be used to decode `codeUnits`.

## Discussion

This initializer does not try to repair ill-formed code unit sequences. If any are found, the result of the initializer is `nil`.

The following example calls this initializer with the contents of two different arrays—first with a well-formed UTF-8 code unit sequence and then with an ill-formed UTF-16 code unit sequence.

```swift
let validUTF8: [UInt8] = [67, 97, 0, 102, 195, 169]
let valid = String(validating: validUTF8, as: UTF8.self)
print(valid ?? "nil")
// Prints "Café"

let invalidUTF16: [UInt16] = [0x41, 0x42, 0xd801]
let invalid = String(validating: invalidUTF16, as: UTF16.self)
print(invalid ?? "nil")
// Prints "nil"
```

## See Also

### Creating a String from Unicode Data

- [init(_:)](<init(__)-8ay23.md>)
- [init(data:encoding:)](<init(data_encoding_).md>) — Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init(validatingUTF8:)](<init(validatingutf8_)-208fn.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validating:as:)](<init(validating_as_)-5cw2c.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(utf8String:)](<init(utf8string_)-8qmaq.md>) — Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init(utf8String:)](<init(utf8string_)-3mcco.md>) — Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits:count:)](<init(utf16codeunits_count_).md>) — Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy:count:freeWhenDone:)](<init(utf16codeunitsnocopy_count_freewhendone_).md>) — Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units. _(deprecated)_
- [init(decoding:as:)](<init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.

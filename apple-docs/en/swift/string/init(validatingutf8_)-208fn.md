---
title: 'init(validatingUTF8:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（6.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/init(validatingutf8:)-208fn'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validatingutf8:)-208fn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validatingutf8%3A%29-208fn.json'
content_hash: 'sha256:66145f360c1a59f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validatingUTF8:)

<sub>Initializer</sub>

Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(validatingUTF8 cString: UnsafePointer<CChar>)
```

## Parameters

- `cString` — A pointer to a null-terminated sequence of UTF-8 code units.

## Discussion

This initializer does not try to repair ill-formed UTF-8 code unit sequences. If any are found, the result of the initializer is `nil`.

The following example calls this initializer with pointers to the contents of two different `CChar` arrays—the first with well-formed UTF-8 code unit sequences and the second with an ill-formed sequence at the end.

```swift
let validUTF8: [CChar] = [67, 97, 102, -61, -87, 0]
validUTF8.withUnsafeBufferPointer { ptr in
    let s = String(validatingUTF8: ptr.baseAddress!)
    print(s)
}
// Prints "Optional("Café")"

let invalidUTF8: [CChar] = [67, 97, 102, -61, 0]
invalidUTF8.withUnsafeBufferPointer { ptr in
    let s = String(validatingUTF8: ptr.baseAddress!)
    print(s)
}
// Prints "nil"
```

> [!note] Note
> This initializer has been renamed. Use `String.init?(validatingCString:)` instead.

## See Also

### Creating a String from Unicode Data

- [init(_:)](<init(__)-8ay23.md>)
- [init(data:encoding:)](<init(data_encoding_).md>) — Returns a `String` initialized by converting given `data` into Unicode characters using a given `encoding`.
- [init(validating:as:)](<init(validating_as_)-84qr9.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(validating:as:)](<init(validating_as_)-5cw2c.md>) — Creates a new string by copying and validating the sequence of code units passed in, according to the specified encoding.
- [init(utf8String:)](<init(utf8string_)-8qmaq.md>) — Creates a string by copying the data from a given null-terminated array of UTF8-encoded bytes.
- [init(utf8String:)](<init(utf8string_)-3mcco.md>) — Creates a string by copying the data from a given null-terminated C array of UTF8-encoded bytes.
- [init(utf16CodeUnits:count:)](<init(utf16codeunits_count_).md>) — Creates a new string that contains the specified number of characters from the given C array of Unicode characters.
- [init(utf16CodeUnitsNoCopy:count:freeWhenDone:)](<init(utf16codeunitsnocopy_count_freewhendone_).md>) — Creates a new string that contains the specified number of characters from the given C array of UTF-16 code units. _(deprecated)_
- [init(decoding:as:)](<init(decoding_as_).md>) — Creates a string from the given Unicode code units in the specified encoding.

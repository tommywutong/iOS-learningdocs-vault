---
title: 'init(validatingCString:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+, Swift（6.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/swift/string/init(validatingcstring:)-98wra'
source_url: 'https://developer.apple.com/documentation/swift/string/init(validatingcstring:)-98wra'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28validatingcstring%3A%29-98wra.json'
content_hash: 'sha256:2f25d809a63c3247'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(validatingCString:)

<sub>Initializer</sub>

Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(validatingCString nullTerminatedUTF8: [CChar])
```

## Parameters

- `nullTerminatedUTF8` — An array containing a null-terminated sequence of UTF-8 code units.

## Discussion

This initializer does not try to repair ill-formed UTF-8 code unit sequences. If any are found, the result of the initializer is `nil`.

> [!note] Note
> This initializer is deprecated. Use the initializer `String.init?(validating: array, as: UTF8.self)` instead, remembering that “\\0” is a valid character in Swift.

## See Also

### Converting a C String

- [init(bytes:encoding:)](<init(bytes_encoding_).md>) — Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init(bytesNoCopy:length:encoding:freeWhenDone:)](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer. _(deprecated)_
- [init(validatingCString:)](<init(validatingcstring_)-992vo.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](<init(cstring_)-2p84k.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](<init(cstring_)-6kr8s.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:encoding:)](<init(cstring_encoding_)-3h7bc.md>) — Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init(cString:encoding:)](<init(cstring_encoding_)-3qgzd.md>) — Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init(decodingCString:as:)](<init(decodingcstring_as_)-8way7.md>) — Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [decodeCString(_:as:repairingInvalidCodeUnits:)](<decodecstring(__as_repairinginvalidcodeunits_)-46n2p.md>) — Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.

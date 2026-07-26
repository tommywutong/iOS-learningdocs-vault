---
title: 'init(cString:encoding:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 8.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/init(cstring:encoding:)-3h7bc'
source_url: 'https://developer.apple.com/documentation/swift/string/init(cstring:encoding:)-3h7bc'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/init%28cstring%3Aencoding%3A%29-3h7bc.json'
content_hash: 'sha256:6f86f9d0b1d8d10b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# init(cString:encoding:)

<sub>Initializer</sub>

Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init?(cString: [CChar], encoding enc: String.Encoding)
```

## See Also

### Converting a C String

- [init(bytes:encoding:)](<init(bytes_encoding_).md>) — Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init(bytesNoCopy:length:encoding:freeWhenDone:)](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer. _(deprecated)_
- [init(validatingCString:)](<init(validatingcstring_)-992vo.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validatingCString:)](<init(validatingcstring_)-98wra.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](<init(cstring_)-2p84k.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](<init(cstring_)-6kr8s.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:encoding:)](<init(cstring_encoding_)-3qgzd.md>) — Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init(decodingCString:as:)](<init(decodingcstring_as_)-8way7.md>) — Creates a new string by copying the null-terminated sequence of code units referenced by the given array.
- [decodeCString(_:as:repairingInvalidCodeUnits:)](<decodecstring(__as_repairinginvalidcodeunits_)-46n2p.md>) — Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.

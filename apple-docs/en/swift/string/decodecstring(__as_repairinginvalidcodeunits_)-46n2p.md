---
title: 'decodeCString(_:as:repairingInvalidCodeUnits:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-46n2p'
source_url: 'https://developer.apple.com/documentation/swift/string/decodecstring(_:as:repairinginvalidcodeunits:)-46n2p'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/string/decodecstring%28_%3Aas%3Arepairinginvalidcodeunits%3A%29-46n2p.json'
content_hash: 'sha256:537bdc784a3646ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [String](../string.md)

# decodeCString(_:as:repairingInvalidCodeUnits:)

<sub>Type Method</sub>

Creates a new string by copying the null-terminated data referenced by the given pointer using the specified encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func decodeCString<Encoding>(_ cString: UnsafePointer<Encoding.CodeUnit>?, as encoding: Encoding.Type, repairingInvalidCodeUnits isRepairing: Bool = true) -> (result: String, repairsMade: Bool)? where Encoding : _UnicodeEncoding
```

## Parameters

- `cString` — A pointer to a null-terminated sequence of code units encoded in `encoding`.

- `encoding` — The Unicode encoding of the data referenced by `cString`.

- `isRepairing` — Pass `true` to create a new string, even when the data referenced by `cString` contains ill-formed sequences. Ill-formed sequences are replaced with the Unicode replacement character (`"\u{FFFD}"`). Pass `false` to interrupt the creation of the new string if an ill-formed sequence is detected.

## Return Value

A tuple with the new string and a Boolean value that indicates whether any repairs were made. If `isRepairing` is `false` and an ill-formed sequence is detected, this method returns `nil`.

## Discussion

When you pass `true` as `isRepairing`, this method replaces ill-formed sequences with the Unicode replacement character (`"\u{FFFD}"`); otherwise, an ill-formed sequence causes this method to stop decoding and return `nil`.

The following example calls this method with pointers to the contents of two different `CChar` arrays—the first with well-formed UTF-8 code unit sequences and the second with an ill-formed sequence at the end.

```swift
let validUTF8: [UInt8] = [67, 97, 102, 195, 169, 0]
validUTF8.withUnsafeBufferPointer { ptr in
    let s = String.decodeCString(ptr.baseAddress,
                                 as: UTF8.self,
                                 repairingInvalidCodeUnits: true)
    print(s)
}
// Prints "Optional((result: "Café", repairsMade: false))"

let invalidUTF8: [UInt8] = [67, 97, 102, 195, 0]
invalidUTF8.withUnsafeBufferPointer { ptr in
    let s = String.decodeCString(ptr.baseAddress,
                                 as: UTF8.self,
                                 repairingInvalidCodeUnits: true)
    print(s)
}
// Prints "Optional((result: "Caf�", repairsMade: true))"
```

## See Also

### Converting a C String

- [init(bytes:encoding:)](<init(bytes_encoding_).md>) — Creates a new string equivalent to the given bytes interpreted in the specified encoding. Note: This API does not interpret embedded nulls as termination of the string. Use `String?(validatingCString:)` instead for null-terminated C strings.
- [init(bytesNoCopy:length:encoding:freeWhenDone:)](<init(bytesnocopy_length_encoding_freewhendone_).md>) — Creates a new string that contains the specified number of bytes from the given buffer, interpreted in the specified encoding, and optionally frees the buffer. _(deprecated)_
- [init(validatingCString:)](<init(validatingcstring_)-992vo.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given pointer.
- [init(validatingCString:)](<init(validatingcstring_)-98wra.md>) — Creates a new string by copying and validating the null-terminated UTF-8 data referenced by the given array.
- [init(cString:)](<init(cstring_)-2p84k.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:)](<init(cstring_)-6kr8s.md>) — Creates a new string by copying the null-terminated UTF-8 data referenced by the given pointer.
- [init(cString:encoding:)](<init(cstring_encoding_)-3h7bc.md>) — Produces a string by copying the null-terminated bytes in a given array, interpreted according to a given encoding.
- [init(cString:encoding:)](<init(cstring_encoding_)-3qgzd.md>) — Produces a string by copying the null-terminated bytes in a given C array, interpreted according to a given encoding.
- [init(decodingCString:as:)](<init(decodingcstring_as_)-8way7.md>) — Creates a new string by copying the null-terminated sequence of code units referenced by the given array.

---
title: 'data(using:allowLossyConversion:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/data(using:allowlossyconversion:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/data(using:allowlossyconversion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/data%28using%3Aallowlossyconversion%3A%29.json'
content_hash: 'sha256:6e56a115b8c28314'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# data(using:allowLossyConversion:)

<sub>Instance Method</sub>

Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func data(using encoding: UInt, allowLossyConversion lossy: Bool) -> Data?
```

## Parameters

- `encoding` — A string encoding. For possible values, see [NSStringEncoding](../nsstringencoding.md).

- `lossy` — If [true](../../swift/true.md), then allows characters to be removed or altered in conversion.

## Return Value

An `NSData` object containing a representation of the receiver encoded using `encoding`. Returns `nil` if `flag` is [false](../../swift/false.md) and the receiver can’t be converted without losing some information (such as accents or case).

## Discussion

If `flag` is [true](../../swift/true.md) and the receiver can’t be converted without losing some information, some characters may be removed or altered in conversion. For example, in converting a character from `NSUnicodeStringEncoding` to `NSASCIIStringEncoding`, the character ‘Á’ becomes ‘A’, losing the accent.

This method creates an external representation (with a byte order marker, if necessary, to indicate endianness) to ensure that the resulting `NSData` object can be written out to a file safely. The result of this method, when lossless conversion is made, is the default “plain text” format for encoding and is the recommended way to save or transmit a string object.

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [+ localizedNameOfStringEncoding:](<localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](description.md)
- [fastestEncoding](fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

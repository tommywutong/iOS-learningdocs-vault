---
title: 'stringEncoding(for:encodingOptions:convertedString:usedLossyConversion:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/stringencoding(for:encodingoptions:convertedstring:usedlossyconversion:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/stringencoding(for:encodingoptions:convertedstring:usedlossyconversion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/stringencoding%28for%3Aencodingoptions%3Aconvertedstring%3Ausedlossyconversion%3A%29.json'
content_hash: 'sha256:bccf0ddbbd843398'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# stringEncoding(for:encodingOptions:convertedString:usedLossyConversion:)

<sub>Type Method</sub>

Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func stringEncoding(for data: Data, encodingOptions opts: [StringEncodingDetectionOptionsKey : Any]? = nil, convertedString string: AutoreleasingUnsafeMutablePointer<NSString?>?, usedLossyConversion: UnsafeMutablePointer<ObjCBool>?) -> UInt
```

## Parameters

- `data` — An `NSData` object containing bytes in an encoding to be determined.

- `opts` — Options to use when attempting to determine the string encoding. See `String Encoding Detection Options` for a full list of supported options.

- `string` — If a string encoding could be determined, upon return contains an `NSString` object constructed from data using the determined string encoding.

- `usedLossyConversion` — If a string encoding could be determined, upon return contains a `BOOL` value corresponding to whether lossy conversion was used.

## Return Value

An `NSStringEncoding` value, or `0` if a string encoding could not be determined.

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ localizedNameOfStringEncoding:](<localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](description.md)
- [fastestEncoding](fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

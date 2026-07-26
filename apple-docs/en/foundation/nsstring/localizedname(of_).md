---
title: 'localizedName(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsstring/localizedname(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/localizedname(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/localizedname%28of%3A%29.json'
content_hash: 'sha256:7a677c4054b6f1e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# localizedName(of:)

<sub>Type Method</sub>

Returns a human-readable string giving the name of a given encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func localizedName(of encoding: UInt) -> String
```

## Parameters

- `encoding` — A string encoding. For possible values, see [NSStringEncoding](../nsstringencoding.md).

## Return Value

A human-readable string giving the name of `encoding` in the current locale.

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](description.md)
- [fastestEncoding](fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

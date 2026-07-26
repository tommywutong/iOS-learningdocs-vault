---
title: fastestEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/fastestencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/fastestencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/fastestencoding.json'
content_hash: 'sha256:a383f986aa76247d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# fastestEncoding

<sub>Instance Property</sub>

The fastest encoding to which the receiver may be converted without loss of information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fastestEncoding: UInt { get }
```

## Discussion

“Fastest” applies to retrieval of characters from the string. This encoding may not be space efficient.

## See Also

### Related Documentation

- [- getCharacters:range:](<getcharacters(__range_).md>) — Copies characters from a given range in the receiver into a given buffer.

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [+ localizedNameOfStringEncoding:](<localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](description.md)
- [smallestEncoding](smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

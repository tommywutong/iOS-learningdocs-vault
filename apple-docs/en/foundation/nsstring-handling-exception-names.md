---
title: NSString Handling Exception Names
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring-handling-exception-names
source_url: 'https://developer.apple.com/documentation/foundation/nsstring-handling-exception-names'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring-handling-exception-names.json'
content_hash: 'sha256:cc8069a45b3df9db'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSString](nsstring.md)

# NSString Handling Exception Names

<sub>API Collection</sub>

These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

## Topics

### Constants

- [NSCharacterConversionException](nsexceptionname/characterconversionexception.md) — `NSString` raises an `NSCharacterConversionException` if a string cannot be represented in a file-system or string encoding.
- [NSParseErrorException](nsexceptionname/parseerrorexception.md) — `NSString` raises an `NSParseErrorException` if a string cannot be parsed as a property list.

## See Also

### Working with Encodings

- [availableStringEncodings](nsstring/availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
- [defaultCStringEncoding](nsstring/defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<nsstring/stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [+ localizedNameOfStringEncoding:](<nsstring/localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<nsstring/canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<nsstring/data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<nsstring/data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](nsstring/description.md)
- [fastestEncoding](nsstring/fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](nsstring/smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](stringencodingdetectionoptionskey.md)

---
title: availableStringEncodings
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/availablestringencodings
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/availablestringencodings'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/availablestringencodings.json'
content_hash: 'sha256:69604482badda51c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# availableStringEncodings

<sub>Type Property</sub>

Returns a zero-terminated list of the encodings string objects support in the application’s environment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var availableStringEncodings: UnsafePointer<UInt> { get }
```

## Return Value

A zero-terminated list of the encodings string objects support in the application’s environment.

## Discussion

Among the more commonly used encodings are:

- [NSASCIIStringEncoding](../nsasciistringencoding.md)
- [NSUnicodeStringEncoding](../nsunicodestringencoding.md)
- [NSISOLatin1StringEncoding](../nsisolatin1stringencoding.md)
- [NSISOLatin2StringEncoding](../nsisolatin2stringencoding.md)
- [NSSymbolStringEncoding](../nssymbolstringencoding.md)

See the [NSStringEncoding](../nsstringencoding.md) type for a larger list and descriptions of many supported encodings. In addition to those encodings listed here, you can also use the encodings defined for CFString in Core Foundation; you just need to call the [CFStringConvertEncodingToNSStringEncoding(_:)](<../../corefoundation/cfstringconvertencodingtonsstringencoding(__).md>) function to convert them to a usable format.

## See Also

### Working with Encodings

- [defaultCStringEncoding](defaultcstringencoding.md) — Returns the C-string encoding assumed for any method accepting a C string as an argument.
- [+ stringEncodingForData:encodingOptions:convertedString:usedLossyConversion:](<stringencoding(for_encodingoptions_convertedstring_usedlossyconversion_).md>) — Returns the string encoding for the given data as detected by attempting to create a string according to the specified encoding options.
- [+ localizedNameOfStringEncoding:](<localizedname(of_).md>) — Returns a human-readable string giving the name of a given encoding.
- [- canBeConvertedToEncoding:](<canbeconverted(to_).md>) — Returns a Boolean value that indicates whether the receiver can be converted to a given encoding without loss of information.
- [- dataUsingEncoding:](<data(using_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [- dataUsingEncoding:allowLossyConversion:](<data(using_allowlossyconversion_).md>) — Returns an `NSData` object containing a representation of the receiver encoded using a given encoding.
- [description](description.md)
- [fastestEncoding](fastestencoding.md) — The fastest encoding to which the receiver may be converted without loss of information.
- [smallestEncoding](smallestencoding.md) — The smallest encoding to which the receiver can be converted without loss of information.
- [StringEncodingDetectionOptionsKey](../stringencodingdetectionoptionskey.md)
- [NSString Handling Exception Names](../nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

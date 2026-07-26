---
title: defaultCStringEncoding
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstring/defaultcstringencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsstring/defaultcstringencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstring/defaultcstringencoding.json'
content_hash: 'sha256:35e64a55360e2490'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSString](../nsstring.md)

# defaultCStringEncoding

<sub>Type Property</sub>

Returns the C-string encoding assumed for any method accepting a C string as an argument.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var defaultCStringEncoding: UInt { get }
```

## Return Value

The C-string encoding assumed for any method accepting a C string as an argument.

## Discussion

This method returns a user-dependent encoding who value is derived from user’s default language and potentially other factors. You might sometimes need to use this encoding when interpreting user documents with unknown encodings, in the absence of other hints, but in general this encoding should be used rarely, if at all. Note that some potential values might result in unexpected encoding conversions of even fairly straightforward `NSString` content—for example, punctuation characters with a bidirectional encoding.

Methods that accept a C string as an argument use `...CString...` in the keywords for such arguments: for example, [+ stringWithCString:](<string(withcstring_).md>)—note, though, that these are deprecated. The default C-string encoding is determined from system information and can’t be changed programmatically for an individual process. See [NSStringEncoding](../nsstringencoding.md) for a full list of supported encodings.

## See Also

### Working with Encodings

- [availableStringEncodings](availablestringencodings.md) — Returns a zero-terminated list of the encodings string objects support in the application’s environment.
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

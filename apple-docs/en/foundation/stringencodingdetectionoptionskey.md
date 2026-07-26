---
title: StringEncodingDetectionOptionsKey
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/stringencodingdetectionoptionskey
source_url: 'https://developer.apple.com/documentation/foundation/stringencodingdetectionoptionskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/stringencodingdetectionoptionskey.json'
content_hash: 'sha256:3bc10f194d38c2e6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# StringEncodingDetectionOptionsKey

<sub>Structure</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StringEncodingDetectionOptionsKey
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Type Properties

- [NSStringEncodingDetectionAllowLossyKey](stringencodingdetectionoptionskey/allowlossykey.md)
- [NSStringEncodingDetectionDisallowedEncodingsKey](stringencodingdetectionoptionskey/disallowedencodingskey.md)
- [NSStringEncodingDetectionFromWindowsKey](stringencodingdetectionoptionskey/fromwindowskey.md)
- [NSStringEncodingDetectionLikelyLanguageKey](stringencodingdetectionoptionskey/likelylanguagekey.md)
- [NSStringEncodingDetectionLossySubstitutionKey](stringencodingdetectionoptionskey/lossysubstitutionkey.md)
- [NSStringEncodingDetectionSuggestedEncodingsKey](stringencodingdetectionoptionskey/suggestedencodingskey.md)
- [NSStringEncodingDetectionUseOnlySuggestedEncodingsKey](stringencodingdetectionoptionskey/useonlysuggestedencodingskey.md)

### Initializers

- [init(rawValue:)](<stringencodingdetectionoptionskey/init(rawvalue_).md>)

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
- [NSString Handling Exception Names](nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

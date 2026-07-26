---
title: NSStringEncoding
framework: Foundation
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsstringencoding
source_url: 'https://developer.apple.com/documentation/foundation/nsstringencoding'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsstringencoding.json'
content_hash: 'sha256:9ac823f0258696a7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSStringEncoding

<sub>Type Alias</sub>

The following constants are provided by `NSString` as possible string encodings.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
typedef NSUInteger NSStringEncoding;
```

## Discussion

These values represent the various character encodings supported by the `NSString` classes. This is an incomplete list. Additional encodings are defined in [String Programming Guide for Core Foundation](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFStrings/introCFStrings.html#//apple_ref/doc/uid/10000131i) (see `CFStringEncodingExt.h`); these encodings can be used with `NSString` by first passing the Core Foundation encoding to the [CFStringConvertEncodingToNSStringEncoding(_:)](<../corefoundation/cfstringconvertencodingtonsstringencoding(__).md>) function.

## Topics

### Constants

- [NSASCIIStringEncoding](nsasciistringencoding.md) — Strict 7-bit ASCII encoding within 8-bit chars; ASCII values 0…127 only.
- [NSNEXTSTEPStringEncoding](nsnextstepstringencoding.md) — 8-bit ASCII encoding with NEXTSTEP extensions.
- [NSJapaneseEUCStringEncoding](nsjapaneseeucstringencoding.md) — 8-bit EUC encoding for Japanese text.
- [NSUTF8StringEncoding](nsutf8stringencoding.md) — An 8-bit representation of Unicode characters, suitable for transmission or storage by ASCII-based systems.
- [NSISOLatin1StringEncoding](nsisolatin1stringencoding.md) — 8-bit ISO Latin 1 encoding.
- [NSSymbolStringEncoding](nssymbolstringencoding.md) — 8-bit Adobe Symbol encoding vector.
- [NSNonLossyASCIIStringEncoding](nsnonlossyasciistringencoding.md) — 7-bit verbose ASCII to represent all Unicode characters.
- [NSShiftJISStringEncoding](nsshiftjisstringencoding.md) — 8-bit Shift-JIS encoding for Japanese text.
- [NSISOLatin2StringEncoding](nsisolatin2stringencoding.md) — 8-bit ISO Latin 2 encoding.
- [NSUnicodeStringEncoding](nsunicodestringencoding.md) — The canonical Unicode encoding for string objects.
- [NSWindowsCP1251StringEncoding](nswindowscp1251stringencoding.md) — Microsoft Windows codepage 1251, encoding Cyrillic characters; equivalent to AdobeStandardCyrillic font encoding.
- [NSWindowsCP1252StringEncoding](nswindowscp1252stringencoding.md) — Microsoft Windows codepage 1252; equivalent to WinLatin1.
- [NSWindowsCP1253StringEncoding](nswindowscp1253stringencoding.md) — Microsoft Windows codepage 1253, encoding Greek characters.
- [NSWindowsCP1254StringEncoding](nswindowscp1254stringencoding.md) — Microsoft Windows codepage 1254, encoding Turkish characters.
- [NSWindowsCP1250StringEncoding](nswindowscp1250stringencoding.md) — Microsoft Windows codepage 1250; equivalent to WinLatin2.
- [NSISO2022JPStringEncoding](nsiso2022jpstringencoding.md) — ISO 2022 Japanese encoding for email.
- [NSMacOSRomanStringEncoding](nsmacosromanstringencoding.md) — Classic Macintosh Roman encoding.
- [NSUTF16StringEncoding](nsutf16stringencoding.md)
- [NSUTF16BigEndianStringEncoding](nsutf16bigendianstringencoding.md) — `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [NSUTF16LittleEndianStringEncoding](nsutf16littleendianstringencoding.md) — `NSUTF16StringEncoding` encoding with explicit endianness specified.
- [NSUTF32StringEncoding](nsutf32stringencoding.md) — 32-bit UTF encoding.
- [NSUTF32BigEndianStringEncoding](nsutf32bigendianstringencoding.md) — `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [NSUTF32LittleEndianStringEncoding](nsutf32littleendianstringencoding.md) — `NSUTF32StringEncoding` encoding with explicit endianness specified.
- [NSProprietaryStringEncoding](nsproprietarystringencoding.md) — Installation-specific encoding. _(deprecated)_

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
- [NSString Handling Exception Names](nsstring-handling-exception-names.md) — These constants define the names of exceptions raised if `NSString` cannot represent a string in a given encoding, or parse a string as a property list.

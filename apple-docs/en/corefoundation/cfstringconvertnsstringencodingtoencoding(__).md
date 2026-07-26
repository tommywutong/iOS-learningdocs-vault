---
title: 'CFStringConvertNSStringEncodingToEncoding(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringconvertnsstringencodingtoencoding(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringconvertnsstringencodingtoencoding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringconvertnsstringencodingtoencoding%28_%3A%29.json'
content_hash: 'sha256:e7669eda9f71e278'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringConvertNSStringEncodingToEncoding(_:)

<sub>Function</sub>

Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringConvertNSStringEncodingToEncoding(_ encoding: UInt) -> CFStringEncoding
```

## Parameters

- `encoding` — The Cocoa string encoding (of type [NSStringEncoding](../foundation/nsstringencoding.md)) to use.

## Return Value

The Core Foundation string encoding that is closest to the Cocoa string encoding `encoding`. Returns the [kCFStringEncodingInvalidId](kcfstringencodinginvalidid.md) constant if the mapping is not known.

## Discussion

The [CFStringConvertEncodingToNSStringEncoding](<cfstringconvertencodingtonsstringencoding(__).md>) function is complementary to this function.

## See Also

### Working With Encodings

- [CFStringConvertEncodingToIANACharSetName](<cfstringconvertencodingtoianacharsetname(__).md>) — Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [CFStringConvertEncodingToNSStringEncoding](<cfstringconvertencodingtonsstringencoding(__).md>) — Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertEncodingToWindowsCodepage](<cfstringconvertencodingtowindowscodepage(__).md>) — Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertIANACharSetNameToEncoding](<cfstringconvertianacharsetnametoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [CFStringConvertWindowsCodepageToEncoding](<cfstringconvertwindowscodepagetoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.
- [CFStringGetFastestEncoding](<cfstringgetfastestencoding(__).md>) — Returns for a CFString object the character encoding that requires the least conversion time.
- [CFStringGetListOfAvailableEncodings](<cfstringgetlistofavailableencodings().md>) — Returns a pointer to a list of string encodings supported by the current system.
- [CFStringGetMaximumSizeForEncoding](<cfstringgetmaximumsizeforencoding(____).md>) — Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [CFStringGetMostCompatibleMacStringEncoding](<cfstringgetmostcompatiblemacstringencoding(__).md>) — Returns the most compatible Mac OS script value for the given input encoding.
- [CFStringGetNameOfEncoding](<cfstringgetnameofencoding(__).md>) — Returns the canonical name of a specified string encoding.
- [CFStringGetSmallestEncoding](<cfstringgetsmallestencoding(__).md>) — Returns the smallest encoding on the current system for the character contents of a string.
- [CFStringGetSystemEncoding](<cfstringgetsystemencoding().md>) — Returns the default encoding used by the operating system when it creates strings.
- [CFStringIsEncodingAvailable](<cfstringisencodingavailable(__).md>) — Determines whether a given Core Foundation string encoding is available on the current system.

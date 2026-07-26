---
title: 'CFStringGetMostCompatibleMacStringEncoding(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetmostcompatiblemacstringencoding(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetmostcompatiblemacstringencoding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetmostcompatiblemacstringencoding%28_%3A%29.json'
content_hash: 'sha256:d2cd2f91d6780cd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetMostCompatibleMacStringEncoding(_:)

<sub>Function</sub>

Returns the most compatible Mac OS script value for the given input encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetMostCompatibleMacStringEncoding(_ encoding: CFStringEncoding) -> CFStringEncoding
```

## Parameters

- `encoding` — The encoding for which you wish to find a compatible Mac OS script value.

## Return Value

The most compatible Mac OS script value for `encoding`.

## See Also

### Working With Encodings

- [CFStringConvertEncodingToIANACharSetName](<cfstringconvertencodingtoianacharsetname(__).md>) — Returns the name of the IANA registry “charset” that is the closest mapping to a specified string encoding.
- [CFStringConvertEncodingToNSStringEncoding](<cfstringconvertencodingtonsstringencoding(__).md>) — Returns the Cocoa encoding constant that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertEncodingToWindowsCodepage](<cfstringconvertencodingtowindowscodepage(__).md>) — Returns the Windows codepage identifier that maps most closely to a given Core Foundation encoding constant.
- [CFStringConvertIANACharSetNameToEncoding](<cfstringconvertianacharsetnametoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given IANA registry “charset” name.
- [CFStringConvertNSStringEncodingToEncoding](<cfstringconvertnsstringencodingtoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given Cocoa encoding.
- [CFStringConvertWindowsCodepageToEncoding](<cfstringconvertwindowscodepagetoencoding(__).md>) — Returns the Core Foundation encoding constant that is the closest mapping to a given Windows codepage identifier.
- [CFStringGetFastestEncoding](<cfstringgetfastestencoding(__).md>) — Returns for a CFString object the character encoding that requires the least conversion time.
- [CFStringGetListOfAvailableEncodings](<cfstringgetlistofavailableencodings().md>) — Returns a pointer to a list of string encodings supported by the current system.
- [CFStringGetMaximumSizeForEncoding](<cfstringgetmaximumsizeforencoding(____).md>) — Returns the maximum number of bytes a string of a specified length (in Unicode characters) will take up if encoded in a specified encoding.
- [CFStringGetNameOfEncoding](<cfstringgetnameofencoding(__).md>) — Returns the canonical name of a specified string encoding.
- [CFStringGetSmallestEncoding](<cfstringgetsmallestencoding(__).md>) — Returns the smallest encoding on the current system for the character contents of a string.
- [CFStringGetSystemEncoding](<cfstringgetsystemencoding().md>) — Returns the default encoding used by the operating system when it creates strings.
- [CFStringIsEncodingAvailable](<cfstringisencodingavailable(__).md>) — Determines whether a given Core Foundation string encoding is available on the current system.

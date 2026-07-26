---
title: 'CFStringGetNameOfEncoding(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetnameofencoding(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetnameofencoding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetnameofencoding%28_%3A%29.json'
content_hash: 'sha256:54fe060e59860f62'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetNameOfEncoding(_:)

<sub>Function</sub>

Returns the canonical name of a specified string encoding.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetNameOfEncoding(_ encoding: CFStringEncoding) -> CFString!
```

## Parameters

- `encoding` — The string encoding to use.

## Return Value

Name of `encoding`; non-localized. Ownership follows the [The Get Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-SW1).

## Discussion

This function returns the “canonical” name of the string encoding because the return value has to be the same no matter what localization is chosen. In other words, it can’t change based on the International Preferences language panel setting. The canonical name is usually expressed in English.

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
- [CFStringGetMostCompatibleMacStringEncoding](<cfstringgetmostcompatiblemacstringencoding(__).md>) — Returns the most compatible Mac OS script value for the given input encoding.
- [CFStringGetSmallestEncoding](<cfstringgetsmallestencoding(__).md>) — Returns the smallest encoding on the current system for the character contents of a string.
- [CFStringGetSystemEncoding](<cfstringgetsystemencoding().md>) — Returns the default encoding used by the operating system when it creates strings.
- [CFStringIsEncodingAvailable](<cfstringisencodingavailable(__).md>) — Determines whether a given Core Foundation string encoding is available on the current system.

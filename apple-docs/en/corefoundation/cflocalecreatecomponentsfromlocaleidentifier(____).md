---
title: 'CFLocaleCreateComponentsFromLocaleIdentifier(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalecreatecomponentsfromlocaleidentifier(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecreatecomponentsfromlocaleidentifier(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecreatecomponentsfromlocaleidentifier%28_%3A_%3A%29.json'
content_hash: 'sha256:d97c5e4205fee7eb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCreateComponentsFromLocaleIdentifier(_:_:)

<sub>Function</sub>

Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCreateComponentsFromLocaleIdentifier(_ allocator: CFAllocator!, _ localeID: CFLocaleIdentifier!) -> CFDictionary!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or `kCFAllocatorDefault` to use the current default allocator.

- `localeID` — The locale ID to use when creating the locale dictionary.

## Return Value

A dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs. Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## Discussion

The dictionary keys are the constant CFString objects that correspond to the locale ID components; the values correspond to constants where available. For example: the string “en_US@calendar=japanese” yields a dictionary with three entries: `kCFLocaleLanguageCode``=en`, `kCFLocaleCountryCode``=US`, and `kCFLocaleCalendarIdentifier``=``kCFJapaneseCalendar`. See also [CFLocaleCreateLocaleIdentifierFromComponents](<cflocalecreatelocaleidentifierfromcomponents(____).md>).

## See Also

### Getting and Creating Locale Identifiers

- [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](<cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(______).md>) — Returns a canonical locale identifier from given language and region codes.
- [CFLocaleCreateCanonicalLanguageIdentifierFromString](<cflocalecreatecanonicallanguageidentifierfromstring(____).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [CFLocaleCreateCanonicalLocaleIdentifierFromString](<cflocalecreatecanonicallocaleidentifierfromstring(____).md>) — Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [CFLocaleCreateLocaleIdentifierFromComponents](<cflocalecreatelocaleidentifierfromcomponents(____).md>) — Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode](<cflocalecreatelocaleidentifierfromwindowslocalecode(____).md>) — Returns a locale identifier from a Windows locale code.
- [CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier](<cflocalegetwindowslocalecodefromlocaleidentifier(__).md>) — Returns a Windows locale code from the locale identifier.

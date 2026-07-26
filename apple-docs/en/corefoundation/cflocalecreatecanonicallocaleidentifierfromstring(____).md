---
title: 'CFLocaleCreateCanonicalLocaleIdentifierFromString(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cflocalecreatecanonicallocaleidentifierfromstring(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocalecreatecanonicallocaleidentifierfromstring(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocalecreatecanonicallocaleidentifierfromstring%28_%3A_%3A%29.json'
content_hash: 'sha256:5ff5035e5d9249f5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocaleCreateCanonicalLocaleIdentifierFromString(_:_:)

<sub>Function</sub>

Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFLocaleCreateCanonicalLocaleIdentifierFromString(_ allocator: CFAllocator!, _ localeIdentifier: CFString!) -> CFLocaleIdentifier!
```

## Parameters

- `allocator` — The allocator to use to allocate memory for the new object. Pass `NULL` or kCFAllocatorDefault to use the current default allocator.

- `localeIdentifier` — A string representation of an arbitrary locale identifier (for example, “English”).

## Return Value

A canonical locale identifier created by mapping the arbitrary locale identification string to the canonical identifier for the corresponding locale (for example, “en”). Returns `NULL` if there was a problem creating the object. Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### Getting and Creating Locale Identifiers

- [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](<cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(______).md>) — Returns a canonical locale identifier from given language and region codes.
- [CFLocaleCreateCanonicalLanguageIdentifierFromString](<cflocalecreatecanonicallanguageidentifierfromstring(____).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [CFLocaleCreateComponentsFromLocaleIdentifier](<cflocalecreatecomponentsfromlocaleidentifier(____).md>) — Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [CFLocaleCreateLocaleIdentifierFromComponents](<cflocalecreatelocaleidentifierfromcomponents(____).md>) — Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode](<cflocalecreatelocaleidentifierfromwindowslocalecode(____).md>) — Returns a locale identifier from a Windows locale code.
- [CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier](<cflocalegetwindowslocalecodefromlocaleidentifier(__).md>) — Returns a Windows locale code from the locale identifier.

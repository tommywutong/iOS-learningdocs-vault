---
title: CFLocale
framework: Core Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/corefoundation/cflocale
source_url: 'https://developer.apple.com/documentation/corefoundation/cflocale'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cflocale.json'
content_hash: 'sha256:da970f296bbc40d6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFLocale

<sub>Class</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class CFLocale
```

## Overview

Unicode operations such as collation and text boundary determination can be affected by the conventions of a particular language or region. CFLocale objects specify language-specific or region-specific information for locale-sensitive operations.

The CFLocale opaque type provides support for obtaining available locales, obtaining localized locale names, and converting among locale data formats. Locale identifiers in macOS follow the IETF’s [BCP 47](http://www.rfc-editor.org/rfc/bcp/bcp47.txt). CFLocale never uses Script Manager codes (except for the legacy support provided by [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](<cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(______).md>))—the Script Manager and all its concepts are deprecated.

For more information on locale identifiers, read [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i). It is also useful to read the ICU’s [User Guide for the Locale Class](http://icu-project.org/userguide/locale.html).

CFLocale is “toll-free bridged” with its Cocoa Foundation counterpart, [NSLocale](../foundation/nslocale.md). This means that the Core Foundation type is interchangeable in function or method calls with the bridged Foundation object. Therefore, in a method where you see an `NSLocale *` parameter, you can pass in a `CFLocaleRef`, and in a function where you see a `CFLocaleRef` parameter, you can pass in an `NSLocale` instance. See [Toll-Free Bridged Types](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFDesignConcepts/Articles/tollFreeBridgedTypes.html#//apple_ref/doc/uid/TP40010677) for more information on toll-free bridging.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a Locale

- [CFLocaleCopyCurrent](<cflocalecopycurrent().md>) — Returns a copy of the logical locale for the current user.
- [CFLocaleCreate](<cflocalecreate(____).md>) — Creates a locale for the given arbitrary locale identifier.
- [CFLocaleCreateCopy](<cflocalecreatecopy(____).md>) — Returns a copy of a locale.
- [CFLocaleGetSystem](<cflocalegetsystem().md>) — Returns the root, canonical locale.

### Getting System Locale Information

- [CFLocaleCopyAvailableLocaleIdentifiers](<cflocalecopyavailablelocaleidentifiers().md>) — Returns an array of CFString objects that represents all locales for which locale data is available.

### Getting ISO Information

- [CFLocaleCopyISOCountryCodes](<cflocalecopyisocountrycodes().md>) — Returns an array of CFString objects that represents all known legal ISO country codes.
- [CFLocaleCopyISOLanguageCodes](<cflocalecopyisolanguagecodes().md>) — Returns an array of CFString objects that represents all known legal ISO language codes.
- [CFLocaleCopyISOCurrencyCodes](<cflocalecopyisocurrencycodes().md>) — Returns an array of CFString objects that represents all known legal ISO currency codes.
- [CFLocaleCopyCommonISOCurrencyCodes](<cflocalecopycommonisocurrencycodes().md>) — Returns an array of strings that represents ISO currency codes for currencies in common use.

### Language Preferences

- [CFLocaleCopyPreferredLanguages](<cflocalecopypreferredlanguages().md>) — Returns the array of canonicalized language IDs that the user prefers.

### Getting Information About a Locale

- [CFLocaleCopyDisplayNameForPropertyValue](<cflocalecopydisplaynameforpropertyvalue(______).md>) — Returns the display name for the given value.
- [CFLocaleGetValue](<cflocalegetvalue(____).md>) — Returns the corresponding value for the given key of a locale’s key-value pair.
- [CFLocaleGetIdentifier](<cflocalegetidentifier(__).md>) — Returns the given locale’s identifier.

### Getting and Creating Locale Identifiers

- [CFLocaleCreateCanonicalLocaleIdentifierFromScriptManagerCodes](<cflocalecreatecanonicallocaleidentifierfromscriptmanagercodes(______).md>) — Returns a canonical locale identifier from given language and region codes.
- [CFLocaleCreateCanonicalLanguageIdentifierFromString](<cflocalecreatecanonicallanguageidentifierfromstring(____).md>) — Returns a canonical language identifier by mapping an arbitrary locale identification string to the canonical identifier
- [CFLocaleCreateCanonicalLocaleIdentifierFromString](<cflocalecreatecanonicallocaleidentifierfromstring(____).md>) — Returns a canonical locale identifier by mapping an arbitrary locale identification string to the canonical identifier.
- [CFLocaleCreateComponentsFromLocaleIdentifier](<cflocalecreatecomponentsfromlocaleidentifier(____).md>) — Returns a dictionary containing the result from parsing a locale ID consisting of language, script, country or region, variant, and keyword/value pairs.
- [CFLocaleCreateLocaleIdentifierFromComponents](<cflocalecreatelocaleidentifierfromcomponents(____).md>) — Returns a locale identifier consisting of language, script, country or region, variant, and keyword/value pairs derived from a dictionary containing the source information.
- [CFLocaleCreateLocaleIdentifierFromWindowsLocaleCode](<cflocalecreatelocaleidentifierfromwindowslocalecode(____).md>) — Returns a locale identifier from a Windows locale code.
- [CFLocaleGetWindowsLocaleCodeFromLocaleIdentifier](<cflocalegetwindowslocalecodefromlocaleidentifier(__).md>) — Returns a Windows locale code from the locale identifier.

### Getting Line and Character Direction for a Language

- [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) — Returns the character direction for the specified ISO language code.
- [CFLocaleGetLanguageLineDirection](<cflocalegetlanguagelinedirection(__).md>) — Returns the line direction for the specified ISO language code.

### Getting the CFLocale Type ID

- [CFLocaleGetTypeID](<cflocalegettypeid().md>) — Returns the type identifier for the CFLocale opaque type.

### Constants

- [CFLocaleLanguageDirection](cflocalelanguagedirection.md) — These constants describe the text direction for a language. They are returned by the functions [CFLocaleGetLanguageCharacterDirection](<cflocalegetlanguagecharacterdirection(__).md>) and [CFLocaleGetLanguageLineDirection](<cflocalegetlanguagelinedirection(__).md>).
- [Locale Property Keys](locale-property-keys.md) — Predefined locale keys used to get property values.
- [Locale Calendar Identifiers](locale-calendar-identifiers.md) — Predefined locale keys used to get calendar values—values for `kCFLocaleCalendarIdentifier`.
- [Locale Change Notification](locale-change-notification.md) — Identifier for notification sent if the current locale changes.

## See Also

### Related Documentation

- [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i)

### Opaque Types

- [CFAllocator](cfallocator.md)
- [CFArray](cfarray.md)
- [CFAttributedString](cfattributedstring.md)
- [CFBag](cfbag.md)
- [CFBinaryHeap](cfbinaryheap.md)
- [CFBitVector](cfbitvector.md)
- [CFBoolean](cfboolean.md)
- [CFBundle](cfbundle.md)
- [CFCalendar](cfcalendar.md)
- [CFCharacterSet](cfcharacterset.md)
- [CFData](cfdata.md)
- [CFDate](cfdate.md)
- [CFDateFormatter](cfdateformatter.md)
- [CFDictionary](cfdictionary.md)
- [CFError](cferror.md)

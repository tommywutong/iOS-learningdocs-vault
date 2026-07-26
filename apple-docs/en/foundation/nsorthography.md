---
title: NSOrthography
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorthography
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography.json'
content_hash: 'sha256:a444033ff38788c3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSOrthography

<sub>Class</sub>

A description of the linguistic content of natural language text, typically used for spelling and grammar checking.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSOrthography
```

## Overview

Use [NSOrthography](nsorthography.md) objects to describe the linguistic content of a piece of text, including which scripts the text contains, a dominant language (and possibly other languages) for each script, and a dominant script and language for the text as a whole.

Scripts are uniformly described by four-letter ISO 15924 script codes, such as `"Latn"`, `"Grek"`, and `"Cyrl"`. The supertags `"Jpan"` and `"Kore"` are typically used for Japanese and Korean text, and `"Hans"` and `"Hant"` are typically used for Chinese text. The tag `"Zyyy"` is used if a specific script cannot be identified. See [Internationalization and Localization Guide](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPInternational/Introduction/Introduction.html#//apple_ref/doc/uid/10000171i) for more information.

Languages are uniformly described by BCP-47 tags (preferably in canonical form). The tag `"und"` is used if a specific language cannot be determined.

You typically work with orthography objects returned from methods and properties for classes like [NSLinguisticTagger](nslinguistictagger.md) and [NSSpellChecker](../appkit/nsspellchecker.md).

### Subclassing Notes

Subclasses must override the [dominantScript](nsorthography/dominantscript.md) and [languageMap](nsorthography/languagemap.md) properties. These properties are set using [- initWithDominantScript:languageMap:](<nsorthography/init(dominantscript_languagemap_).md>) or [orthographyWithDominantScript:languageMap:](nsorthography/orthographywithdominantscript_languagemap_.md) in Objective-C.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](nscoding.md), [NSCopying](nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSSecureCoding](nssecurecoding.md)

## Topics

### Creating Orthography Objects

- [+ defaultOrthographyForLanguage:](<nsorthography/defaultorthography(forlanguage_).md>) — Creates and returns an orthography object with the default language map for the specified language.
- [- initWithDominantScript:languageMap:](<nsorthography/init(dominantscript_languagemap_).md>) — Creates an orthography object with the specified dominant script and language map.

### Determining Correspondences Between Languages and Scripts

- [languageMap](nsorthography/languagemap.md) — A dictionary that maps script tags to arrays of language tags.
- [dominantLanguage](nsorthography/dominantlanguage.md) — The first language in the list of languages for the dominant script.
- [dominantScript](nsorthography/dominantscript.md) — The dominant script for the text.
- [- dominantLanguageForScript:](<nsorthography/dominantlanguage(forscript_).md>) — Returns the dominant language for the specified script.
- [- languagesForScript:](<nsorthography/languages(forscript_).md>) — Returns the list of languages for the specified script.
- [allScripts](nsorthography/allscripts.md) — The scripts appearing as keys in the language map.
- [allLanguages](nsorthography/alllanguages.md) — The languages appearing in values of the language map.

### Initializers

- [- initWithCoder:](<nsorthography/init(coder_).md>)

## See Also

### Localization

- [Locale](locale.md) — Information about linguistic, cultural, and technological conventions for use in formatting data for presentation.
- [NSLocalizedString(_:tableName:bundle:value:comment:)](<nslocalizedstring(__tablename_bundle_value_comment_).md>) — Returns a localized string from a table that Xcode generates for you when exporting localizations.
- [LocalizedStringResource](localizedstringresource.md) — A reference to a localizable string, accessible from another process.
- [CustomLocalizedStringResourceConvertible](customlocalizedstringresourceconvertible.md) — A type that provides an out-of-process localizable description.
- [URLResource](urlresource.md) — A resource located at a particular file URL within a bundle.

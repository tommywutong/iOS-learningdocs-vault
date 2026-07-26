---
title: allLanguages
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorthography/alllanguages
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/alllanguages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/alllanguages.json'
content_hash: 'sha256:aa9ec6be5f58a2ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# allLanguages

<sub>Instance Property</sub>

The languages appearing in values of the language map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allLanguages: [String] { get }
```

## Discussion

The value of this property is an array of BCP-47 language tags, such as `"en"` or `"fr"`, that identify the languages.

## See Also

### Determining Correspondences Between Languages and Scripts

- [languageMap](languagemap.md) — A dictionary that maps script tags to arrays of language tags.
- [dominantLanguage](dominantlanguage.md) — The first language in the list of languages for the dominant script.
- [dominantScript](dominantscript.md) — The dominant script for the text.
- [- dominantLanguageForScript:](<dominantlanguage(forscript_).md>) — Returns the dominant language for the specified script.
- [- languagesForScript:](<languages(forscript_).md>) — Returns the list of languages for the specified script.
- [allScripts](allscripts.md) — The scripts appearing as keys in the language map.

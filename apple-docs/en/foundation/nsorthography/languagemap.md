---
title: languageMap
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsorthography/languagemap
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/languagemap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/languagemap.json'
content_hash: 'sha256:d65a901e8c59c88b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# languageMap

<sub>Instance Property</sub>

A dictionary that maps script tags to arrays of language tags.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var languageMap: [String : [String]] { get }
```

## Discussion

The dictionary’s keys are ISO 15924 script codes (such as `"Latn"` or `"Cyrl"`) and its values are arrays of BCP-47 language tags (such as `"en"`, `"fr"`, or `"de"`).

## See Also

### Determining Correspondences Between Languages and Scripts

- [dominantLanguage](dominantlanguage.md) — The first language in the list of languages for the dominant script.
- [dominantScript](dominantscript.md) — The dominant script for the text.
- [- dominantLanguageForScript:](<dominantlanguage(forscript_).md>) — Returns the dominant language for the specified script.
- [- languagesForScript:](<languages(forscript_).md>) — Returns the list of languages for the specified script.
- [allScripts](allscripts.md) — The scripts appearing as keys in the language map.
- [allLanguages](alllanguages.md) — The languages appearing in values of the language map.

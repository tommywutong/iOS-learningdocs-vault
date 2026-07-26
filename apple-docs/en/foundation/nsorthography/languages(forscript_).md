---
title: 'languages(forScript:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorthography/languages(forscript:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/languages(forscript:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/languages%28forscript%3A%29.json'
content_hash: 'sha256:4f61793b2a3ecf83'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# languages(forScript:)

<sub>Instance Method</sub>

Returns the list of languages for the specified script.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func languages(forScript script: String) -> [String]?
```

## Parameters

- `script` — The specified script.

## Discussion

The value of this property is an array of BCP-47 language tags, such as `"en"` or `"fr"`, that identify the languages.

## See Also

### Determining Correspondences Between Languages and Scripts

- [languageMap](languagemap.md) — A dictionary that maps script tags to arrays of language tags.
- [dominantLanguage](dominantlanguage.md) — The first language in the list of languages for the dominant script.
- [dominantScript](dominantscript.md) — The dominant script for the text.
- [- dominantLanguageForScript:](<dominantlanguage(forscript_).md>) — Returns the dominant language for the specified script.
- [allScripts](allscripts.md) — The scripts appearing as keys in the language map.
- [allLanguages](alllanguages.md) — The languages appearing in values of the language map.

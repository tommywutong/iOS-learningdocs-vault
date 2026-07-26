---
title: 'defaultOrthography(forLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 11.0+, visionOS 1.0+, watchOS 4.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorthography/defaultorthography(forlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/defaultorthography(forlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/defaultorthography%28forlanguage%3A%29.json'
content_hash: 'sha256:e060e5145b474439'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# defaultOrthography(forLanguage:)

<sub>Type Method</sub>

Creates and returns an orthography object with the default language map for the specified language.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func defaultOrthography(forLanguage language: String) -> Self
```

## Parameters

- `language` — A BCP-47 tag identifying the language.

## Discussion

This method automatically determines the script for the specified language. For example, the default orthography for the Hindi language has a language map with a single key, `"Deva"` (the ISO 15924 script code for Devanagari), that has a corresponding value of an array containing the element `"hi"` (the BCP-47 identifier for Hindi).

## See Also

### Creating Orthography Objects

- [- initWithDominantScript:languageMap:](<init(dominantscript_languagemap_).md>) — Creates an orthography object with the specified dominant script and language map.

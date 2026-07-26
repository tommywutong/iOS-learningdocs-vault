---
title: 'init(dominantScript:languageMap:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorthography/init(dominantscript:languagemap:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/init(dominantscript:languagemap:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/init%28dominantscript%3Alanguagemap%3A%29.json'
content_hash: 'sha256:d29a5c7525f30057'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# init(dominantScript:languageMap:)

<sub>Initializer</sub>

Creates an orthography object with the specified dominant script and language map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(dominantScript script: String, languageMap map: [String : [String]])
```

## Parameters

- `script` — The dominant script.

- `map` — A dictionary mapping ISO 15924 script codes to arrays of BCP-47 language tags.

## Return Value

An orthography object initialized with the specified script and language map.

## Discussion

You typically use the [+ defaultOrthographyForLanguage:](<defaultorthography(forlanguage_).md>) method to create orthography objects with automatic language mapping. Use this initializer only if you need to override the script associated with one or more languages.

## See Also

### Creating Orthography Objects

- [+ defaultOrthographyForLanguage:](<defaultorthography(forlanguage_).md>) — Creates and returns an orthography object with the default language map for the specified language.

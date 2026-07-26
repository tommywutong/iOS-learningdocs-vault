---
title: 'orthographyWithDominantScript:languageMap:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorthography/orthographywithdominantscript:languagemap:'
source_url: 'https://developer.apple.com/documentation/foundation/nsorthography/orthographywithdominantscript:languagemap:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorthography/orthographywithdominantscript%3Alanguagemap%3A.json'
content_hash: 'sha256:d3ab7498d81370f6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrthography](../nsorthography.md)

# orthographyWithDominantScript:languageMap:

<sub>Type Method</sub>

Creates and returns an orthography object with the specified dominant script and language map.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) orthographyWithDominantScript:(NSString *) script languageMap:(NSDictionary<NSString *,NSArray<NSString *> *> *) map;
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
- [- initWithDominantScript:languageMap:](<init(dominantscript_languagemap_).md>) — Creates an orthography object with the specified dominant script and language map.

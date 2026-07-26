---
title: dominantLanguage
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagger/dominantlanguage
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/dominantlanguage.json'
content_hash: 'sha256:14fc6423c6f629f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# dominantLanguage

<sub>Instance Property</sub>

Returns the dominant language of the string set for the linguistic tagger.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var dominantLanguage: String? { get }
```

## Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

## Discussion

If you want to know the dominant language of a string that you’re analyzing with a linguistic tagger (for example, identifying part of speech for each word), specify the [NSLinguisticTagSchemeLanguage](../nslinguistictagscheme/language.md) tag scheme in the initializer. After you set the [string](string.md) property of the linguistic tagger, the dominant language can be determined with the [dominantLanguage](dominantlanguage.md) property, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
let tagger = NSLinguisticTagger(tagSchemes: [.language], options: 0)
tagger.string = text
tagger.dominantLanguage // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## See Also

### Determining the Dominant Language and Orthography

- [+ dominantLanguageForString:](<dominantlanguage(for_).md>) — Returns the dominant language for the specified string. _(deprecated)_
- [- orthographyAtIndex:effectiveRange:](<orthography(at_effectiverange_).md>) — Returns the orthography at the index and also returns the effective range. _(deprecated)_
- [- setOrthography:range:](<setorthography(__range_).md>) — Sets the orthography for the specified range. _(deprecated)_

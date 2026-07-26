---
title: 'dominantLanguage(for:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/dominantlanguage(for:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/dominantlanguage(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/dominantlanguage%28for%3A%29.json'
content_hash: 'sha256:8376c68235f57c3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# dominantLanguage(for:)

<sub>Type Method</sub>

Returns the dominant language for the specified string.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class func dominantLanguage(for string: String) -> String?
```

## Parameters

- `string` — The string for which the dominant language is determined.

## Return Value

The BCP-47 tag identifying the dominant language of the string, or the tag “und” if a specific language cannot be determined.

## Discussion

The [+ dominantLanguageForString:](<dominantlanguage(for_).md>) method is a convenience method for creating a new linguistic tagger, setting the [string](string.md) property, and getting the [dominantLanguage](dominantlanguage.md) property. If you analyze the same string more than once, create a linguistic tagger object instead of calling the method, as shown in this example:

```swift
let text = "Die Kleinen haben friedlich zusammen gespielt."
NSLinguisticTagger.dominantLanguage(for: text) // "de"
```

In the example, the BCP-47 language tag “de” is returned as the dominant language, indicating that the text is in German.

## See Also

### Determining the Dominant Language and Orthography

- [dominantLanguage](dominantlanguage.md) — Returns the dominant language of the string set for the linguistic tagger. _(deprecated)_
- [- orthographyAtIndex:effectiveRange:](<orthography(at_effectiverange_).md>) — Returns the orthography at the index and also returns the effective range. _(deprecated)_
- [- setOrthography:range:](<setorthography(__range_).md>) — Sets the orthography for the specified range. _(deprecated)_

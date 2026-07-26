---
title: 'setOrthography(_:range:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/setorthography(_:range:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/setorthography(_:range:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/setorthography%28_%3Arange%3A%29.json'
content_hash: 'sha256:0159a6267c249351'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# setOrthography(_:range:)

<sub>Instance Method</sub>

Sets the orthography for the specified range.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func setOrthography(_ orthography: NSOrthography?, range: NSRange)
```

## Parameters

- `orthography` — The orthography.

- `range` — The range.

## Discussion

If the orthography of the linguistic tagger is not set, it will determine it automatically from the contents of the text.  You should call this method only if you  know the orthography of the text by some other means.

## See Also

### Determining the Dominant Language and Orthography

- [+ dominantLanguageForString:](<dominantlanguage(for_).md>) — Returns the dominant language for the specified string. _(deprecated)_
- [dominantLanguage](dominantlanguage.md) — Returns the dominant language of the string set for the linguistic tagger. _(deprecated)_
- [- orthographyAtIndex:effectiveRange:](<orthography(at_effectiverange_).md>) — Returns the orthography at the index and also returns the effective range. _(deprecated)_

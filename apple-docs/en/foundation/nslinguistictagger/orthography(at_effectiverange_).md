---
title: 'orthography(at:effectiveRange:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/orthography(at:effectiverange:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/orthography(at:effectiverange:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/orthography%28at%3Aeffectiverange%3A%29.json'
content_hash: 'sha256:be0c7d069b3680ce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# orthography(at:effectiveRange:)

<sub>Instance Method</sub>

Returns the orthography at the index and also returns the effective range.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func orthography(at charIndex: Int, effectiveRange: NSRangePointer?) -> NSOrthography?
```

## Parameters

- `charIndex` — The character index to begin examination.

- `effectiveRange` — An NSRangePointer that, upon completion, contains the range of the orthography containing `charIndex`.

## Return Value

The orthography for the location.

## See Also

### Determining the Dominant Language and Orthography

- [+ dominantLanguageForString:](<dominantlanguage(for_).md>) — Returns the dominant language for the specified string. _(deprecated)_
- [dominantLanguage](dominantlanguage.md) — Returns the dominant language of the string set for the linguistic tagger. _(deprecated)_
- [- setOrthography:range:](<setorthography(__range_).md>) — Sets the orthography for the specified range. _(deprecated)_

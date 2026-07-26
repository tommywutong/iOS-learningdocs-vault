---
title: 'init(tagSchemes:options:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/init(tagschemes:options:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/init(tagschemes:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/init%28tagschemes%3Aoptions%3A%29.json'
content_hash: 'sha256:6497dcbbf02e1fe5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# init(tagSchemes:options:)

<sub>Initializer</sub>

Creates a linguistic tagger instance using the specified tag schemes and options.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(tagSchemes: [NSLinguisticTagScheme], options opts: Int)
```

## Parameters

- `tagSchemes` — An array of tag schemes to be used. See [NSLinguisticTagScheme](../nslinguistictagscheme.md) for the possible values.

- `opts` — Reserved for future use. Specify `0` for this parameter.

## Return Value

An initialized linguistic tagger.

## Discussion

Pass any tag schemes to `tagSchemes` that you intend to use with the methods described in Enumerating Linguistic Tags and Getting Linguistic Tags.

> [!tip] Tip
> Avoid specifying tag schemes that you won’t use to ensure optimal performance.

## See Also

### Related Documentation

- [NSLinguisticTagScheme](../nslinguistictagscheme.md) — Constants for the tag schemes specified when initializing a linguistic tagger.

### First Steps

- [Tokenizing Natural Language Text](../tokenizing-natural-language-text.md) — Enumerate the words in a string.
- [string](string.md) — The string being analyzed by the linguistic tagger. _(deprecated)_

---
title: 'enumerateTags(in:unit:scheme:options:using:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 4.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/foundation/nslinguistictagger/enumeratetags(in:unit:scheme:options:using:)'
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/enumeratetags(in:unit:scheme:options:using:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/enumeratetags%28in%3Aunit%3Ascheme%3Aoptions%3Ausing%3A%29.json'
content_hash: 'sha256:d76132e37f545fa9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# enumerateTags(in:unit:scheme:options:using:)

<sub>Instance Method</sub>

Enumerates over a given range of the string for a particular unit and calls the specified block for each tag.

> [!warning] Deprecated
> All NSLinguisticTagger API should be replaced with NaturalLanguage.framework API

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func enumerateTags(in range: NSRange, unit: NSLinguisticTaggerUnit, scheme: NSLinguisticTagScheme, options: NSLinguisticTagger.Options = [], using block: (NSLinguisticTag?, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)
```

## Parameters

- `range` — The range to analyze.

- `unit` — The linguistic unit. For possible values, see [NSLinguisticTaggerUnit](../nslinguistictaggerunit.md).

- `scheme` — The tag scheme. For possible values, see [NSLinguisticTagScheme](../nslinguistictagscheme.md).

- `options` — The linguistic tagger options to use. See [Options](options.md) for possible values.

- `block` — The block to apply to ranges of the string. The block takes the following arguments: - **tag** — The located linguistic tag. - **tokenRange** — The range of the linguistic tag. - **stop** — A reference to a Boolean value. The block can set the value to [true](../../swift/true.md) to stop further processing of the set. The `stop` argument is an out-only argument. You should only ever set this Boolean to [true](../../swift/true.md) within the block.

## Discussion

This method’s block is called for all tokens intersecting a given range, supplying tags and ranges. The tagger segments the string into sentences and tokens as necessary, and return those ranges along with a tag for any scheme in its array of tag schemes. For example, if the tag scheme is [NSLinguisticTagSchemeLexicalClass](../nslinguistictagscheme/lexicalclass.md), the tags specify the part of speech (for word tokens) or the type of whitespace or punctuation (for whitespace or punctuation tokens).  If the tag scheme is [NSLinguisticTagSchemeLemma](../nslinguistictagscheme/lemma.md), the tags specify the stem form of the word (if known) for each word token.

> [!important] Important
> This method enumerates over the ranges of all tokens that intersect the specified range.

## See Also

### Enumerating Linguistic Tags

- [Identifying Parts of Speech](../identifying-parts-of-speech.md) — Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](../identifying-people-places-and-organizations.md) — Use a linguistic tagger to perform named entity recognition on a string.
- [- enumerateTagsInRange:scheme:options:usingBlock:](<enumeratetags(in_scheme_options_using_).md>) — Enumerates over a given range of the string and calls the specified block for each tag. _(deprecated)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — Enumerates over a given string and calls the specified block for each tag. _(deprecated)_
- [Options](options.md) — Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

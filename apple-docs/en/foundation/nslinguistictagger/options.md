---
title: NSLinguisticTagger.Options
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslinguistictagger/options
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger/options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger/options.json'
content_hash: 'sha256:84fd2097a97763db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSLinguisticTagger](../nslinguistictagger.md)

# NSLinguisticTagger.Options

<sub>Structure</sub>

Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Options
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Constants

- [NSLinguisticTaggerOmitWords](options/omitwords.md) — Omit tokens of type [NSLinguisticTagWord](../nslinguistictag/word.md) (items considered to be words).
- [NSLinguisticTaggerOmitPunctuation](options/omitpunctuation.md) — Omit tokens of type [NSLinguisticTagPunctuation](../nslinguistictag/punctuation.md) (all punctuation).
- [NSLinguisticTaggerOmitWhitespace](options/omitwhitespace.md) — Omit tokens of type [NSLinguisticTagWhitespace](../nslinguistictag/whitespace.md) (whitespace of all sorts).
- [NSLinguisticTaggerOmitOther](options/omitother.md) — Omit tokens of type [NSLinguisticTagOther](../nslinguistictag/other.md) (non-linguistic items, such as symbols).
- [NSLinguisticTaggerJoinNames](options/joinnames.md) — Typically, multiple-word names will be returned as multiple tokens, following the standard tokenization practice of the tagger.  If this option is set, then multiple-word names will be joined together and returned as a single token.

### Initializers

- [init(rawValue:)](<options/init(rawvalue_).md>)

## See Also

### Enumerating Linguistic Tags

- [Identifying Parts of Speech](../identifying-parts-of-speech.md) — Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](../identifying-people-places-and-organizations.md) — Use a linguistic tagger to perform named entity recognition on a string.
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<enumeratetags(in_unit_scheme_options_using_).md>) — Enumerates over a given range of the string for a particular unit and calls the specified block for each tag. _(deprecated)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<enumeratetags(in_scheme_options_using_).md>) — Enumerates over a given range of the string and calls the specified block for each tag. _(deprecated)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — Enumerates over a given string and calls the specified block for each tag. _(deprecated)_

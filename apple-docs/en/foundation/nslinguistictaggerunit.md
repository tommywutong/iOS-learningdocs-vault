---
title: NSLinguisticTaggerUnit
framework: Foundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslinguistictaggerunit
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictaggerunit'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictaggerunit.json'
content_hash: 'sha256:08e5cb2b5c04d551'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLinguisticTaggerUnit

<sub>Enumeration</sub>

Constants representing linguistic units.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NSLinguisticTaggerUnit
```

## Overview

You use these constants with the [+ availableTagSchemesForUnit:language:](<nslinguistictagger/availabletagschemes(for_language_).md>) method as well as the [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<nslinguistictagger/tag(for_at_unit_scheme_orthography_tokenrange_).md>),  [- tagsInRange:unit:scheme:options:tokenRanges:](<nslinguistictagger/tags(in_unit_scheme_options_tokenranges_).md>), and [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) methods.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSLinguisticTaggerUnitDocument](nslinguistictaggerunit/document.md) — The document in its entirety.
- [NSLinguisticTaggerUnitParagraph](nslinguistictaggerunit/paragraph.md) — An individual paragraph.
- [NSLinguisticTaggerUnitSentence](nslinguistictaggerunit/sentence.md) — An individual sentence.
- [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) — An individual word.

### Initializers

- [init(rawValue:)](<nslinguistictaggerunit/init(rawvalue_).md>)

## See Also

### Supporting Types

- [NSLinguisticTagScheme](nslinguistictagscheme.md) — Constants for the tag schemes specified when initializing a linguistic tagger.
- [NSLinguisticTag](nslinguistictag.md) — A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

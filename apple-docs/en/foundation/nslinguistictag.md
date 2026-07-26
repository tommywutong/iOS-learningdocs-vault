---
title: NSLinguisticTag
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nslinguistictag
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictag'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictag.json'
content_hash: 'sha256:6e1798a2e636648c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLinguisticTag

<sub>Structure</sub>

A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NSLinguisticTag
```

## Overview

When you create a linguistic tagger, you specify one or more [NSLinguisticTagScheme](nslinguistictagscheme.md) constants that correspond to the kind of information you want to know about a selection of natural language text.  When working with linguistic tags using the methods described in Getting Linguistic Tags and Enumerating Linguistic Tags, the returned value depends on the specified scheme. The [NSLinguisticTag](nslinguistictag.md) type represents the constant values that can be returned for certain [NSLinguisticTagScheme](nslinguistictagscheme.md) values.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Token Types

- [NSLinguisticTagWord](nslinguistictag/word.md) — The token indicates a word. _(deprecated)_
- [NSLinguisticTagPunctuation](nslinguistictag/punctuation.md) — The token indicates punctuation. _(deprecated)_
- [NSLinguisticTagWhitespace](nslinguistictag/whitespace.md) — The token indicates white space of any sort. _(deprecated)_
- [NSLinguisticTagOther](nslinguistictag/other.md) — The token indicates a non-linguistic item, such as a symbol. _(deprecated)_

### Lexical Classes

- [NSLinguisticTagNoun](nslinguistictag/noun.md) — The token is a noun. _(deprecated)_
- [NSLinguisticTagVerb](nslinguistictag/verb.md) — This token is a verb. _(deprecated)_
- [NSLinguisticTagAdjective](nslinguistictag/adjective.md) — This token is an adjective _(deprecated)_
- [NSLinguisticTagAdverb](nslinguistictag/adverb.md) — This token is an adverb. _(deprecated)_
- [NSLinguisticTagPronoun](nslinguistictag/pronoun.md) — This token is a pronoun. _(deprecated)_
- [NSLinguisticTagDeterminer](nslinguistictag/determiner.md) — This token is a determiner. _(deprecated)_
- [NSLinguisticTagParticle](nslinguistictag/particle.md) — This token is a particle. _(deprecated)_
- [NSLinguisticTagPreposition](nslinguistictag/preposition.md) — This token is a preposition. _(deprecated)_
- [NSLinguisticTagNumber](nslinguistictag/number.md) — This token is a number. _(deprecated)_
- [NSLinguisticTagConjunction](nslinguistictag/conjunction.md) — This token is a conjunction. _(deprecated)_
- [NSLinguisticTagInterjection](nslinguistictag/interjection.md) — This token is an interjection. _(deprecated)_
- [NSLinguisticTagClassifier](nslinguistictag/classifier.md) — This token is a classifier. _(deprecated)_
- [NSLinguisticTagIdiom](nslinguistictag/idiom.md) — This token is an idiom. _(deprecated)_
- [NSLinguisticTagOtherWord](nslinguistictag/otherword.md) — This token is a word other than a kind described by other lexical classes (noun, verb, adjective, adverb, pronoun, determiner, particle, preposition, number, conjunction, interjection, classifier, and idiom). _(deprecated)_
- [NSLinguisticTagSentenceTerminator](nslinguistictag/sentenceterminator.md) — This token is a sentence terminator. _(deprecated)_
- [NSLinguisticTagOpenQuote](nslinguistictag/openquote.md) — This token is an open quote. _(deprecated)_
- [NSLinguisticTagCloseQuote](nslinguistictag/closequote.md) — This token is a close quote. _(deprecated)_
- [NSLinguisticTagOpenParenthesis](nslinguistictag/openparenthesis.md) — This token is an open parenthesis. _(deprecated)_
- [NSLinguisticTagCloseParenthesis](nslinguistictag/closeparenthesis.md) — This token is a close parenthesis. _(deprecated)_
- [NSLinguisticTagWordJoiner](nslinguistictag/wordjoiner.md) — This token is a word joiner. _(deprecated)_
- [NSLinguisticTagDash](nslinguistictag/dash.md) — This token is a dash. _(deprecated)_
- [NSLinguisticTagOtherPunctuation](nslinguistictag/otherpunctuation.md) — This token is punctuation other than a kind described by other lexical classes (sentence terminator, open or close quote, open or close parenthesis, word joiner, and dash). _(deprecated)_
- [NSLinguisticTagParagraphBreak](nslinguistictag/paragraphbreak.md) — This token is a paragraph break. _(deprecated)_
- [NSLinguisticTagOtherWhitespace](nslinguistictag/otherwhitespace.md) — This token is whitespace other than a kind described by other lexical classes (paragraph break). _(deprecated)_

### Name Types

- [NSLinguisticTagPersonalName](nslinguistictag/personalname.md) — This token is a personal name. _(deprecated)_
- [NSLinguisticTagOrganizationName](nslinguistictag/organizationname.md) — This token is an organization name. _(deprecated)_
- [NSLinguisticTagPlaceName](nslinguistictag/placename.md) — This token is a place name. _(deprecated)_

### Initializers

- [init(_:)](<nslinguistictag/init(__).md>)
- [init(rawValue:)](<nslinguistictag/init(rawvalue_).md>)

## See Also

### Supporting Types

- [NSLinguisticTagScheme](nslinguistictagscheme.md) — Constants for the tag schemes specified when initializing a linguistic tagger.
- [NSLinguisticTaggerUnit](nslinguistictaggerunit.md) — Constants representing linguistic units.

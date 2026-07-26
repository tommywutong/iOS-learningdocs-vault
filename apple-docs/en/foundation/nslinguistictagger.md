---
title: NSLinguisticTagger
framework: Foundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 5.0+（27.0 起废弃）, iPadOS 5.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, macOS 10.7+（27.0 起废弃）, tvOS 9.0+（27.0 起废弃）, visionOS 1.0+（27.0 起废弃）, watchOS 2.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/foundation/nslinguistictagger
source_url: 'https://developer.apple.com/documentation/foundation/nslinguistictagger'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nslinguistictagger.json'
content_hash: 'sha256:3edef49b192d8297'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSLinguisticTagger

<sub>Class</sub>

Analyze natural language text to tag part of speech and lexical class, identify names, perform lemmatization, and determine the language and script.

> [!warning] Deprecated
> Use the [Natural Language](../naturallanguage.md) framework instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSLinguisticTagger
```

## Overview

[NSLinguisticTagger](nslinguistictagger.md) provides a uniform interface to a variety of natural language processing functionality with support for many different languages and scripts. You can use this class to segment natural language text into paragraphs, sentences, or words, and tag information about those segments, such as part of speech, lexical class, lemma, script, and language.

When you create a linguistic tagger, you specify what kind of information you’re interested in by passing one or more [NSLinguisticTagScheme](nslinguistictagscheme.md) values. Set the [string](nslinguistictagger/string.md) property to the natural language text you want to analyze, and the linguistic tagger processes it according to the specified tag schemes. You can then enumerate over the tags in a specified range, using the methods described in Enumerating Linguistic Tags, to get the information requested for a given scheme and unit.

### Thread Safety

A single instance of [NSLinguisticTagger](nslinguistictagger.md) should not be used simultaneously from multiple threads.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### First Steps

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md) — Enumerate the words in a string.
- [- initWithTagSchemes:options:](<nslinguistictagger/init(tagschemes_options_).md>) — Creates a linguistic tagger instance using the specified tag schemes and options. _(deprecated)_
- [string](nslinguistictagger/string.md) — The string being analyzed by the linguistic tagger. _(deprecated)_

### Getting the Tag Schemes

- [+ availableTagSchemesForUnit:language:](<nslinguistictagger/availabletagschemes(for_language_).md>) — Returns the tag schemes available for a particular unit and language on the current device. _(deprecated)_
- [+ availableTagSchemesForLanguage:](<nslinguistictagger/availabletagschemes(forlanguage_).md>) — Returns the tag schemes available for a particular language on the current device. _(deprecated)_
- [tagSchemes](nslinguistictagger/tagschemes.md) — Returns the tag schemes configured for this linguistic tagger. For possible values, see [NSLinguisticTagScheme](nslinguistictagscheme.md). _(deprecated)_

### Determining the Dominant Language and Orthography

- [+ dominantLanguageForString:](<nslinguistictagger/dominantlanguage(for_).md>) — Returns the dominant language for the specified string. _(deprecated)_
- [dominantLanguage](nslinguistictagger/dominantlanguage.md) — Returns the dominant language of the string set for the linguistic tagger. _(deprecated)_
- [- orthographyAtIndex:effectiveRange:](<nslinguistictagger/orthography(at_effectiverange_).md>) — Returns the orthography at the index and also returns the effective range. _(deprecated)_
- [- setOrthography:range:](<nslinguistictagger/setorthography(__range_).md>) — Sets the orthography for the specified range. _(deprecated)_

### Enumerating Linguistic Tags

- [Identifying Parts of Speech](identifying-parts-of-speech.md) — Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md) — Use a linguistic tagger to perform named entity recognition on a string.
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) — Enumerates over a given range of the string for a particular unit and calls the specified block for each tag. _(deprecated)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_scheme_options_using_).md>) — Enumerates over a given range of the string and calls the specified block for each tag. _(deprecated)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<nslinguistictagger/enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — Enumerates over a given string and calls the specified block for each tag. _(deprecated)_
- [Options](nslinguistictagger/options.md) — Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

### Getting Linguistic Tags

- [- tagAtIndex:unit:scheme:tokenRange:](<nslinguistictagger/tag(at_unit_scheme_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position. _(deprecated)_
- [- tagAtIndex:scheme:tokenRange:sentenceRange:](<nslinguistictagger/tag(at_scheme_tokenrange_sentencerange_).md>) — Returns a tag for a single scheme at the specified character position. _(deprecated)_
- [+ tagForString:atIndex:unit:scheme:orthography:tokenRange:](<nslinguistictagger/tag(for_at_unit_scheme_orthography_tokenrange_).md>) — Returns a tag for a single scheme, for a given linguistic unit, at the specified character position in a string. _(deprecated)_
- [- tagsInRange:unit:scheme:options:tokenRanges:](<nslinguistictagger/tags(in_unit_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range and linguistic unit. _(deprecated)_
- [- tagsInRange:scheme:options:tokenRanges:](<nslinguistictagger/tags(in_scheme_options_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string range. _(deprecated)_
- [+ tagsForString:range:unit:scheme:options:orthography:tokenRanges:](<nslinguistictagger/tags(for_range_unit_scheme_options_orthography_tokenranges_).md>) — Returns an array of linguistic tags and token ranges for a given string and linguistic unit. _(deprecated)_

### Determining the Range of a Unit Token

- [- tokenRangeAtIndex:unit:](<nslinguistictagger/tokenrange(at_unit_).md>) — Returns the range of the linguistic unit containing the specified character index. _(deprecated)_
- [- sentenceRangeForRange:](<nslinguistictagger/sentencerange(for_).md>) — Returns the range of a sentence containing the specified range. _(deprecated)_

### Determining the Possible Tags

- [- possibleTagsAtIndex:scheme:tokenRange:sentenceRange:scores:](<nslinguistictagger/possibletags(at_scheme_tokenrange_sentencerange_scores_).md>) — Returns an array of possible tags for the given scheme at the specified range, supplying matching scores. _(deprecated)_

### Notifying for Changes to the Analyzed String

- [- stringEditedInRange:changeInLength:](<nslinguistictagger/stringedited(in_changeinlength_).md>) — Notifies the linguistic tagger that the string (if mutable) has changed as specified by the parameters. _(deprecated)_

### Supporting Types

- [NSLinguisticTagScheme](nslinguistictagscheme.md) — Constants for the tag schemes specified when initializing a linguistic tagger.
- [NSLinguisticTaggerUnit](nslinguistictaggerunit.md) — Constants representing linguistic units.
- [NSLinguisticTag](nslinguistictag.md) — A token, lexical class, name, lemma, language, or script returned by a linguistic tagger for natural language text.

## See Also

### Deprecated

- [Deprecated String Encodings](1497268-deprecated-string-encodings.md)

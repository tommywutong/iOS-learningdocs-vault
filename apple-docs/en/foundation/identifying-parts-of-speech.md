---
title: Identifying Parts of Speech
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/identifying-parts-of-speech
source_url: 'https://developer.apple.com/documentation/foundation/identifying-parts-of-speech'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/identifying-parts-of-speech.json'
content_hash: 'sha256:a376c9f52a3bbae4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSLinguisticTagger](nslinguistictagger.md)

# Identifying Parts of Speech

<sub>Article</sub>

Classify nouns, verbs, adjectives, and other parts of speech in a string.

## Overview

Identifying the parts of speech for words in natural language text can help your program understand the meaning of sentences. For example, given the transcription of a request spoken by the user, you might determine general intent by looking at only the nouns and verbs.

The example below shows how to use [NSLinguisticTagger](nslinguistictagger.md) to enumerate over natural language text and identify the part of speech for each word.

```swift
let text = "The ripe taste of cheese improves with age."
let tagger = NSLinguisticTagger(tagSchemes: [.lexicalClass], options: 0)
tagger.string = text
let range = NSRange(location: 0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace]
tagger.enumerateTags(in: range, unit: .word, scheme: .lexicalClass, options: options) { tag, tokenRange, _ in
    if let tag = tag {
        let word = (text as NSString).substring(with: tokenRange)
        print("\(word): \(tag)")
    }
}
```

First, an instance of [NSLinguisticTagger](nslinguistictagger.md) is created, specifying [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) as the tag scheme to be used. Next, the [string](nslinguistictagger/string.md) property of the linguistic tagger is set to the natural language text. Finally, the linguistic tagger enumerates over the entire range of the string, specifying [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) as the tag unit and [NSLinguisticTagSchemeLexicalClass](nslinguistictagscheme/lexicalclass.md) as the tag scheme, and omitting any punctuation or whitespace. In the enumeration block, the part of speech is provided by `tag`, and each word is obtained by taking a substring of the original text at `tokenRange`.

When run, this code prints out each word and its part of speech on a new line, as shown below:

| Word | Part of speech |
|---|---|
| The | [NSLinguisticTagDeterminer](nslinguistictag/determiner.md) |
| ripe | [NSLinguisticTagAdjective](nslinguistictag/adjective.md) |
| taste | [NSLinguisticTagNoun](nslinguistictag/noun.md) |
| of | [NSLinguisticTagPreposition](nslinguistictag/preposition.md) |
| cheese | [NSLinguisticTagNoun](nslinguistictag/noun.md) |
| improves | [NSLinguisticTagVerb](nslinguistictag/verb.md) |
| with | [NSLinguisticTagPreposition](nslinguistictag/preposition.md) |
| age | [NSLinguisticTagNoun](nslinguistictag/noun.md) |

## See Also

### Related Documentation

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md) — Enumerate the words in a string.

### Enumerating Linguistic Tags

- [Identifying People, Places, and Organizations](identifying-people-places-and-organizations.md) — Use a linguistic tagger to perform named entity recognition on a string.
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) — Enumerates over a given range of the string for a particular unit and calls the specified block for each tag. _(deprecated)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_scheme_options_using_).md>) — Enumerates over a given range of the string and calls the specified block for each tag. _(deprecated)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<nslinguistictagger/enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — Enumerates over a given string and calls the specified block for each tag. _(deprecated)_
- [Options](nslinguistictagger/options.md) — Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

---
title: Identifying People, Places, and Organizations
framework: Foundation
symbol_kind: article
role: article
role_heading: Article
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/identifying-people-places-and-organizations
source_url: 'https://developer.apple.com/documentation/foundation/identifying-people-places-and-organizations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/identifying-people-places-and-organizations.json'
content_hash: 'sha256:30085566a539f1d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSLinguisticTagger](nslinguistictagger.md)

# Identifying People, Places, and Organizations

<sub>Article</sub>

Use a linguistic tagger to perform named entity recognition on a string.

## Overview

Identifying named entities in natural language text can help make your app more intelligent. For example, a messaging app might look for names of people and places in text in order to display related information like contact information or directions.

The example below shows how to use [NSLinguisticTagger](nslinguistictagger.md) to enumerate over natural language text and identify any named person, place, or organization.

```swift
let text = "The American Red Cross was established in Washington, D.C., by Clara Barton."
let tagger = NSLinguisticTagger(tagSchemes: [.nameType], options: 0)
tagger.string = text
let range = NSRange(location:0, length: text.utf16.count)
let options: NSLinguisticTagger.Options = [.omitPunctuation, .omitWhitespace, .joinNames]
let tags: [NSLinguisticTag] = [.personalName, .placeName, .organizationName]
tagger.enumerateTags(in: range, unit: .word, scheme: .nameType, options: options) { tag, tokenRange, stop in
    if let tag = tag, tags.contains(tag) {
        let name = (text as NSString).substring(with: tokenRange)
        print("\(name): \(tag)")
    }
}
```

First, an instance of [NSLinguisticTagger](nslinguistictagger.md) is created, specifying [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) as the tag scheme to be used. Next, the [string](nslinguistictagger/string.md) property of the linguistic tagger is set to the natural language text. Finally, the linguistic tagger enumerates over the entire range of the string, specifying [NSLinguisticTaggerUnitWord](nslinguistictaggerunit/word.md) as the tag unit and [NSLinguisticTagSchemeNameType](nslinguistictagscheme/nametype.md) as the tag scheme, omitting any punctuation or whitespace, and joining words that are part of a single name into the same token. In the enumeration block, the name type is provided by `tag`, and each word is obtained by taking a substring of the original text at `tokenRange`.

When run, this code prints out each name and its type on a new line, as shown below:

| Name | Type |
|---|---|
| The American Red Cross | [NSLinguisticTagOrganizationName](nslinguistictag/organizationname.md) |
| Washington, D.C. | [NSLinguisticTagPlaceName](nslinguistictag/placename.md) |
| Clara Barton | [NSLinguisticTagPersonalName](nslinguistictag/personalname.md) |

## See Also

### Related Documentation

- [Tokenizing Natural Language Text](tokenizing-natural-language-text.md) — Enumerate the words in a string.

### Enumerating Linguistic Tags

- [Identifying Parts of Speech](identifying-parts-of-speech.md) — Classify nouns, verbs, adjectives, and other parts of speech in a string.
- [- enumerateTagsInRange:unit:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_unit_scheme_options_using_).md>) — Enumerates over a given range of the string for a particular unit and calls the specified block for each tag. _(deprecated)_
- [- enumerateTagsInRange:scheme:options:usingBlock:](<nslinguistictagger/enumeratetags(in_scheme_options_using_).md>) — Enumerates over a given range of the string and calls the specified block for each tag. _(deprecated)_
- [+ enumerateTagsForString:range:unit:scheme:options:orthography:usingBlock:](<nslinguistictagger/enumeratetags(for_range_unit_scheme_options_orthography_using_).md>) — Enumerates over a given string and calls the specified block for each tag. _(deprecated)_
- [Options](nslinguistictagger/options.md) — Constants for linguistic tagger enumeration specifying which tokens to omit and whether to join names.

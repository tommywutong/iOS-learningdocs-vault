---
title: Grammatical-Analysis Details
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/grammatical-analysis-details
source_url: 'https://developer.apple.com/documentation/foundation/grammatical-analysis-details'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/grammatical-analysis-details.json'
content_hash: 'sha256:820aa312edee8d68'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [Strings and Text](strings-and-text.md) · [NSSpellServer](nsspellserver.md)

# Grammatical-Analysis Details

<sub>API Collection</sub>

These constants are used as the keys in the outDetails dictionaries returned by [NSSpellServer](nsspellserver.md) and [checkGrammar(of:startingAt:language:wrap:inSpellDocumentWithTag:details:)](<../appkit/nsspellchecker/checkgrammar(of_startingat_language_wrap_inspelldocumentwithtag_details_).md>) ([NSSpellChecker](../appkit/nsspellchecker.md)).

## Topics

### Constants

- [NSGrammarRange](nsgrammarrange.md) — The value for the `NSGrammarRange` dictionary key should be an `NSValue` containing an `NSRange`, a subrange of the sentence range used as the return value, whose location should be an offset from the beginning of the sentence–so, for example, an `NSGrammarRange` for the first four characters of the overall sentence range should be `{0, 4}`. If the `NSGrammarRange` key is not present in the dictionary it is assumed to be equal to the overall sentence range.
- [NSGrammarUserDescription](nsgrammaruserdescription.md) — The value for the `NSGrammarUserDescription` dictionary key should be an `NSString` containing descriptive text about that range, to be presented directly to the user; it is intended that the user description should provide enough information to allow the user to correct the problem. It is recommended that `NSGrammarUserDescription` be supplied in all cases, however, `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.
- [NSGrammarCorrections](nsgrammarcorrections.md) — The value for the `NSGrammarCorrections` key should be an `NSArray` of `NSStrings` representing potential substitutions to correct the problem, but it is expected that this may not be available in all cases. `NSGrammarUserDescription` or `NSGrammarCorrections` must be supplied in order for correction guidance to be presented to the user.

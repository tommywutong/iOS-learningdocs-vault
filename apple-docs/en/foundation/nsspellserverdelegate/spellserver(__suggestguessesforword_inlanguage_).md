---
title: 'spellServer(_:suggestGuessesForWord:inLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestguessesforword:inlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Asuggestguessesforword%3Ainlanguage%3A%29.json'
content_hash: 'sha256:60fd47a74d6794c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:suggestGuessesForWord:inLanguage:)

<sub>Instance Method</sub>

Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, suggestGuessesForWord word: String, inLanguage language: String) -> [String]?
```

## Parameters

- `sender` — The `NSSpellServer` object that sent this message.

- `word` — The misspelled word.

- `language` — The language to use for the guesses.

## Return Value

An array of `NSString` objects indicating possible correct spellings.

## See Also

### Check Grammar and Spelling in Strings

- [- spellServer:checkString:offset:types:options:orthography:wordCount:](<spellserver(__check_offset_types_options_orthography_wordcount_).md>) — Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [- spellServer:checkGrammarInString:language:details:](<spellserver(__checkgrammarin_language_details_).md>) — Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [- spellServer:findMisspelledWordInString:language:wordCount:countOnly:](<spellserver(__findmisspelledwordin_language_wordcount_countonly_).md>) — Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.

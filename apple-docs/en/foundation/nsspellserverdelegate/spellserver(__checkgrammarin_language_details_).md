---
title: 'spellServer(_:checkGrammarIn:language:details:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:checkgrammarin:language:details:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Acheckgrammarin%3Alanguage%3Adetails%3A%29.json'
content_hash: 'sha256:fd25ba3a040f54fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:checkGrammarIn:language:details:)

<sub>Instance Method</sub>

Gives the delegate the opportunity to customize the grammatical analysis of a given string.

<sub>macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, checkGrammarIn stringToCheck: String, language: String?, details: AutoreleasingUnsafeMutablePointer<NSArray?>?) -> NSRange
```

## Parameters

- `sender` — Spell server satisfying a grammatical analysis request.

- `stringToCheck` — String to analyze.

- `language` — Language use in `string`. When `nil`, the language selected in the Spelling panel is used.

- `details` — On output, dictionaries describing grammar-analysis details within the flagged grammatical unit. See the [NSSpellServer](../nsspellserver.md) class for information about these dictionaries.

## Return Value

Location of the first flagged grammatical unit within `string`.

## See Also

### Check Grammar and Spelling in Strings

- [- spellServer:checkString:offset:types:options:orthography:wordCount:](<spellserver(__check_offset_types_options_orthography_wordcount_).md>) — Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [- spellServer:suggestGuessesForWord:inLanguage:](<spellserver(__suggestguessesforword_inlanguage_).md>) — Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [- spellServer:findMisspelledWordInString:language:wordCount:countOnly:](<spellserver(__findmisspelledwordin_language_wordcount_countonly_).md>) — Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.

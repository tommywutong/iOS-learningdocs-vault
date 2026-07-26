---
title: 'spellServer(_:findMisspelledWordIn:language:wordCount:countOnly:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:findmisspelledwordin:language:wordcount:countonly:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:findmisspelledwordin:language:wordcount:countonly:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Afindmisspelledwordin%3Alanguage%3Awordcount%3Acountonly%3A%29.json'
content_hash: 'sha256:74fa5e0990283163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:findMisspelledWordIn:language:wordCount:countOnly:)

<sub>Instance Method</sub>

Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, findMisspelledWordIn stringToCheck: String, language: String, wordCount: UnsafeMutablePointer<Int>, countOnly: Bool) -> NSRange
```

## Parameters

- `sender` — The `NSSpellServer` object that sent this message.

- `stringToCheck` — The string to search for the misspelled word.

- `language` — The language to use for the search.

- `wordCount` — On output, returns by reference the number of words from the beginning of the string object until the misspelled word (or the end of string).

- `countOnly` — If [true](../../swift/true.md), the method only counts the words in the string object and does not spell checking.

## Return Value

The range of the misspelled word within the given string.

## Discussion

Send [- isWordInUserDictionaries:caseSensitive:](<../nsspellserver/isword(inuserdictionaries_casesensitive_).md>) to the spelling server to determine if the word exists in the user’s language dictionaries.

## See Also

### Check Grammar and Spelling in Strings

- [- spellServer:checkString:offset:types:options:orthography:wordCount:](<spellserver(__check_offset_types_options_orthography_wordcount_).md>) — Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [- spellServer:suggestGuessesForWord:inLanguage:](<spellserver(__suggestguessesforword_inlanguage_).md>) — Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [- spellServer:checkGrammarInString:language:details:](<spellserver(__checkgrammarin_language_details_).md>) — Gives the delegate the opportunity to customize the grammatical analysis of a given string.

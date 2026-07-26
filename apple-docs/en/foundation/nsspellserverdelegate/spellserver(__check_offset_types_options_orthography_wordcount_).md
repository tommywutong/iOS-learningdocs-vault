---
title: 'spellServer(_:check:offset:types:options:orthography:wordCount:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.6+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:check:offset:types:options:orthography:wordcount:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Acheck%3Aoffset%3Atypes%3Aoptions%3Aorthography%3Awordcount%3A%29.json'
content_hash: 'sha256:bd748555932f2e7a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:check:offset:types:options:orthography:wordCount:)

<sub>Instance Method</sub>

Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.

<sub>macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, check stringToCheck: String, offset: Int, types checkingTypes: NSTextCheckingTypes, options: [String : Any]? = nil, orthography: NSOrthography?, wordCount: UnsafeMutablePointer<Int>) -> [NSTextCheckingResult]?
```

## Parameters

- `sender` — Spell server making the analysis request.

- `stringToCheck` — String to analyze.

- `offset` — The offset in the string.

- `checkingTypes` — The text checking types to perform.

- `options` — A dictionary defining the actions to be taken while checking this string. See Constants in [NSSpellChecker](../../appkit/nsspellchecker.md) for the possible keys.

- `orthography` — The identified orthography of `stringToCheck`. See [NSOrthography](../nsorthography.md) for more information.

- `wordCount` — On output, returns by-reference the number of words from the beginning of the string object until the misspelled word (or the end of string).

## Return Value

An array of NSTextCheckingResult instances of the spelling, grammar, or correction types, depending on the `checkingTypes` requested.

## Discussion

This method is optional, but if implemented it will be called during the course of unified text checking via the `NSSpellChecker` [checkSpelling(of:startingAt:)](<../../appkit/nsspellchecker/checkspelling(of_startingat_).md>) and [requestChecking(of:range:types:options:inSpellDocumentWithTag:completionHandler:)](<../../appkit/nsspellchecker/requestchecking(of_range_types_options_inspelldocumentwithtag_completionhandler_).md>) methods.  This allows spelling and grammar checking to be performed simultaneously, which can be significantly more efficient, and allows the delegate to return autocorrection results as well.

If this method is not implemented, then unified text checking will call the separate spelling and grammar checking methods instead.

This method may be called repeatedly with strings representing different subranges of the string that was originally requested to be checked; the offset argument represents the offset of the portion passed in to this method within that original string, and should be added to the origin of the range in any [NSTextCheckingResult](../nstextcheckingresult.md) returned.

## See Also

### Related Documentation

- [Spell Checking Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/SpellCheck/SpellCheck.html#//apple_ref/doc/uid/10000092i)

### Check Grammar and Spelling in Strings

- [- spellServer:suggestGuessesForWord:inLanguage:](<spellserver(__suggestguessesforword_inlanguage_).md>) — Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [- spellServer:checkGrammarInString:language:details:](<spellserver(__checkgrammarin_language_details_).md>) — Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [- spellServer:findMisspelledWordInString:language:wordCount:countOnly:](<spellserver(__findmisspelledwordin_language_wordcount_countonly_).md>) — Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.

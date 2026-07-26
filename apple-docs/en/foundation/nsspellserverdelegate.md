---
title: NSSpellServerDelegate
framework: Foundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsspellserverdelegate
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate.json'
content_hash: 'sha256:b66833c0d5623a6a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSSpellServerDelegate

<sub>Protocol</sub>

The optional methods implemented by the delegate of a spell server.

<sub>Mac Catalyst, macOS</sub>

```swift
protocol NSSpellServerDelegate : NSObjectProtocol
```

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Check Grammar and Spelling in Strings

- [- spellServer:checkString:offset:types:options:orthography:wordCount:](<nsspellserverdelegate/spellserver(__check_offset_types_options_orthography_wordcount_).md>) — Gives the delegate the opportunity to analyze both the spelling and grammar simultaneously, which is more efficient.
- [- spellServer:suggestGuessesForWord:inLanguage:](<nsspellserverdelegate/spellserver(__suggestguessesforword_inlanguage_).md>) — Gives the delegate the opportunity to suggest guesses to the sender for the correct spelling of the given misspelled word in the specified language.
- [- spellServer:checkGrammarInString:language:details:](<nsspellserverdelegate/spellserver(__checkgrammarin_language_details_).md>) — Gives the delegate the opportunity to customize the grammatical analysis of a given string.
- [- spellServer:findMisspelledWordInString:language:wordCount:countOnly:](<nsspellserverdelegate/spellserver(__findmisspelledwordin_language_wordcount_countonly_).md>) — Asks the delegate to search for a misspelled word in a given string, using the specified language, and marking the first misspelled word found by returning its range within the string.

### Managing the Spelling Dictionary

- [- spellServer:didForgetWord:inLanguage:](<nsspellserverdelegate/spellserver(__didforgetword_inlanguage_).md>) — Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [- spellServer:didLearnWord:inLanguage:](<nsspellserverdelegate/spellserver(__didlearnword_inlanguage_).md>) — Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [- spellServer:suggestCompletionsForPartialWordRange:inString:language:](<nsspellserverdelegate/spellserver(__suggestcompletionsforpartialwordrange_in_language_).md>) — This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [- spellServer:recordResponse:toCorrection:forWord:language:](<nsspellserverdelegate/spellserver(__recordresponse_tocorrection_forword_language_).md>) — Notifies the spell checker of the users’s response to a correction.

## See Also

### Spelling and Grammar

- [NSSpellServer](nsspellserver.md) — A server that your app uses to provide a spell checker service to other apps running in the system.

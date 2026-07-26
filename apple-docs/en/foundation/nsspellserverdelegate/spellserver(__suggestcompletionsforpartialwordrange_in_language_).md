---
title: 'spellServer(_:suggestCompletionsForPartialWordRange:in:language:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestcompletionsforpartialwordrange:in:language:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:suggestcompletionsforpartialwordrange:in:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Asuggestcompletionsforpartialwordrange%3Ain%3Alanguage%3A%29.json'
content_hash: 'sha256:ce4c0124b7703dfd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:suggestCompletionsForPartialWordRange:in:language:)

<sub>Instance Method</sub>

This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, suggestCompletionsForPartialWordRange range: NSRange, in string: String, language: String) -> [String]?
```

## Parameters

- `sender` — The `NSSpellServer` object that sent this message.

- `range` — The range of the partially completed word.

- `string` — The string containing the partial word range.

- `language` — The language to use for the completion.

## Return Value

An array of `NSString` objects indicating possible completions.

## See Also

### Related Documentation

- [completions(forPartialWordRange:in:language:inSpellDocumentWithTag:)](<../../appkit/nsspellchecker/completions(forpartialwordrange_in_language_inspelldocumentwithtag_).md>) — Provides a list of complete words that the user might be trying to type based on a partial word in a given string.

### Managing the Spelling Dictionary

- [- spellServer:didForgetWord:inLanguage:](<spellserver(__didforgetword_inlanguage_).md>) — Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [- spellServer:didLearnWord:inLanguage:](<spellserver(__didlearnword_inlanguage_).md>) — Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [- spellServer:recordResponse:toCorrection:forWord:language:](<spellserver(__recordresponse_tocorrection_forword_language_).md>) — Notifies the spell checker of the users’s response to a correction.

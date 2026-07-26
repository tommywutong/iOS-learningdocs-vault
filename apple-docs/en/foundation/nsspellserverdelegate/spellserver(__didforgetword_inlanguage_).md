---
title: 'spellServer(_:didForgetWord:inLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:didforgetword:inlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:didforgetword:inlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Adidforgetword%3Ainlanguage%3A%29.json'
content_hash: 'sha256:52430f3cb04ac118'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:didForgetWord:inLanguage:)

<sub>Instance Method</sub>

Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, didForgetWord word: String, inLanguage language: String)
```

## Parameters

- `sender` — The `NSSpellServer` object that removed the word.

- `word` — The word that was removed.

- `language` — The language of the removed word.

## Discussion

If your delegate maintains a similar auxiliary word list, you may wish to edit the list accordingly.

## See Also

### Managing the Spelling Dictionary

- [- spellServer:didLearnWord:inLanguage:](<spellserver(__didlearnword_inlanguage_).md>) — Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [- spellServer:suggestCompletionsForPartialWordRange:inString:language:](<spellserver(__suggestcompletionsforpartialwordrange_in_language_).md>) — This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [- spellServer:recordResponse:toCorrection:forWord:language:](<spellserver(__recordresponse_tocorrection_forword_language_).md>) — Notifies the spell checker of the users’s response to a correction.

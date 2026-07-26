---
title: 'spellServer(_:didLearnWord:inLanguage:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:didlearnword:inlanguage:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:didlearnword:inlanguage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Adidlearnword%3Ainlanguage%3A%29.json'
content_hash: 'sha256:ec5de98686075b29'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:didLearnWord:inLanguage:)

<sub>Instance Method</sub>

Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, didLearnWord word: String, inLanguage language: String)
```

## Parameters

- `sender` — The `NSSpellServer` object that added the word.

- `word` — The word that was added.

- `language` — The language of the added word.

## Discussion

If your delegate maintains a similar auxiliary word list, you may wish to edit the list accordingly.

## See Also

### Managing the Spelling Dictionary

- [- spellServer:didForgetWord:inLanguage:](<spellserver(__didforgetword_inlanguage_).md>) — Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [- spellServer:suggestCompletionsForPartialWordRange:inString:language:](<spellserver(__suggestcompletionsforpartialwordrange_in_language_).md>) — This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.
- [- spellServer:recordResponse:toCorrection:forWord:language:](<spellserver(__recordresponse_tocorrection_forword_language_).md>) — Notifies the spell checker of the users’s response to a correction.

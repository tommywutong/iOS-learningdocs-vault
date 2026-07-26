---
title: 'spellServer(_:recordResponse:toCorrection:forWord:language:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsspellserverdelegate/spellserver(_:recordresponse:tocorrection:forword:language:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsspellserverdelegate/spellserver(_:recordresponse:tocorrection:forword:language:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsspellserverdelegate/spellserver%28_%3Arecordresponse%3Atocorrection%3Aforword%3Alanguage%3A%29.json'
content_hash: 'sha256:8c7e255f2d6bacac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSpellServerDelegate](../nsspellserverdelegate.md)

# spellServer(_:recordResponse:toCorrection:forWord:language:)

<sub>Instance Method</sub>

Notifies the spell checker of the users’s response to a correction.

<sub>macOS</sub>

```swift
optional func spellServer(_ sender: NSSpellServer, recordResponse response: Int, toCorrection correction: String, forWord word: String, language: String)
```

## Parameters

- `sender` — The spell server.

- `response` — The user’s response.

- `correction` — The corrected word. This should match the original correction.

- `word` — The original word. This should match the original correction.

- `language` — The language being edited. This should match the original correction.

## Discussion

When the user accepts, rejects, or edits an autocorrection, the view notifies the [NSSpellChecker](../../appkit/nsspellchecker.md) class of what happened in the client application, and `NSSpellChecker` then invokes this method, so that it can record that and modify future autocorrection behavior based on what it has learned from the user’s actions.

## See Also

### Managing the Spelling Dictionary

- [- spellServer:didForgetWord:inLanguage:](<spellserver(__didforgetword_inlanguage_).md>) — Notifies the delegate that the sender has removed the specified word from the user’s list of acceptable words in the specified language.
- [- spellServer:didLearnWord:inLanguage:](<spellserver(__didlearnword_inlanguage_).md>) — Notifies the delegate that the sender has added the specified word to the user’s list of acceptable words in the specified language.
- [- spellServer:suggestCompletionsForPartialWordRange:inString:language:](<spellserver(__suggestcompletionsforpartialwordrange_in_language_).md>) — This delegate method returns an array of possible word completions from the spell checker, based on a partially completed string and a given range.

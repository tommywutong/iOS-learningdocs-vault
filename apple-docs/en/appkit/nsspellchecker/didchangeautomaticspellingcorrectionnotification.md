---
title: didChangeAutomaticSpellingCorrectionNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsspellchecker/didchangeautomaticspellingcorrectionnotification.json'
content_hash: 'sha256:9cb594262f183d1d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSSpellChecker](../nsspellchecker.md)

# didChangeAutomaticSpellingCorrectionNotification

<sub>Type Property</sub>

This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.

<sub>macOS</sub>

```swift
class let didChangeAutomaticSpellingCorrectionNotification: NSNotification.Name
```

## Discussion

To observe this notification using Swift concurrency, use [DidChangeAutomaticSpellingCorrectionMessage](didchangeautomaticspellingcorrectionmessage.md).

## See Also

### Notifications

- [NSSpellCheckerDidChangeAutomaticTextReplacementNotification](didchangeautomatictextreplacementnotification.md) — Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.

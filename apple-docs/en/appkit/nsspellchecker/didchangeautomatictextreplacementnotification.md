---
title: didChangeAutomaticTextReplacementNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.7+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsspellchecker/didchangeautomatictextreplacementnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsspellchecker/didchangeautomatictextreplacementnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsspellchecker/didchangeautomatictextreplacementnotification.json'
content_hash: 'sha256:e39415f85c85a97a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSSpellChecker](../nsspellchecker.md)

# didChangeAutomaticTextReplacementNotification

<sub>Type Property</sub>

Posted when the spell checker changed text using automatic text replacement.  This notification is posted to the app’s default notification center.

<sub>macOS</sub>

```swift
class let didChangeAutomaticTextReplacementNotification: NSNotification.Name
```

## Discussion

To observe this notification using Swift concurrency, use [DidChangeAutomaticTextReplacementMessage](didchangeautomatictextreplacementmessage.md).

## See Also

### Notifications

- [NSSpellCheckerDidChangeAutomaticSpellingCorrectionNotification](didchangeautomaticspellingcorrectionnotification.md) — This notification is posted when the spell checker did change text using automatic spell checking correction. The are posted to the application’s default notification center.

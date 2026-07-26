---
title: fontSetChangedNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsfont/fontsetchangednotification
source_url: 'https://developer.apple.com/documentation/appkit/nsfont/fontsetchangednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsfont/fontsetchangednotification.json'
content_hash: 'sha256:da479b855ecd87ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSFont](../nsfont.md)

# fontSetChangedNotification

<sub>Type Property</sub>

Posted after the currently-set font changes.

<sub>macOS</sub>

```swift
class let fontSetChangedNotification: NSNotification.Name
```

## Discussion

To observe this notification using Swift concurrency, use [FontSetChangedMessage](fontsetchangedmessage.md).

## See Also

### Responding to Font-Related Notifications

- [NSAntialiasThresholdChangedNotification](antialiasthresholdchangednotification.md) — Posted after the threshold for antialiasing changes.

---
title: systemColorsDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscolor/systemcolorsdidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nscolor/systemcolorsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscolor/systemcolorsdidchangenotification.json'
content_hash: 'sha256:52fbb54f28267222'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSColor](../nscolor.md)

# systemColorsDidChangeNotification

<sub>Type Property</sub>

Sent when the system colors have changed, such as through a system control panel interface.

<sub>macOS</sub>

```swift
class let systemColorsDidChangeNotification: NSNotification.Name
```

## Discussion

This notification contains no notification object and no `userInfo` dictionary.

To observe this notification using Swift concurrency, use [SystemColorsDidChangeMessage](systemcolorsdidchangemessage.md).

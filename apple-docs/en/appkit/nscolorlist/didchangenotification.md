---
title: didChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS]
languages: [swift, swift, swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nscolorlist/didchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nscolorlist/didchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nscolorlist/didchangenotification.json'
content_hash: 'sha256:1b01fb8ce7dfeced'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSColorList](../nscolorlist.md)

# didChangeNotification

<sub>Type Property</sub>

Posted whenever a color list changes.

<sub>macOS</sub>

```swift
class let didChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the [NSColorList](../nscolorlist.md) object that changed. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [DidChangeMessage](didchangemessage.md).

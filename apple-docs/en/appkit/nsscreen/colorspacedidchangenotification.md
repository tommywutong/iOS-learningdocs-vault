---
title: colorSpaceDidChangeNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.6+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsscreen/colorspacedidchangenotification
source_url: 'https://developer.apple.com/documentation/appkit/nsscreen/colorspacedidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsscreen/colorspacedidchangenotification.json'
content_hash: 'sha256:aa1d0dca0b620930'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSScreen](../nsscreen.md)

# colorSpaceDidChangeNotification

<sub>Type Property</sub>

Posted when the color space of the screen has changed.

<sub>macOS</sub>

```swift
class let colorSpaceDidChangeNotification: NSNotification.Name
```

## Discussion

The notification object is the [NSScreen](../nsscreen.md) object whose [colorSpace](colorspace.md) has changed.. This notification does not contain a `userInfo` dictionary.

To observe this notification using Swift concurrency, use [ColorSpaceDidChangeMessage](colorspacedidchangemessage.md).

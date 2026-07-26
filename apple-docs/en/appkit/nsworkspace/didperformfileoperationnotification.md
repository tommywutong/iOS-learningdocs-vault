---
title: didPerformFileOperationNotification
framework: AppKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 10.0+（10.11 起废弃）]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/appkit/nsworkspace/didperformfileoperationnotification
source_url: 'https://developer.apple.com/documentation/appkit/nsworkspace/didperformfileoperationnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/appkit/nsworkspace/didperformfileoperationnotification.json'
content_hash: 'sha256:52a6f5f5afaf8d71'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AppKit](../../appkit.md) · [NSWorkspace](../nsworkspace.md)

# didPerformFileOperationNotification

<sub>Type Property</sub>

Posted when a file operation has been performed in the receiving app.

<sub>macOS</sub>

```swift
class let didPerformFileOperationNotification: NSNotification.Name
```

## Discussion

The notification object is the shared `NSWorkspace` instance. The `userInfo` dictionary contains a key `@"NSOperationNumber"` with a `NSNumber` object containing an integer indicating the type of file operation

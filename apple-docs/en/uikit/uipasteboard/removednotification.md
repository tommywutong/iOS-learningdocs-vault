---
title: removedNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/removednotification
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/removednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/removednotification.json'
content_hash: 'sha256:09a365f182bcf79c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# removedNotification

<sub>Type Property</sub>

A notification that a pasteboard object posts just before an app removes it.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let removedNotification: NSNotification.Name
```

## Discussion

The removal class method is [+ removePasteboardWithName:](<remove(withname_).md>). There is no `userInfo` dictionary.

## See Also

### Notifications

- [UIPasteboardChangedNotification](changednotification.md) — A notification that a pasteboard object posts when its contents change.

---
title: changedNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipasteboard/changednotification
source_url: 'https://developer.apple.com/documentation/uikit/uipasteboard/changednotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipasteboard/changednotification.json'
content_hash: 'sha256:d8aa0aed749912db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPasteboard](../uipasteboard.md)

# changedNotification

<sub>Type Property</sub>

A notification that a pasteboard object posts when its contents change.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let changedNotification: NSNotification.Name
```

## Discussion

This happens at the same time the pasteboard’s change count ([changeCount](changecount.md) property) is incremented. Changes include the addition, removal, and modification of pasteboard items. The `userInfo` dictionary may contain the representation types of pasteboard items that have been added to or removed from the pasteboard. See [UserInfo Dictionary Keys](../userinfo-dictionary-keys.md) for the keys used to access these representation types. If pasteboard items have been modified but not added or removed, the `userInfo` dictionary is `nil`.

## See Also

### Notifications

- [UIPasteboardRemovedNotification](removednotification.md) — A notification that a pasteboard object posts just before an app removes it.

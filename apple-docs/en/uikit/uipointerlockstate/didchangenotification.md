---
title: didChangeNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerlockstate/didchangenotification
source_url: 'https://developer.apple.com/documentation/uikit/uipointerlockstate/didchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerlockstate/didchangenotification.json'
content_hash: 'sha256:4501d03040990168'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerLockState](../uipointerlockstate.md)

# didChangeNotification

<sub>Type Property</sub>

A notification that posts when the value of the locked state for a scene changes.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let didChangeNotification: NSNotification.Name
```

## Discussion

This notification is sent when the value in the [locked](islocked.md) property changes. The `userInfo` dictionary of the notification contains the [UIPointerLockStateSceneUserInfoKey](sceneuserinfokey.md) key, which reflects the new value of the [locked](islocked.md) property.

## See Also

### Updating the Lock State

- [UIPointerLockStateSceneUserInfoKey](sceneuserinfokey.md) — A key that reflects the new locked state.

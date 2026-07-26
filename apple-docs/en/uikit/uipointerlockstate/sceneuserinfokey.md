---
title: sceneUserInfoKey
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipointerlockstate/sceneuserinfokey
source_url: 'https://developer.apple.com/documentation/uikit/uipointerlockstate/sceneuserinfokey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipointerlockstate/sceneuserinfokey.json'
content_hash: 'sha256:0f30263b7389a815'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPointerLockState](../uipointerlockstate.md)

# sceneUserInfoKey

<sub>Type Property</sub>

A key that reflects the new locked state.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
nonisolated class let sceneUserInfoKey: String
```

## Discussion

The `userInfo` dictionary of the notification contains the [UIPointerLockStateSceneUserInfoKey](sceneuserinfokey.md) key, which reflects the new value of the [locked](islocked.md) property.

## See Also

### Updating the Lock State

- [UIPointerLockStateDidChangeNotification](didchangenotification.md) — A notification that posts when the value of the locked state for a scene changes.

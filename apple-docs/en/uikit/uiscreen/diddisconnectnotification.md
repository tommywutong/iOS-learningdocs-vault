---
title: didDisconnectNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/diddisconnectnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/diddisconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/diddisconnectnotification.json'
content_hash: 'sha256:02a1687596c66249'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# didDisconnectNotification

<sub>Type Property</sub>

A notification the system posts when a screen disconnects from the device.

> [!warning] Deprecated
> Use the [- sceneDidDisconnect:](<../uiscenedelegate/scenediddisconnect(__).md>) method on a scene delegate or [UISceneDidDisconnectNotification](../uiscene/diddisconnectnotification.md) to recieve notification of disconnecting scenes from other screens.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let didDisconnectNotification: NSNotification.Name
```

## Discussion

The object of the notification is the [UIScreen](../uiscreen.md) object that represented the now-disconnected screen. There’s no `userInfo` dictionary.

## See Also

### Deprecated notifications

- [UIScreenDidConnectNotification](didconnectnotification.md) — A notification the system posts when a new screen connects to the device. _(deprecated)_

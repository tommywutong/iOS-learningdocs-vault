---
title: didConnectNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, tvOS（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/didconnectnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/didconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/didconnectnotification.json'
content_hash: 'sha256:4ecb33ba3eac5c7c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# didConnectNotification

<sub>Type Property</sub>

A notification the system posts when a new screen connects to the device.

> [!warning] Deprecated
> Use the [- scene:willConnectToSession:options:](<../uiscenedelegate/scene(__willconnectto_options_).md>) method on a scene delegate or [UISceneWillConnectNotification](../uiscene/willconnectnotification.md) to recieve notification of connecting scenes from other screens.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
nonisolated class let didConnectNotification: NSNotification.Name
```

## Discussion

Connection notifications aren’t sent for screens that are already present when the app launches. The app can instead use the [screens](screens.md) method to get the current set of screens at launch time.

The object of the notification is the [UIScreen](../uiscreen.md) object representing the new screen. There’s no `userInfo` dictionary.

## See Also

### Deprecated notifications

- [UIScreenDidDisconnectNotification](diddisconnectnotification.md) — A notification the system posts when a screen disconnects from the device. _(deprecated)_

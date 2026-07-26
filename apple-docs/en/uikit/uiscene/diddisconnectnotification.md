---
title: didDisconnectNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/diddisconnectnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/diddisconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/diddisconnectnotification.json'
content_hash: 'sha256:e0cb06dbe6ef5dc6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# didDisconnectNotification

<sub>Type Property</sub>

A notification that indicates that UIKit removed a scene from your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didDisconnectNotification: NSNotification.Name
```

## Discussion

Use this notification to perform any final cleanup before your scene is purged from memory. For example, use it to release references to files or shared resources and to save user data. UIKit places the affected scene in the [object](../../foundation/nsnotification/object.md) property of the notification.

The removal of a scene is a precursor to the destruction of that scene. UIKit disconnects a scene when the user explicitly closes it in the app switcher. UIKit may also disconnect a scene in order to reclaim memory for other processes. UIKit does not automatically disconnect a scene when the user switches to another app.

UIKit also calls the [- sceneDidDisconnect:](<../uiscenedelegate/scenediddisconnect(__).md>) method of your scene delegate object.

## See Also

### Responding to life cycle notifications

- [UISceneWillConnectNotification](willconnectnotification.md) — A notification that indicates that UIKit added a scene to your app.
- [UISceneWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [UISceneDidActivateNotification](didactivatenotification.md) — A notification that indicates that the scene is now onscreen and responding to user events.
- [UISceneWillDeactivateNotification](willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [UISceneDidEnterBackgroundNotification](didenterbackgroundnotification.md) — A notification that indicates that the scene is running in the background and is no longer onscreen.

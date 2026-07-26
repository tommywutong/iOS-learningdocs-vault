---
title: willEnterForegroundNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/willenterforegroundnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/willenterforegroundnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/willenterforegroundnotification.json'
content_hash: 'sha256:363cdfe33ed1b462'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# willEnterForegroundNotification

<sub>Type Property</sub>

A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let willEnterForegroundNotification: NSNotification.Name
```

## Discussion

UIKit posts this notification before moving a scene to the foreground. This transition occurs both for newly created and connected scenes and for scenes that were running in the background and were brought to the foreground by the system or a user action. A scene enters the foreground as a precursor to becoming visible onscreen, so this method is invariably followed by the posting of a [UISceneDidActivateNotification](didactivatenotification.md) notification. UIKit places the scene object in the [object](../../foundation/nsnotification/object.md) property of the notification.

UIKit also calls the [- sceneWillEnterForeground:](<../uiscenedelegate/scenewillenterforeground(__).md>) method of your scene delegate object.

## See Also

### Responding to life cycle notifications

- [UISceneWillConnectNotification](willconnectnotification.md) — A notification that indicates that UIKit added a scene to your app.
- [UISceneDidDisconnectNotification](diddisconnectnotification.md) — A notification that indicates that UIKit removed a scene from your app.
- [UISceneDidActivateNotification](didactivatenotification.md) — A notification that indicates that the scene is now onscreen and responding to user events.
- [UISceneWillDeactivateNotification](willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [UISceneDidEnterBackgroundNotification](didenterbackgroundnotification.md) — A notification that indicates that the scene is running in the background and is no longer onscreen.

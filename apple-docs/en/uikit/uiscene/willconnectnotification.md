---
title: willConnectNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/willconnectnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/willconnectnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/willconnectnotification.json'
content_hash: 'sha256:c912d427899a8c4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# willConnectNotification

<sub>Type Property</sub>

A notification that indicates that UIKit added a scene to your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let willConnectNotification: NSNotification.Name
```

## Discussion

When the user or your app requests a new instance of your user interface, UIKit creates an appropriate [UIScene](../uiscene.md) object and places it in the [object](../../foundation/nsnotification/object.md) property of the notification. Use this notification to respond to the addition of the new scene and to begin loading any data that the scene needs to display.

UIKit also calls the [- scene:willConnectToSession:options:](<../uiscenedelegate/scene(__willconnectto_options_).md>) method of your scene delegate object.

## See Also

### Responding to life cycle notifications

- [UISceneDidDisconnectNotification](diddisconnectnotification.md) — A notification that indicates that UIKit removed a scene from your app.
- [UISceneWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [UISceneDidActivateNotification](didactivatenotification.md) — A notification that indicates that the scene is now onscreen and responding to user events.
- [UISceneWillDeactivateNotification](willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [UISceneDidEnterBackgroundNotification](didenterbackgroundnotification.md) — A notification that indicates that the scene is running in the background and is no longer onscreen.

---
title: didActivateNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/didactivatenotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/didactivatenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/didactivatenotification.json'
content_hash: 'sha256:db51a16c6c39b86c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# didActivateNotification

<sub>Type Property</sub>

A notification that indicates that the scene is now onscreen and responding to user events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didActivateNotification: NSNotification.Name
```

## Discussion

Use this notification to prepare your scene to be onscreen. UIKit posts this notification after loading the interface for your scene, but before that interface appears onscreen. Use it to refresh the contents of views, start timers, or increase frame rates for your UI. UIKit places the scene object in the [object](../../foundation/nsnotification/object.md) property of the notification.

UIKit also calls the [- sceneDidBecomeActive:](<../uiscenedelegate/scenedidbecomeactive(__).md>) method of your scene delegate object.

For more information on what to do when your app becomes active, see [Preparing your UI to run in the foreground](../preparing-your-ui-to-run-in-the-foreground.md).

## See Also

### Responding to life cycle notifications

- [UISceneWillConnectNotification](willconnectnotification.md) — A notification that indicates that UIKit added a scene to your app.
- [UISceneDidDisconnectNotification](diddisconnectnotification.md) — A notification that indicates that UIKit removed a scene from your app.
- [UISceneWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [UISceneWillDeactivateNotification](willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.
- [UISceneDidEnterBackgroundNotification](didenterbackgroundnotification.md) — A notification that indicates that the scene is running in the background and is no longer onscreen.

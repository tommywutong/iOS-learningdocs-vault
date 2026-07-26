---
title: didEnterBackgroundNotification
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscene/didenterbackgroundnotification
source_url: 'https://developer.apple.com/documentation/uikit/uiscene/didenterbackgroundnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscene/didenterbackgroundnotification.json'
content_hash: 'sha256:e392566c6d41b6b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScene](../uiscene.md)

# didEnterBackgroundNotification

<sub>Type Property</sub>

A notification that indicates that the scene is running in the background and is no longer onscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
nonisolated class let didEnterBackgroundNotification: NSNotification.Name
```

## Discussion

Use this notification to reduce your scene’s memory usage, free up any shared resources, and clean up your scene’s user interface. Shortly after your notification handler returns, UIKit takes a snapshot of your scene’s interface for display in the app switcher. Make sure your interface doesn’t contain sensitive user information.

UIKit also calls the [- sceneDidEnterBackground:](<../uiscenedelegate/scenedidenterbackground(__).md>) method of your scene delegate object.

For more information about what to do when your app enters the background, see [Preparing your UI to run in the background](../preparing-your-ui-to-run-in-the-background.md).

## See Also

### Responding to life cycle notifications

- [UISceneWillConnectNotification](willconnectnotification.md) — A notification that indicates that UIKit added a scene to your app.
- [UISceneDidDisconnectNotification](diddisconnectnotification.md) — A notification that indicates that UIKit removed a scene from your app.
- [UISceneWillEnterForegroundNotification](willenterforegroundnotification.md) — A notification that indicates that a scene is about to begin running in the foreground and become visible to the user.
- [UISceneDidActivateNotification](didactivatenotification.md) — A notification that indicates that the scene is now onscreen and responding to user events.
- [UISceneWillDeactivateNotification](willdeactivatenotification.md) — A notification that indicates that the scene is about to resign the active state and stop responding to user events.

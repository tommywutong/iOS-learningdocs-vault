---
title: 'sceneDidEnterBackground(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scenedidenterbackground(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidenterbackground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scenedidenterbackground%28_%3A%29.json'
content_hash: 'sha256:e16850192d577a5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# sceneDidEnterBackground(_:)

<sub>Instance Method</sub>

Tells the delegate that the scene is running in the background and is no longer onscreen.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func sceneDidEnterBackground(_ scene: UIScene)
```

## Parameters

- `scene` — The scene that entered the background.

## Discussion

To use this method, you must implement the [UISceneDelegate](../uiscenedelegate.md) protocol and configure scenes for your app (see [Specifying the scenes your app supports](../specifying-the-scenes-your-app-supports.md)).

Use this method to reduce your scene’s memory usage, free up any shared resources, and clean up your scene’s user interface. Shortly after this method returns, UIKit takes a snapshot of your scene’s interface for display in the app switcher. Make sure your interface doesn’t contain sensitive user information.

In addition to calling this method, UIKit posts a [UISceneDidEnterBackgroundNotification](../uiscene/didenterbackgroundnotification.md) notification from [UIApplication](../uiapplication.md) and [UIScene](../uiscene.md).

For more information about what to do when your app enters the background, see [Preparing your UI to run in the background](../preparing-your-ui-to-run-in-the-background.md).

> [!note] Note
> When you implement this method and enable scenes, UIKit calls this method but does not call the [- applicationDidEnterBackground:](<../uiapplicationdelegate/applicationdidenterbackground(__).md>) method on [UIApplicationDelegate](../uiapplicationdelegate.md).

## See Also

### Transitioning to the background

- [- sceneWillResignActive:](<scenewillresignactive(__).md>) — Tells the delegate that the scene is about to resign the active state and stop responding to user events.

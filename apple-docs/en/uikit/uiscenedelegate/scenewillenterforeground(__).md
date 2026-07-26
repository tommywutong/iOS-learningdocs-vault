---
title: 'sceneWillEnterForeground(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scenewillenterforeground(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scenewillenterforeground(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scenewillenterforeground%28_%3A%29.json'
content_hash: 'sha256:ca6b538a2f7950b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# sceneWillEnterForeground(_:)

<sub>Instance Method</sub>

Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func sceneWillEnterForeground(_ scene: UIScene)
```

## Parameters

- `scene` — The scene that is about to enter the foreground.

## Discussion

To use this method, you must implement the [UISceneDelegate](../uiscenedelegate.md) protocol and configure scenes for your app (see [Specifying the scenes your app supports](../specifying-the-scenes-your-app-supports.md)).

UIKit calls this method before moving a scene to the foreground. This transition occurs both for newly created and connected scenes, as well as for scenes that were running in the background and were brought to the foreground by the system or a user action. A scene enters the foreground as a precursor to becoming visible onscreen, so this method is invariably followed by a call to the [- sceneDidBecomeActive:](<scenedidbecomeactive(__).md>) method.

In addition to calling this method, UIKit posts a [UISceneDidActivateNotification](../uiscene/didactivatenotification.md) and a [UISceneWillEnterForegroundNotification](../uiscene/willenterforegroundnotification.md).

For more information on what to do when your app is about to enter the foreground, see [Preparing your UI to run in the foreground](../preparing-your-ui-to-run-in-the-foreground.md).

> [!note] Note
> When you implement this method and enable scenes, UIKit calls this method but does not call the [- applicationWillEnterForeground:](<../uiapplicationdelegate/applicationwillenterforeground(__).md>) method on [UIApplicationDelegate](../uiapplicationdelegate.md).

## See Also

### Transitioning to the foreground

- [- sceneDidBecomeActive:](<scenedidbecomeactive(__).md>) — Tells the delegate that the scene became active and is now responding to user events.

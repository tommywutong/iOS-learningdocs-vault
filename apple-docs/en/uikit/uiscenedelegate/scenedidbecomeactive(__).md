---
title: 'sceneDidBecomeActive(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scenedidbecomeactive(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scenedidbecomeactive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scenedidbecomeactive%28_%3A%29.json'
content_hash: 'sha256:b1974ff0f93988e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# sceneDidBecomeActive(_:)

<sub>Instance Method</sub>

Tells the delegate that the scene became active and is now responding to user events.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func sceneDidBecomeActive(_ scene: UIScene)
```

## Parameters

- `scene` — The scene that became active and is now responding to user events.

## Discussion

To use this method, you must implement the [UISceneDelegate](../uiscenedelegate.md) protocol and configure scenes for your app (see [Specifying the scenes your app supports](../specifying-the-scenes-your-app-supports.md)).

Use this method to prepare your scene to be onscreen. UIKit calls this method after loading the interface for your scene, but before that interface appears onscreen. Use it to refresh the contents of views, start timers, or increase frame rates for your UI.

In addition to calling this method, UIKit posts a [UISceneDidActivateNotification](../uiscene/didactivatenotification.md) and a [UIApplicationDidBecomeActiveNotification](../uiapplication/didbecomeactivenotification.md).

For more information on what to do when your app becomes active, see [Preparing your UI to run in the foreground](../preparing-your-ui-to-run-in-the-foreground.md).

> [!note] Note
> When you implement this method and enable scenes, UIKit calls this method but does not call the [- applicationDidBecomeActive:](<../uiapplicationdelegate/applicationdidbecomeactive(__).md>) method on [UIApplicationDelegate](../uiapplicationdelegate.md).

## See Also

### Transitioning to the foreground

- [- sceneWillEnterForeground:](<scenewillenterforeground(__).md>) — Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.

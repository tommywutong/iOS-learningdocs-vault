---
title: UISceneDelegate
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenedelegate
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate.json'
content_hash: 'sha256:1579a2ad09fdc294'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneDelegate

<sub>Protocol</sub>

The core methods you use to respond to life-cycle events occurring within a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UISceneDelegate : NSObjectProtocol
```

## Overview

Use your [UISceneDelegate](uiscenedelegate.md) object to manage life-cycle events in one instance of your app’s user interface. This interface defines methods for responding to state transitions that affect the scene, including when the scene enters the foreground and becomes active, and when it enters the background. Use your delegate to provide appropriate behavior when these transitions occur. For example, finish critical tasks and quiet your app when it enters the background.

Don’t create [UISceneDelegate](uiscenedelegate.md) objects directly. Instead, specify the name of your custom delegate class as part of the configuration data for your scenes. You can specify this information in your app’s `Info.plist` file, or in the [UISceneConfiguration](uisceneconfiguration.md) object you return from your app delegate’s [- application:configurationForConnectingSceneSession:options:](<uiapplicationdelegate/application(__configurationforconnecting_options_).md>) method. For more information about how to configure scenes, see [Specifying the scenes your app supports](specifying-the-scenes-your-app-supports.md).

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

- **Inherited By**: [UIWindowSceneDelegate](uiwindowscenedelegate.md)

## Topics

### Working with window scenes

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md) — Support side-by-side instances of your app’s interface and create new windows.

### Connecting and disconnecting the scene

- [- scene:willConnectToSession:options:](<uiscenedelegate/scene(__willconnectto_options_).md>) — Tells the delegate about the addition of a scene to the app.
- [- sceneDidDisconnect:](<uiscenedelegate/scenediddisconnect(__).md>) — Tells the delegate that UIKit removed a scene from your app.
- [ConnectionOptions](uiscene/connectionoptions.md) — A data object containing information about the reasons why UIKit created the scene.

### Transitioning to the foreground

- [- sceneWillEnterForeground:](<uiscenedelegate/scenewillenterforeground(__).md>) — Tells the delegate that the scene is about to begin running in the foreground and become visible to the user.
- [- sceneDidBecomeActive:](<uiscenedelegate/scenedidbecomeactive(__).md>) — Tells the delegate that the scene became active and is now responding to user events.

### Transitioning to the background

- [- sceneWillResignActive:](<uiscenedelegate/scenewillresignactive(__).md>) — Tells the delegate that the scene is about to resign the active state and stop responding to user events.
- [- sceneDidEnterBackground:](<uiscenedelegate/scenedidenterbackground(__).md>) — Tells the delegate that the scene is running in the background and is no longer onscreen.

### Opening URLs

- [- scene:openURLContexts:](<uiscenedelegate/scene(__openurlcontexts_).md>) — Asks the delegate to open one or more URLs.

### Continuing user activities

- [- scene:willContinueUserActivityWithType:](<uiscenedelegate/scene(__willcontinueuseractivitywithtype_).md>) — Tells the delegate that it’s about to receive Handoff-related data.
- [- scene:continueUserActivity:](<uiscenedelegate/scene(__continue_).md>) — Tells the delegate to handle the specified Handoff-related activity.
- [- scene:didFailToContinueUserActivityWithType:error:](<uiscenedelegate/scene(__didfailtocontinueuseractivitywithtype_error_).md>) — Tells the delegate that the activity couldn’t be continued.

### Saving the state of the scene

- [Restoring your app’s state](restoring-your-app-s-state.md) — Provide continuity for the user by preserving current activities.
- [- stateRestorationActivityForScene:](<uiscenedelegate/staterestorationactivity(for_).md>) — Returns a user activity object encapsulating the current state of the specified scene.
- [- scene:restoreInteractionStateWithUserActivity:](<uiscenedelegate/scene(__restoreinteractionstatewith_).md>)
- [- scene:didUpdateUserActivity:](<uiscenedelegate/scene(__didupdate_).md>) — Tells the delegate that the specified activity object was updated.

## See Also

### Window scenes

- [Supporting multiple windows on iPad](supporting-multiple-windows-on-ipad.md) — Support side-by-side instances of your app’s interface and create new windows.
- [UIWindowSceneDelegate](uiwindowscenedelegate.md) — Additional methods that you use to manage app-specific tasks occurring in a scene.
- [UIWindowScene](uiwindowscene.md) — A scene that manages one or more windows for your app.
- [UIScene](uiscene.md) — An object that represents one instance of your app’s user interface.

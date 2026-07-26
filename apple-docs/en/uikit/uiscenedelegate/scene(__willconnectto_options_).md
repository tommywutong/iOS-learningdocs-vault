---
title: 'scene(_:willConnectTo:options:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scene(_:willconnectto:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scene(_:willconnectto:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scene%28_%3Awillconnectto%3Aoptions%3A%29.json'
content_hash: 'sha256:98c303dd1964e2ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# scene(_:willConnectTo:options:)

<sub>Instance Method</sub>

Tells the delegate about the addition of a scene to the app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions)
```

## Parameters

- `scene` — The scene object being connected to your app.

- `session` — The session object containing details about the scene’s configuration.

- `connectionOptions` — Additional options for configuring the scene. Use the information in this object to handle actions that caused the creation of the scene, for example, to respond to a quick action selected by the user.

## Discussion

This method is called when your app creates or restores an instance of your user interface.

When the user or your app requests a new instance of your user interface, UIKit creates an appropriate scene object and connects it to your app. Use this method to respond to the addition of the new scene and to begin loading any data that the scene needs to display.

When your app responds to scene activations requests, for example, by using [- requestSceneSessionActivation:userActivity:options:errorHandler:](<../uiapplication/requestscenesessionactivation(__useractivity_options_errorhandler_).md>), the user activity is in the [userActivities](../uiscene/connectionoptions/useractivities.md) set provided by options.

When the user reactivates an instance of your user interface, UIKit creates a scene object and populates it with saved state, provided by  [- stateRestorationActivityForScene:](<staterestorationactivity(for_).md>). When your app restores state, the user activity is presented in the [stateRestorationActivity](../uiscenesession/staterestorationactivity.md) property of session.

In addition to calling this method, UIKit also posts a [UISceneWillConnectNotification](../uiscene/willconnectnotification.md) notification.

## Topics

### Window Scenes

- [Supporting multiple windows on iPad](../supporting-multiple-windows-on-ipad.md) — Support side-by-side instances of your app’s interface and create new windows.

## See Also

### Connecting and disconnecting the scene

- [- sceneDidDisconnect:](<scenediddisconnect(__).md>) — Tells the delegate that UIKit removed a scene from your app.
- [ConnectionOptions](../uiscene/connectionoptions.md) — A data object containing information about the reasons why UIKit created the scene.

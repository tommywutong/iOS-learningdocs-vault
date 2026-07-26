---
title: 'sceneDidDisconnect(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, swift, swift, swift, swift, swift, occ, occ, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenedelegate/scenediddisconnect(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenedelegate/scenediddisconnect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenedelegate/scenediddisconnect%28_%3A%29.json'
content_hash: 'sha256:02cff1152a60564c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneDelegate](../uiscenedelegate.md)

# sceneDidDisconnect(_:)

<sub>Instance Method</sub>

Tells the delegate that UIKit removed a scene from your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func sceneDidDisconnect(_ scene: UIScene)
```

## Parameters

- `scene` — The scene that UIKit disconnected from your app.

## Discussion

Use this method to perform any final cleanup before your scene is purged from memory. For example, use it to release references to files or shared resources and to save user data.

The removal of a scene is a precursor to the destruction of that scene. UIKit disconnects a scene when the user explicitly closes it in the app switcher. UIKit may also disconnect a scene in order to reclaim memory for other processes. UIKit does not automatically disconnect a scene when the user switches to another app.

UIKit also posts a [UISceneDidDisconnectNotification](../uiscene/diddisconnectnotification.md) notification in addition to calling this method.

## See Also

### Connecting and disconnecting the scene

- [- scene:willConnectToSession:options:](<scene(__willconnectto_options_).md>) — Tells the delegate about the addition of a scene to the app.
- [ConnectionOptions](../uiscene/connectionoptions.md) — A data object containing information about the reasons why UIKit created the scene.

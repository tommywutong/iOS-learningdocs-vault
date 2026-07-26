---
title: 'requestSceneSessionRefresh(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/requestscenesessionrefresh(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessionrefresh(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/requestscenesessionrefresh%28_%3A%29.json'
content_hash: 'sha256:ef4e3abcc5c38538'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# requestSceneSessionRefresh(_:)

<sub>Instance Method</sub>

Asks the system to update any system UI associated with the specified scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestSceneSessionRefresh(_ sceneSession: UISceneSession)
```

## Parameters

- `sceneSession` — The session whose scene you want to update.

## Discussion

Call this method when your scene is in the background and any part of your scene’s visible appearance changes. For example, call this method after updating your scene’s content to let the system know your scene’s snapshot requires refreshing. You don’t need to call this method when your scene is running in the foreground.

## See Also

### Managing a scene’s life cycle

- [activateSceneSession(for:errorHandler:)](<activatescenesession(for_errorhandler_).md>) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionDestruction:options:errorHandler:](<requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md) — A collection of properties that you use to request activation of a scene.
- [ActivationRequestOptions](../uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

---
title: 'requestSceneSessionDestruction(_:options:errorHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, tvOS 13.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/requestscenesessiondestruction(_:options:errorhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/requestscenesessiondestruction(_:options:errorhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/requestscenesessiondestruction%28_%3Aoptions%3Aerrorhandler%3A%29.json'
content_hash: 'sha256:335b916767753510'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# requestSceneSessionDestruction(_:options:errorHandler:)

<sub>Instance Method</sub>

Asks the system to dismiss an existing scene and remove it from the app switcher.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func requestSceneSessionDestruction(_ sceneSession: UISceneSession, options: UISceneDestructionRequestOptions?, errorHandler: ((any Error) -> Void)? = nil)
```

## Parameters

- `sceneSession` — The session whose scene you want to remove from the screen and app switcher.

- `options` — Information for the system to use when dismissing the scene. For information about how to create this object, see [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md).

- `errorHandler` — An error handler block to execute if a problem occurs. The method does not execute this block when it successfully dismisses the scene. This block has no return value and has the following parameter: - **error** — The [NSError](../../foundation/nserror.md) object describing the problem that occurred.

## Discussion

If the specified scene is onscreen, calling this method dismisses it using the specified options. The method sends a disconnect notification to the scene and then calls your app delegate’s [- application:didDiscardSceneSessions:](<../uiapplicationdelegate/application(__diddiscardscenesessions_).md>) method.

## See Also

### Managing a scene’s life cycle

- [activateSceneSession(for:errorHandler:)](<activatescenesession(for_errorhandler_).md>) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionRefresh:](<requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md) — A collection of properties that you use to request activation of a scene.
- [ActivationRequestOptions](../uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

---
title: 'activateSceneSession(for:errorHandler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/activatescenesession(for:errorhandler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/activatescenesession(for:errorhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/activatescenesession%28for%3Aerrorhandler%3A%29.json'
content_hash: 'sha256:d40ba04449b29dd0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# activateSceneSession(for:errorHandler:)

<sub>Instance Method</sub>

Asks the system to activate an existing scene or create a new scene and associate it with your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor @preconcurrency func activateSceneSession(for request: UISceneSessionActivationRequest, errorHandler: ((any Error) -> Void)? = nil)
```

## Parameters

- `request` — The activation request.

- `errorHandler` — A handler to call if the request fails.

## See Also

### Related Documentation

- [- requestSceneSessionActivation:userActivity:options:errorHandler:](<requestscenesessionactivation(__useractivity_options_errorhandler_).md>) — Asks the system to activate an existing scene, or create a new scene and associate it with your app. _(deprecated)_

### Managing a scene’s life cycle

- [- requestSceneSessionDestruction:options:errorHandler:](<requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [- requestSceneSessionRefresh:](<requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md) — A collection of properties that you use to request activation of a scene.
- [ActivationRequestOptions](../uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

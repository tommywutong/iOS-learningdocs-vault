---
title: 'activateSceneSessionForRequest:errorHandler:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiapplication/activatescenesessionforrequest:errorhandler:'
source_url: 'https://developer.apple.com/documentation/uikit/uiapplication/activatescenesessionforrequest:errorhandler:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiapplication/activatescenesessionforrequest%3Aerrorhandler%3A.json'
content_hash: 'sha256:4d6a9d7b1c989c9f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIApplication](../uiapplication.md)

# activateSceneSessionForRequest:errorHandler:

<sub>Instance Method</sub>

Asks the system to activate an existing scene or create a new scene and associate it with your app.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
- (void) activateSceneSessionForRequest:(UISceneSessionActivationRequest *) request errorHandler:(void (^)(NSError *error)) errorHandler;
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
- [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md) — A collection of properties that you use to request activation of a scene.
- [ActivationRequestOptions](../uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](../uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

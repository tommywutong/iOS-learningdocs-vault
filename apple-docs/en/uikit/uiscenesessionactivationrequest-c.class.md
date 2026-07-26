---
title: UISceneSessionActivationRequest
framework: UIKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-c.class
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-c.class.json'
content_hash: 'sha256:e2fd42015a316254'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneSessionActivationRequest

<sub>Class</sub>

A collection of properties that you use to request activation of a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@interface UISceneSessionActivationRequest : NSObject
```

## Overview

A `UISceneSessionActiviationRequest` object provides information about how to activate a scene session. Create a request to specify:

- A user activity for the scene session.
- An existing scene session.
- A scene session with a specific role.

You create and configure a `UISceneSessionActivationRequest` object in your code, then you pass it as a parameter when you call [activateSceneSessionForRequest:errorHandler:](uiapplication/activatescenesessionforrequest_errorhandler_.md) to ask the system to activate the scene session.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [NSCopying](../foundation/nscopying.md)

## Topics

### Creating a request

- [request](uiscenesessionactivationrequest-c.class/request.md) — Creates a scene session activation request object.
- [requestWithRole:](uiscenesessionactivationrequest-c.class/requestwithrole_.md) — Creates a scene session activation request object with a role that you provide.
- [requestWithSession:](uiscenesessionactivationrequest-c.class/requestwithsession_.md) — Creates a scene session activation request object with a scene session that you provide.

### Managing request details

- [options](uiscenesessionactivationrequest-c.class/options.md) — Activation request options to further customize the request.
- [role](uiscenesessionactivationrequest-c.class/role.md) — The role to request.
- [session](uiscenesessionactivationrequest-c.class/session.md) — The specific scene session to activate.
- [userActivity](uiscenesessionactivationrequest-c.class/useractivity.md) — A user activity to send to the newly activated scene.

## See Also

### Managing a scene’s life cycle

- [activateSceneSessionForRequest:errorHandler:](uiapplication/activatescenesessionforrequest_errorhandler_.md) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionDestruction:options:errorHandler:](<uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [- requestSceneSessionRefresh:](<uiapplication/requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

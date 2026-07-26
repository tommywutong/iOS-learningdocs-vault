---
title: UISceneSessionActivationRequest
framework: UIKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-swift.struct
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct.json'
content_hash: 'sha256:334be21bf883cae8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UISceneSessionActivationRequest

<sub>Structure</sub>

A collection of properties that you use to request activation of a scene.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct UISceneSessionActivationRequest
```

## Overview

A `UISceneSessionActiviationRequest` object provides information about how to activate a scene session. Create a request to specify:

- A user activity for the scene session.
- An existing scene session.
- A scene session with a specific role.

You create a `UISceneSessionActivationRequest` object in your code, then you pass it as a parameter when you call [activateSceneSession(for:errorHandler:)](<uiapplication/activatescenesession(for_errorhandler_).md>) to ask the system to activate the scene session.

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md)

## Topics

### Creating a request

- [init(role:userActivity:options:)](<uiscenesessionactivationrequest-swift.struct/init(role_useractivity_options_).md>) — Creates a scene session activation request object with a role, a user activity, and options that you provide.
- [init(session:userActivity:options:)](<uiscenesessionactivationrequest-swift.struct/init(session_useractivity_options_).md>) — Creates a scene session activation request object with a scene session, a user activity, and options that you provide.

### Managing request details

- [options](uiscenesessionactivationrequest-swift.struct/options.md) — Activation request options to further customize the request.
- [role](uiscenesessionactivationrequest-swift.struct/role.md) — The role to request.
- [session](uiscenesessionactivationrequest-swift.struct/session.md) — The specific scene session to activate.
- [userActivity](uiscenesessionactivationrequest-swift.struct/useractivity.md) — A user activity to send to the newly activated scene.

### Initializers

- [init(hostingDelegateClass:)](<uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass_).md>) — Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene.
- [init(hostingDelegateClass:id:)](<uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass_id_).md>) — Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier.
- [init(hostingDelegateClass:id:value:)](<uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass_id_value_).md>) — Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with the given identifier and presented value.
- [init(hostingDelegateClass:value:)](<uiscenesessionactivationrequest-swift.struct/init(hostingdelegateclass_value_).md>) — Creates a `UISceneSessionActivationRequest` customized to open a SwiftUI scene with a presented value.

## See Also

### Managing a scene’s life cycle

- [activateSceneSession(for:errorHandler:)](<uiapplication/activatescenesession(for_errorhandler_).md>) — Asks the system to activate an existing scene or create a new scene and associate it with your app.
- [- requestSceneSessionDestruction:options:errorHandler:](<uiapplication/requestscenesessiondestruction(__options_errorhandler_).md>) — Asks the system to dismiss an existing scene and remove it from the app switcher.
- [- requestSceneSessionRefresh:](<uiapplication/requestscenesessionrefresh(__).md>) — Asks the system to update any system UI associated with the specified scene.
- [ActivationRequestOptions](uiscene/activationrequestoptions.md) — An object that contains information you want the system to use when activating the session associated with a scene.
- [UISceneDestructionRequestOptions](uiscenedestructionrequestoptions.md) — An object you pass to UIKit to permanently remove a scene and its associated session from your app.

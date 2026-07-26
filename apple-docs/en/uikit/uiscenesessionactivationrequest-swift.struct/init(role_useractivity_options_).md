---
title: 'init(role:userActivity:options:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(role:useractivity:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(role:useractivity:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init%28role%3Auseractivity%3Aoptions%3A%29.json'
content_hash: 'sha256:782b051eeb5263ae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# init(role:userActivity:options:)

<sub>Initializer</sub>

Creates a scene session activation request object with a role, a user activity, and options that you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(role: UISceneSession.Role = .windowApplication, userActivity: NSUserActivity? = nil, options: UIScene.ActivationRequestOptions? = nil)
```

## Parameters

- `role` — The role to request.

- `userActivity` — A user activity to send to the newly activated scene.

- `options` — Activation request options to further customize the request.

## Discussion

Create an activation request with this method when you want the system to activate a scene session appropriate for the `role` and `userActivity` you provide. The system activates an existing scene session when the scene session’s [role](../uiscenesession/role-swift.property.md) matches the [role](role.md) you request, and the user activity’s [targetContentIdentifier](../../foundation/nsuseractivity/targetcontentidentifier.md) satisfies the scene’s [activationConditions](../uiscene/activationconditions.md). Otherwise, the system activates a new scene session.

## See Also

### Creating a request

- [init(session:userActivity:options:)](<init(session_useractivity_options_).md>) — Creates a scene session activation request object with a scene session, a user activity, and options that you provide.

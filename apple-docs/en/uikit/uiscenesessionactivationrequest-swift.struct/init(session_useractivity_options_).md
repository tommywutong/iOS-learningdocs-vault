---
title: 'init(session:userActivity:options:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(session:useractivity:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init(session:useractivity:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/init%28session%3Auseractivity%3Aoptions%3A%29.json'
content_hash: 'sha256:d46e91144eb47d06'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# init(session:userActivity:options:)

<sub>Initializer</sub>

Creates a scene session activation request object with a scene session, a user activity, and options that you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(session: UISceneSession, userActivity: NSUserActivity? = nil, options: UIScene.ActivationRequestOptions? = nil)
```

## Parameters

- `session` — The specific scene session to activate.

- `userActivity` — A user activity to send to the newly activated scene.

- `options` — Activation request options to further customize the request.

## Discussion

Create an activation request with this method when you want the system to activate an existing scene session that you provide.

## See Also

### Creating a request

- [init(role:userActivity:options:)](<init(role_useractivity_options_).md>) — Creates a scene session activation request object with a role, a user activity, and options that you provide.

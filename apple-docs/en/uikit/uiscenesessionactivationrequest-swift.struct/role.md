---
title: role
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-swift.struct/role
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-swift.struct/role'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-swift.struct/role.json'
content_hash: 'sha256:98d96001df625cc4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-swift.struct.md)

# role

<sub>Instance Property</sub>

The role to request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var role: UISceneSession.Role { get }
```

## Discussion

If you created the request using [init(session:userActivity:options:)](<init(session_useractivity_options_).md>), this property reflects the role of the `session`.

## See Also

### Managing request details

- [options](options.md) — Activation request options to further customize the request.
- [session](session.md) — The specific scene session to activate.
- [userActivity](useractivity.md) — A user activity to send to the newly activated scene.

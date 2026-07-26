---
title: role
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-c.class/role
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/role'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-c.class/role.json'
content_hash: 'sha256:5ec82021d489bf03'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md)

# role

<sub>Instance Property</sub>

The role to request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
@property (nonatomic, readonly) UISceneSessionRole role;
```

## Discussion

If you created the request using [requestWithSession:](requestwithsession_.md), this property reflects the role of the `session`.

## See Also

### Managing request details

- [options](options.md) — Activation request options to further customize the request.
- [session](session.md) — The specific scene session to activate.
- [userActivity](useractivity.md) — A user activity to send to the newly activated scene.

---
title: 'requestWithRole:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithrole:'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithrole:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithrole%3A.json'
content_hash: 'sha256:452d7bb0e530ccee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md)

# requestWithRole:

<sub>Type Method</sub>

Creates a scene session activation request object with a role that you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) requestWithRole:(UISceneSessionRole) role;
```

## Parameters

- `role` — The role to request.

## Return Value

A scene session activation request object.

## Discussion

Create an activation request with this method when you want the system to activate a scene session appropriate for the `role` and `userActivity` you provide. The system activates an existing scene session when the scene session’s [role](../uiscenesession/role-swift.property.md) matches the [role](role.md) you request, and the user activity’s [targetContentIdentifier](../../foundation/nsuseractivity/targetcontentidentifier.md) satisfies the scene’s [activationConditions](../uiscene/activationconditions.md). Otherwise, the system activates a new scene session.

## See Also

### Creating a request

- [request](request.md) — Creates a scene session activation request object.
- [requestWithSession:](requestwithsession_.md) — Creates a scene session activation request object with a scene session that you provide.

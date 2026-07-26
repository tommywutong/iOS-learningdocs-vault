---
title: request
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uiscenesessionactivationrequest-c.class/request
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/request'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-c.class/request.json'
content_hash: 'sha256:b6db0c23c7134ecc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md)

# request

<sub>Type Method</sub>

Creates a scene session activation request object.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) request;
```

## Return Value

A scene session activation request object.

## Discussion

When you create a scene session activation request object with this method, [role](role.md) defaults to [UIWindowSceneSessionRoleApplication](../uiscenesession/role-swift.struct/windowapplication.md).

## See Also

### Creating a request

- [requestWithRole:](requestwithrole_.md) — Creates a scene session activation request object with a role that you provide.
- [requestWithSession:](requestwithsession_.md) — Creates a scene session activation request object with a scene session that you provide.

---
title: 'requestWithSession:'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithsession:'
source_url: 'https://developer.apple.com/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithsession:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscenesessionactivationrequest-c.class/requestwithsession%3A.json'
content_hash: 'sha256:5426a07a1ffa6baa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISceneSessionActivationRequest](../uiscenesessionactivationrequest-c.class.md)

# requestWithSession:

<sub>Type Method</sub>

Creates a scene session activation request object with a scene session that you provide.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) requestWithSession:(UISceneSession *) session;
```

## Parameters

- `session` — The specific scene session to activate.

## Return Value

A scene session activation request object.

## Discussion

Create an activation request with this method when you want the system to activate an existing scene session that you provide.

## See Also

### Creating a request

- [request](request.md) — Creates a scene session activation request object.
- [requestWithRole:](requestwithrole_.md) — Creates a scene session activation request object with a role that you provide.

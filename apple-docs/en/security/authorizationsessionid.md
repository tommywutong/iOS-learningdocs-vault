---
title: AuthorizationSessionId
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationsessionid
source_url: 'https://developer.apple.com/documentation/security/authorizationsessionid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationsessionid.json'
content_hash: 'sha256:f710ada9584994fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationSessionId

<sub>Type Alias</sub>

A unique value for an authorization session, provided by the authorization engine.

<sub>Mac Catalyst, macOS</sub>

```objc
typedef void * AuthorizationSessionId;
```

## Discussion

Use the [GetSessionId](authorizationcallbacks/getsessionid.md) function to retrieve the authorization session ID.

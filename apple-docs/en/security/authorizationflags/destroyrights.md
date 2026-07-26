---
title: destroyRights
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationflags/destroyrights
source_url: 'https://developer.apple.com/documentation/security/authorizationflags/destroyrights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationflags/destroyrights.json'
content_hash: 'sha256:585d80e5ae730e9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationFlags](../authorizationflags.md)

# destroyRights

<sub>Type Property</sub>

A flag that instructs the Security Server to revoke authorization.

<sub>Mac Catalyst, macOS</sub>

```swift
static var destroyRights: AuthorizationFlags { get }
```

## Discussion

If this flag is set, the Security Server revokes authorization from the process as well as from any other process that is sharing the authorization. If not set, the Security Server revokes authorization from the process but not from other processes that share the authorization.

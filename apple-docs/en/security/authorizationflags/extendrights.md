---
title: extendRights
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationflags/extendrights
source_url: 'https://developer.apple.com/documentation/security/authorizationflags/extendrights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationflags/extendrights.json'
content_hash: 'sha256:abccced0d7ff55b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationFlags](../authorizationflags.md)

# extendRights

<sub>Type Property</sub>

A flag that permits the Security Server to attempt to grant the rights requested.

<sub>Mac Catalyst, macOS</sub>

```swift
static var extendRights: AuthorizationFlags { get }
```

## Discussion

Once the Security Server denies one right, it ignores the remaining requested rights.

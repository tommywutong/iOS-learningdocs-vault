---
title: partialRights
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationflags/partialrights
source_url: 'https://developer.apple.com/documentation/security/authorizationflags/partialrights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationflags/partialrights.json'
content_hash: 'sha256:fb59a5a08343bd13'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationFlags](../authorizationflags.md)

# partialRights

<sub>Type Property</sub>

A flag that permits the Security Server to grant rights on an individual basis.

<sub>Mac Catalyst, macOS</sub>

```swift
static var partialRights: AuthorizationFlags { get }
```

## Discussion

If this and the [kAuthorizationFlagExtendRights](extendrights.md) flags are set, the Security Server grants or denies rights on an individual basis and all rights are checked.

---
title: interactionAllowed
framework: Security
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationflags/interactionallowed
source_url: 'https://developer.apple.com/documentation/security/authorizationflags/interactionallowed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationflags/interactionallowed.json'
content_hash: 'sha256:c020203902ec161c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [AuthorizationFlags](../authorizationflags.md)

# interactionAllowed

<sub>Type Property</sub>

A flag that permits user interaction as needed.

<sub>Mac Catalyst, macOS</sub>

```swift
static var interactionAllowed: AuthorizationFlags { get }
```

## Discussion

If this flag is set, the Security Server is permitted to interact with the user as needed.

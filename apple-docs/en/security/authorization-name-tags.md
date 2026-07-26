---
title: Authorization Name Tags
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorization-name-tags
source_url: 'https://developer.apple.com/documentation/security/authorization-name-tags'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorization-name-tags.json'
content_hash: 'sha256:19a392096f8350b3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Authorization Services](authorization-services.md)

# Authorization Name Tags

<sub>API Collection</sub>

Use name tags to define authorization security items.

## Overview

These tags are possible values for the `name` field of an [AuthorizationItem](authorizationitem.md) structure. This is not an all-inclusive set. You determine the name of the right to request. These environment tags are for future use.

## Topics

### Constants

- [kAuthorizationEnvironmentUsername](kauthorizationenvironmentusername.md) — The type for an authorization item containing a user name.
- [kAuthorizationEnvironmentPassword](kauthorizationenvironmentpassword.md) — The type for an authorization item containing a password.
- [kAuthorizationEnvironmentShared](kauthorizationenvironmentshared.md) — The type for an authorization item containing a shared right.
- [kAuthorizationRightExecute](kauthorizationrightexecute.md) — The type for an authorization item requesting the right to execute with privileges.
- [kAuthorizationEnvironmentPrompt](kauthorizationenvironmentprompt.md) — The type for an authorization item containing the name of the item that should be passed into the environment when specifying invocation-specific additional text.
- [kAuthorizationEnvironmentIcon](kauthorizationenvironmenticon.md) — The type for an authorization item containing the name of the item that should be passed into the environment when specifying an alternate icon.
- [kAuthorizationPamResult](kauthorizationpamresult.md) — The type for an authorization item containing a return code from a Pluggable Authentication Module (PAM).

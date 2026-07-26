---
title: Policy Database Constants
framework: Security
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/policy-database-constants
source_url: 'https://developer.apple.com/documentation/security/policy-database-constants'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/policy-database-constants.json'
content_hash: 'sha256:6d71fc00a512f9dd'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md) · [Authorization Services](authorization-services.md)

# Policy Database Constants

<sub>API Collection</sub>

Use these constants to set rights and rules in the policy database.

## Overview

Use these constants when creating or modifying a rule in the policy database using the [AuthorizationRightSet](<authorizationrightset(____________).md>) function.

## Topics

### Constants

- [kAuthorizationRightRule](kauthorizationrightrule.md) — Indicates a rule delegation key.
- [kAuthorizationRuleIsAdmin](kauthorizationruleisadmin.md) — Indicates a delegate rule definition constant specifying that the user must be an administrator.
- [kAuthorizationRuleAuthenticateAsAdmin](kauthorizationruleauthenticateasadmin.md) — Indicates a delegate rule definition constant specifying that the user must authenticate as an administrator.
- [kAuthorizationRuleAuthenticateAsSessionUser](kauthorizationruleauthenticateassessionuser.md) — Indicates a delegate rule definition constant specifying that the user must authenticate as the session owner (logged-in user).
- [kAuthorizationRuleClassAllow](kauthorizationruleclassallow.md) — Indicates a delegate rule definition constant that always allows the specified right.
- [kAuthorizationRuleClassDeny](kauthorizationruleclassdeny.md) — Indicates a delegate rule definition constant that always denies the specified right.
- [kAuthorizationComment](kauthorizationcomment.md) — Indicates comments for a rule.

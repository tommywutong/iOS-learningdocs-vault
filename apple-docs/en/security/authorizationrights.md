---
title: AuthorizationRights
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationrights
source_url: 'https://developer.apple.com/documentation/security/authorizationrights'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationrights.json'
content_hash: 'sha256:81d37b9521063787'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationRights

<sub>Type Alias</sub>

An authorization item set designated to represent a set of rights.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias AuthorizationRights = AuthorizationItemSet
```

## Discussion

The argument value of each item in the set is as defined for the specific right it belongs to. Argument values may not contain pointers so they remain portable between different address spaces. This set is actually an instance of an [AuthorizationItemSet](authorizationitemset.md).

---
title: AuthorizationEnvironment
framework: Security
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/authorizationenvironment
source_url: 'https://developer.apple.com/documentation/security/authorizationenvironment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/authorizationenvironment.json'
content_hash: 'sha256:440208a59f3ad88b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# AuthorizationEnvironment

<sub>Type Alias</sub>

An authorization item set designated to hold environment information relevant to authorization decisions.

<sub>Mac Catalyst, macOS</sub>

```swift
typealias AuthorizationEnvironment = AuthorizationItemSet
```

## Discussion

The authorization items in the set represent data about the environment, such as user name and other information gathered during evaluation of authorization.

This set is actually an instance of an [AuthorizationItemSet](authorizationitemset.md).

---
title: kAuthorizationEnvironmentShared
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationenvironmentshared
source_url: 'https://developer.apple.com/documentation/security/kauthorizationenvironmentshared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationenvironmentshared.json'
content_hash: 'sha256:94ae492850aa754c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationEnvironmentShared

<sub>Global Variable</sub>

The type for an authorization item containing a shared right.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationEnvironmentShared: String { get }
```

## Discussion

Adding a kAuthorizationEnvironmentShared entry in the environment causes the username and password to be added to the shared credential pool of the calling application’s session. This means that further calls by other applications in this session automatically have this credential available to them.

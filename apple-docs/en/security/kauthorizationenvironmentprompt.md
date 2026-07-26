---
title: kAuthorizationEnvironmentPrompt
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationenvironmentprompt
source_url: 'https://developer.apple.com/documentation/security/kauthorizationenvironmentprompt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationenvironmentprompt.json'
content_hash: 'sha256:aa5863dd7b34dadb'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationEnvironmentPrompt

<sub>Global Variable</sub>

The type for an authorization item containing the name of the item that should be passed into the environment when specifying invocation-specific additional text.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationEnvironmentPrompt: String { get }
```

## Discussion

The value should be a localized UTF-8 string.

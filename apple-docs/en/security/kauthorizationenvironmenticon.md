---
title: kAuthorizationEnvironmentIcon
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationenvironmenticon
source_url: 'https://developer.apple.com/documentation/security/kauthorizationenvironmenticon'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationenvironmenticon.json'
content_hash: 'sha256:b1c0bcec9a540226'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationEnvironmentIcon

<sub>Global Variable</sub>

The type for an authorization item containing the name of the item that should be passed into the environment when specifying an alternate icon.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationEnvironmentIcon: String { get }
```

## Discussion

The value should be a full path to an image compatible with the NSImage class.

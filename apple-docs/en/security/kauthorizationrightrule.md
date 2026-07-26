---
title: kAuthorizationRightRule
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationrightrule
source_url: 'https://developer.apple.com/documentation/security/kauthorizationrightrule'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationrightrule.json'
content_hash: 'sha256:1b6611f93685d0c0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationRightRule

<sub>Global Variable</sub>

Indicates a rule delegation key.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationRightRule: String { get }
```

## Discussion

Instead of specifying exact behavior, some rules are shipped with the system and may be used as delegate rules. Use this with any of the delegate rule definition constants.

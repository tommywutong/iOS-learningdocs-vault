---
title: kAuthorizationComment
framework: Security
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/kauthorizationcomment
source_url: 'https://developer.apple.com/documentation/security/kauthorizationcomment'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/kauthorizationcomment.json'
content_hash: 'sha256:556416bc67bc31bc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# kAuthorizationComment

<sub>Global Variable</sub>

Indicates comments for a rule.

<sub>Mac Catalyst, macOS</sub>

```swift
var kAuthorizationComment: String { get }
```

## Discussion

The comments appear in the policy database for the administrator to understand what the rule is for. Rule comments are not the same as localized descriptions which are presented to the user.

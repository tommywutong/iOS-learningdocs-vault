---
title: SecCredentialType.default
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [macOS 10.3+（12.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/security/seccredentialtype/default
source_url: 'https://developer.apple.com/documentation/security/seccredentialtype/default'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccredentialtype/default.json'
content_hash: 'sha256:7f745ff775722847'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecCredentialType](../seccredentialtype.md)

# SecCredentialType.default

<sub>Case</sub>

The default setting for determining whether to present UI is used.

> [!warning] Deprecated
> No longer supported

<sub>macOS</sub>

```swift
case `default`
```

## Discussion

The default setting can be changed with a call to [SecKeychainSetUserInteractionAllowed](<../seckeychainsetuserinteractionallowed(__).md>).

---
title: 'init(rawValue:)'
framework: Security
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [macOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/security/seckeyusage/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/security/seckeyusage/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyusage/init%28rawvalue%3A%29.json'
content_hash: 'sha256:2b6165e25194e71d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecKeyUsage](../seckeyusage.md)

# init(rawValue:)

<sub>Initializer</sub>

Initializes a key usage structure.

<sub>macOS</sub>

```swift
init(rawValue: UInt32)
```

## Parameters

- `rawValue` — The initial value for the structure composed as the bitwise `OR` of zero or more of the defined flags.

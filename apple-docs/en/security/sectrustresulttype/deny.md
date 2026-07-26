---
title: SecTrustResultType.deny
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/deny
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/deny'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/deny.json'
content_hash: 'sha256:9693d16f6b0ee174'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.deny

<sub>Case</sub>

The user specified that the certificate should not be trusted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case deny
```

## Discussion

This value indicates that the user explicitly chose to not trust a certificate in the chain, usually by clicking the appropriate button in a certificate trust panel. Your app should _not_ trust the chain. The Keychain Access utility refers to this value as “Never Trust.”

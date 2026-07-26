---
title: SecTrustResultType.proceed
framework: Security
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.3+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/sectrustresulttype/proceed
source_url: 'https://developer.apple.com/documentation/security/sectrustresulttype/proceed'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/sectrustresulttype/proceed.json'
content_hash: 'sha256:57468b3aed2d77d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Security](../../security.md) · [SecTrustResultType](../sectrustresulttype.md)

# SecTrustResultType.proceed

<sub>Case</sub>

The user granted permission to trust the certificate for the purposes designated in the specified policies.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case proceed
```

## Discussion

This value indicates that the user explicitly chose to trust a certificate in the chain, usually by clicking a button in a certificate trust panel. Your app should trust the chain. The Keychain Access utility refers to this value as “Always Trust.”

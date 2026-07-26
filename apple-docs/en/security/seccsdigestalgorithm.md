---
title: SecCSDigestAlgorithm
framework: Security
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [Mac Catalyst 13.0+, macOS 10.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seccsdigestalgorithm
source_url: 'https://developer.apple.com/documentation/security/seccsdigestalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seccsdigestalgorithm.json'
content_hash: 'sha256:3c1bda5b8b88ca60'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecCSDigestAlgorithm

<sub>Enumeration</sub>

The list of digest algorithms available for code signatures.

<sub>Mac Catalyst, macOS</sub>

```swift
enum SecCSDigestAlgorithm
```

## Overview

Use these values with the [kSecCodeInfoDigestAlgorithm](kseccodeinfodigestalgorithm.md) and [kSecCodeInfoDigestAlgorithms](kseccodeinfodigestalgorithms.md) keys described in [Signing Information Dictionary Keys](signing-information-dictionary-keys.md).

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [kSecCodeSignatureHashSHA1](seccsdigestalgorithm/codesignaturehashsha1.md)
- [kSecCodeSignatureHashSHA256](seccsdigestalgorithm/codesignaturehashsha256.md)
- [kSecCodeSignatureHashSHA256Truncated](seccsdigestalgorithm/codesignaturehashsha256truncated.md)
- [kSecCodeSignatureHashSHA384](seccsdigestalgorithm/codesignaturehashsha384.md)
- [kSecCodeSignatureHashSHA512](seccsdigestalgorithm/codesignaturehashsha512.md)
- [kSecCodeSignatureNoHash](seccsdigestalgorithm/codesignaturenohash.md)

### Initializers

- [init(rawValue:)](<seccsdigestalgorithm/init(rawvalue_).md>)

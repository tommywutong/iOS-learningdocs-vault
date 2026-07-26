---
title: KEM.EncapsulationResult
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kem/encapsulationresult
source_url: 'https://developer.apple.com/documentation/cryptokit/kem/encapsulationresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kem/encapsulationresult.json'
content_hash: 'sha256:8c6f17e0a0471c9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEM](../kem.md)

# KEM.EncapsulationResult

<sub>Structure</sub>

The result of a key encapsulation operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct EncapsulationResult
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(sharedSecret:encapsulated:)](<encapsulationresult/init(sharedsecret_encapsulated_).md>) — Initializes a key encapsulation result.

### Instance Properties

- [encapsulated](encapsulationresult/encapsulated.md) — The encapsulated representation of the shared secret.
- [sharedSecret](encapsulationresult/sharedsecret.md) — The shared secret.

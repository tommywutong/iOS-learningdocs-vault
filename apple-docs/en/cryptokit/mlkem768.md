---
title: MLKEM768
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/mlkem768
source_url: 'https://developer.apple.com/documentation/cryptokit/mlkem768'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/mlkem768.json'
content_hash: 'sha256:e636751a0ea9018e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# MLKEM768

<sub>Enumeration</sub>

The Module-Lattice key encapsulation mechanism (KEM).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum MLKEM768
```

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Keys

- [PrivateKey](mlkem768/privatekey.md) — A private key you use to decapsulate shared secrets with the Module-Lattice key encapsulation mechanism.
- [PublicKey](mlkem768/publickey.md) — A public key you use to encapsulate shared secrets with the Module-Lattice key encapsulation mechanism.

### Structures

- [OneTimePrivateKey](mlkem768/onetimeprivatekey.md) _(beta)_

## See Also

### Key encapsulation mechanisms (KEM)

- [KEM](kem.md) — A key encapsulation mechanism.
- [MLKEM1024](mlkem1024.md) — The Module-Lattice key encapsulation mechanism (KEM).
- [XWingMLKEM768X25519](xwingmlkem768x25519.md) — The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06

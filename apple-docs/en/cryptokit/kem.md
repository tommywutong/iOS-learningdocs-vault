---
title: KEM
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kem
source_url: 'https://developer.apple.com/documentation/cryptokit/kem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kem.json'
content_hash: 'sha256:3422e2dc5b94006d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# KEM

<sub>Enumeration</sub>

A key encapsulation mechanism.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KEM
```

## Overview

Use a key encapsulation mechanism (KEM) to protect a symmetric cryptographic key that you share with another party.

## Relationships

- **Conforms To**: [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Defining encapsulation outputs

- [EncapsulationResult](kem/encapsulationresult.md) — The result of a key encapsulation operation.

### Handling errors

- [Errors](kem/errors.md) — Errors that CryptoKit throws when it encounters problems in key encapsulation mechanism (KEM) operations.

## See Also

### Key encapsulation mechanisms (KEM)

- [MLKEM768](mlkem768.md) — The Module-Lattice key encapsulation mechanism (KEM).
- [MLKEM1024](mlkem1024.md) — The Module-Lattice key encapsulation mechanism (KEM).
- [XWingMLKEM768X25519](xwingmlkem768x25519.md) — The X-Wing (ML-KEM768 with X25519) Key Encapsulation Mechanism, defined in https://datatracker.ietf.org/doc/html/draft-connolly-cfrg-xwing-kem-06

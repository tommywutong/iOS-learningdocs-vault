---
title: HPKE.Errors
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/errors
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/errors.json'
content_hash: 'sha256:a876ccefb7c54d50'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKE](../hpke.md)

# HPKE.Errors

<sub>Enumeration</sub>

Hybrid public key encryption (HPKE) errors that CryptoKit uses.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Errors
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [HPKE.Errors.ciphertextTooShort](errors/ciphertexttooshort.md) — The ciphertext is too short.
- [HPKE.Errors.expectedPSK](errors/expectedpsk.md) — The PSK is nil and the object is in PSK mode, or in authentication and PSK mode.
- [HPKE.Errors.exportOnlyMode](errors/exportonlymode.md) — The object is in export-only mode and received a request to encrypt or decrypt data.
- [HPKE.Errors.inconsistentCiphersuiteAndKey](errors/inconsistentciphersuiteandkey.md) — The supplied encryption key is incompatible with the requested cipher suite.
- [HPKE.Errors.inconsistentPSKInputs](errors/inconsistentpskinputs.md) — The PSK is nil and the PSK ID isn’t nil, or the PSK ID is nil and the PSK isn’t nil.
- [HPKE.Errors.inconsistentParameters](errors/inconsistentparameters.md) — The parameters for initializing an HPKE sender or receiver are inconsistent.
- [HPKE.Errors.outOfRangeSequenceNumber](errors/outofrangesequencenumber.md) — The sequence number for encrypting or decrypting the message is out of range.
- [HPKE.Errors.unexpectedPSK](errors/unexpectedpsk.md) — The PSK isn’t nil and the object is in base mode, or in authentication mode.

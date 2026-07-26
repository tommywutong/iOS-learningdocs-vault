---
title: KEM.Errors
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/kem/errors
source_url: 'https://developer.apple.com/documentation/cryptokit/kem/errors'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/kem/errors.json'
content_hash: 'sha256:af39d72d4e79fd5d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [KEM](../kem.md)

# KEM.Errors

<sub>Enumeration</sub>

Errors that CryptoKit throws when it encounters problems in key encapsulation mechanism (KEM) operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Errors
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Enumeration Cases

- [KEM.Errors.invalidSeed](errors/invalidseed.md) — The seed value supplied for deriving a key isn’t valid.
- [KEM.Errors.publicKeyMismatchDuringInitialization](errors/publickeymismatchduringinitialization.md) — The public key CryptoKit receives when it initializes a key encapsulation operation doesn’t match the expected value.

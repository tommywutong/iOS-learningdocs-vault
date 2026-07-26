---
title: AES.KeyWrap
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/keywrap
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/keywrap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/keywrap.json'
content_hash: 'sha256:f1f34eac4eeaf323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [AES](../aes.md)

# AES.KeyWrap

<sub>Enumeration</sub>

An implementation of AES Key Wrapping in accordance with the IETF RFC 3394 specification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum KeyWrap
```

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Wrapping an AES key

- [wrap(_:using:)](<keywrap/wrap(__using_).md>) — Wraps a key using the AES wrap algorithm.

### Unwrapping an AES key

- [unwrap(_:using:)](<keywrap/unwrap(__using_).md>) — Unwraps a key using the AES wrap algorithm.

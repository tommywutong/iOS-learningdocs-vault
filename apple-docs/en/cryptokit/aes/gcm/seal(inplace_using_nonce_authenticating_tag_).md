---
title: 'seal(inPlace:using:nonce:authenticating:tag:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/seal(inplace:using:nonce:authenticating:tag:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/seal(inplace:using:nonce:authenticating:tag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/seal%28inplace%3Ausing%3Anonce%3Aauthenticating%3Atag%3A%29.json'
content_hash: 'sha256:11c71b6eaf5d87a6'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [GCM](../gcm.md)

# seal(inPlace:using:nonce:authenticating:tag:)

<sub>Type Method</sub>

Secures the given plaintext message with encryption and an optional authentication tag.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func seal(inPlace message: inout MutableRawSpan, using key: SymmetricKey, nonce: AES.GCM.Nonce, authenticating authenticatedData: RawSpan? = nil, tag: inout OutputRawSpan) throws
```

## Parameters

- `message` — The plaintext data to seal, which will be updated in place.

- `key` — A cryptographic key used to seal the message.

- `nonce` — The nonce the sealing process requires.

- `authenticatedData` — Additional data to be authenticated, if provided.

- `tag` — Receives the 16-byte authentication tag

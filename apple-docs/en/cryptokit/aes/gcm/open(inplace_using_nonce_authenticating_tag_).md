---
title: 'open(inPlace:using:nonce:authenticating:tag:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/open(inplace:using:nonce:authenticating:tag:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/open(inplace:using:nonce:authenticating:tag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/open%28inplace%3Ausing%3Anonce%3Aauthenticating%3Atag%3A%29.json'
content_hash: 'sha256:37641bc261c39f15'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [GCM](../gcm.md)

# open(inPlace:using:nonce:authenticating:tag:)

<sub>Type Method</sub>

Decrypts the message and verifies its authenticity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func open(inPlace message: inout MutableRawSpan, using key: SymmetricKey, nonce: AES.GCM.Nonce, authenticating authenticatedData: RawSpan? = nil, tag: RawSpan) throws
```

## Parameters

- `message` — The message, which will be decrypted in place.

- `key` — The cryptographic key that was used to seal the message.

- `nonce` — The nonce used to encrypt the message.

- `authenticatedData` — Additional data that was authenticated.

## Discussion

The call throws an error if decryption or authentication fail.

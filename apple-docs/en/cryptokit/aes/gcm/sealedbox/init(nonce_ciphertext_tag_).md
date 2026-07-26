---
title: 'init(nonce:ciphertext:tag:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/aes/gcm/sealedbox/init(nonce:ciphertext:tag:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox/init(nonce:ciphertext:tag:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/sealedbox/init%28nonce%3Aciphertext%3Atag%3A%29.json'
content_hash: 'sha256:74da5a1e4bee6113'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [Apple CryptoKit](../../../../cryptokit.md) · [AES](../../../aes.md) · [GCM](../../gcm.md) · [SealedBox](../sealedbox.md)

# init(nonce:ciphertext:tag:)

<sub>Initializer</sub>

Creates a sealed box from the given tag, nonce, and ciphertext.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<C, T>(nonce: AES.GCM.Nonce, ciphertext: C, tag: T) throws where C : DataProtocol, T : DataProtocol
```

## Parameters

- `nonce` — The nonce.

- `ciphertext` — The encrypted data.

- `tag` — The authentication tag.

## See Also

### Creating the sealed box

- [init(combined:)](<init(combined_).md>) — Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.

---
title: AES.GCM.SealedBox
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/aes/gcm/sealedbox
source_url: 'https://developer.apple.com/documentation/cryptokit/aes/gcm/sealedbox'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/aes/gcm/sealedbox.json'
content_hash: 'sha256:a508c46d27b27d41'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [AES](../../aes.md) · [GCM](../gcm.md)

# AES.GCM.SealedBox

<sub>Structure</sub>

A secure container for your data that you can access using a cipher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SealedBox
```

## Overview

Use a sealed box as a container for data that you want to transmit securely. Seal data into a box with one of the cipher algorithms, like [seal(_:using:nonce:)](<seal(__using_nonce_).md>).

The box holds an encrypted version of the original data, an authentication tag, and the nonce during encryption. The encryption makes the data unintelligible to anyone without the key, while the authentication tag makes it possible for the intended receiver to be sure the data remains intact.

The receiver uses another instance of the same cipher, like the [open(_:using:)](<open(__using_).md>) method, to open the box.

## Relationships

- **Conforms To**: [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating the sealed box

- [init(nonce:ciphertext:tag:)](<sealedbox/init(nonce_ciphertext_tag_).md>) — Creates a sealed box from the given tag, nonce, and ciphertext.
- [init(combined:)](<sealedbox/init(combined_).md>) — Creates a sealed box from the combined bytes of an authentication tag, nonce, and encrypted data.

### Retrieving the combined contents

- [combined](sealedbox/combined.md) — A combined element composed of the nonce, encrypted data, and authentication tag.

### Inspecting the component elements

- [nonce](sealedbox/nonce.md) — The nonce used to encrypt the data.
- [ciphertext](sealedbox/ciphertext.md) — The encrypted data.
- [tag](sealedbox/tag.md) — An authentication tag.

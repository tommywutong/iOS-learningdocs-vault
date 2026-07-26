---
title: 'seal(_:authenticating:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/seal(_:authenticating:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/seal(_:authenticating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/seal%28_%3Aauthenticating%3A%29.json'
content_hash: 'sha256:8b097657ca2ff5fd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# seal(_:authenticating:)

<sub>Instance Method</sub>

Encrypts the given cleartext message and attaches additional authenticated data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func seal<M, AD>(_ msg: M, authenticating aad: AD) throws -> Data where M : DataProtocol, AD : DataProtocol
```

## Parameters

- `msg` — The cleartext message to encrypt.

- `aad` — Additional data that the `Sender` authenticates and adds to the message in cleartext.

## Return Value

The ciphertext for the recipient to decrypt.

## Discussion

You can call this method multiple times to encrypt a series of messages. When using this method, you need to supply ciphertext messages to the decryption code on the receiving side in the same order as you encrypt them.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

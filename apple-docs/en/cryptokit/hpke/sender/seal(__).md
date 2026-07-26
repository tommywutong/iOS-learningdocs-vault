---
title: 'seal(_:)'
framework: Apple CryptoKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/seal(_:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/seal(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/seal%28_%3A%29.json'
content_hash: 'sha256:92315c5d03c16bc7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# seal(_:)

<sub>Instance Method</sub>

Encrypts the given cleartext message.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func seal<M>(_ msg: M) throws -> Data where M : DataProtocol
```

## Parameters

- `msg` — The cleartext message to encrypt.

## Return Value

The ciphertext for the recipient to decrypt.

## Discussion

You can call this method multiple times to encrypt a series of messages. When using this method, you need to supply ciphertext messages to the decryption code on the receiving side in the same order as you encrypt them.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

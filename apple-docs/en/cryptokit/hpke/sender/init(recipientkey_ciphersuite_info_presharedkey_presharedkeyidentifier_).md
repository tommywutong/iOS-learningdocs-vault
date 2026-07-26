---
title: 'init(recipientKey:ciphersuite:info:presharedKey:presharedKeyIdentifier:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:presharedkey:presharedkeyidentifier:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:presharedkey:presharedkeyidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/init%28recipientkey%3Aciphersuite%3Ainfo%3Apresharedkey%3Apresharedkeyidentifier%3A%29.json'
content_hash: 'sha256:5a03571bee0ecbc1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# init(recipientKey:ciphersuite:info:presharedKey:presharedKeyIdentifier:)

<sub>Initializer</sub>

Creates a sender in preshared key (PSK) mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data, presharedKey psk: SymmetricKey, presharedKeyIdentifier pskID: Data) throws where PK : HPKEDiffieHellmanPublicKey
```

## Parameters

- `recipientKey` — The recipient’s public key for encrypting the messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `psk` — A preshared key (PSK) that the sender and the recipient both hold.

- `pskID` — An identifier for the PSK.

## Discussion

The `Sender` encrypts messages in PSK mode using a symmetric encryption key that the sender and recipient both know in advance, in combination with a key it derives using a key derivation function (KDF) and the key schedule data in `info`. The `Sender` encapsulates the derived key using the recipient’s public key. You access the encapsulated key using [encapsulatedKey](encapsulatedkey.md).

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

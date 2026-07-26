---
title: 'init(recipientKey:ciphersuite:info:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:)-56p88'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender/init(recipientkey:ciphersuite:info:)-56p88'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender/init%28recipientkey%3Aciphersuite%3Ainfo%3A%29-56p88.json'
content_hash: 'sha256:0c9d2aa1dab2cb4d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Sender](../sender.md)

# init(recipientKey:ciphersuite:info:)

<sub>Initializer</sub>

Creates a sender in base mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<PK>(recipientKey: PK, ciphersuite: HPKE.Ciphersuite, info: Data) throws where PK : HPKEDiffieHellmanPublicKey
```

## Parameters

- `recipientKey` — The recipient’s public key for encrypting the messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

## Discussion

The `Sender` encrypts messages in base mode with a symmetric encryption key it derives using a key derivation function (KDF). The KDF uses the key schedule data in `info` as input to generate the key. The `Sender` encapsulates the derived key using the recipient’s public key. You access the encapsulated key using [encapsulatedKey](encapsulatedkey.md).

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

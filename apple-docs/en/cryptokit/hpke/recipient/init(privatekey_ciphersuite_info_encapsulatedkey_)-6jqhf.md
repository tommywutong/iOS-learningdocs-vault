---
title: 'init(privateKey:ciphersuite:info:encapsulatedKey:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:)-6jqhf'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:)-6jqhf'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/recipient/init%28privatekey%3Aciphersuite%3Ainfo%3Aencapsulatedkey%3A%29-6jqhf.json'
content_hash: 'sha256:9cb221d6e2518c42'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Recipient](../recipient.md)

# init(privateKey:ciphersuite:info:encapsulatedKey:)

<sub>Initializer</sub>

Creates a recipient in base mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data) throws where SK : HPKEDiffieHellmanPrivateKey
```

## Parameters

- `privateKey` — The recipient’s private key for decrypting the incoming messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `encapsulatedKey` — The encapsulated symmetric key that the sender provides.

## Discussion

The `Receiver` decrypts messages in base mode using the encapsulated key with the key schedule information (`info` data).

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

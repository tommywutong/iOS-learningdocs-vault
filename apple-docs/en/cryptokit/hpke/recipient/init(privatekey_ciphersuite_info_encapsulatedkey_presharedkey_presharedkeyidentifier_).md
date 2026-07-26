---
title: 'init(privateKey:ciphersuite:info:encapsulatedKey:presharedKey:presharedKeyIdentifier:)'
framework: Apple CryptoKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:presharedkey:presharedkeyidentifier:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/recipient/init(privatekey:ciphersuite:info:encapsulatedkey:presharedkey:presharedkeyidentifier:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/recipient/init%28privatekey%3Aciphersuite%3Ainfo%3Aencapsulatedkey%3Apresharedkey%3Apresharedkeyidentifier%3A%29.json'
content_hash: 'sha256:69ea75ab76e3a85b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Apple CryptoKit](../../../cryptokit.md) · [HPKE](../../hpke.md) · [Recipient](../recipient.md)

# init(privateKey:ciphersuite:info:encapsulatedKey:presharedKey:presharedKeyIdentifier:)

<sub>Initializer</sub>

Creates a recipient in preshared key (PSK) mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<SK>(privateKey: SK, ciphersuite: HPKE.Ciphersuite, info: Data, encapsulatedKey: Data, presharedKey psk: SymmetricKey, presharedKeyIdentifier pskID: Data) throws where SK : HPKEDiffieHellmanPrivateKey
```

## Parameters

- `privateKey` — The recipient’s private key for decrypting the incoming messages.

- `ciphersuite` — The cipher suite that defines the cryptographic algorithms to use.

- `info` — Data that the key derivation function uses to compute the symmetric key material. The sender and the recipient need to use the same `info` data.

- `encapsulatedKey` — The encapsulated symmetric key that the sender provides.

- `psk` — A preshared key (PSK) that the sender and the recipient both hold.

- `pskID` — An identifier for the PSK.

## Discussion

The `Receiver` decrypts messages in PSK mode using the encapsulated key with the key schedule information (`info` data), in addition to a symmetric encryption key that the sender and recipient both know in advance.

> [!note] Note
> The system throws errors from [Errors](../errors.md) when it encounters them.

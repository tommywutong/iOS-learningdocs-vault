---
title: HPKE.Recipient
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/recipient
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/recipient'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/recipient.json'
content_hash: 'sha256:4c5e34bf46e12a3a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKE](../hpke.md)

# HPKE.Recipient

<sub>Structure</sub>

A type that represents the receiving side of an HPKE message exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Recipient
```

## Overview

To decrypt and verify the identity of encrypted messages, initialize a `Recipient` specifying the appropriate cipher suite, the receiver’s private key, the encapsulated symmetric key, and the additional cryptographic material relevant to your chosen mode of operation. Call [open(_:)](<recipient/open(__).md>) or [open(_:authenticating:)](<recipient/open(__authenticating_).md>) on the `Recipient` instance for each message in turn to retrieve its cleartext. The recipient of the messages needs to process them in the same order as the `Sender`, using the same cipher suite, encryption mode, and key schedule information (`info` data). Use a separate `Recipient` instance for each stream of messages.

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(privateKey:ciphersuite:info:encapsulatedKey:)](<recipient/init(privatekey_ciphersuite_info_encapsulatedkey_)-6jqhf.md>) — Creates a recipient in base mode.
- [init(privateKey:ciphersuite:info:encapsulatedKey:)](<recipient/init(privatekey_ciphersuite_info_encapsulatedkey_)-7v86b.md>) — Creates a recipient in base mode.
- [init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:)](<recipient/init(privatekey_ciphersuite_info_encapsulatedkey_authenticatedby_).md>) — Creates a recipient in authentication mode.
- [init(privateKey:ciphersuite:info:encapsulatedKey:authenticatedBy:presharedKey:presharedKeyIdentifier:)](<recipient/init(privatekey_ciphersuite_info_encapsulatedkey_authenticatedby_presharedkey_presharedkeyidentifier_).md>) — Creates a recipient in authentication and preshared key mode.
- [init(privateKey:ciphersuite:info:encapsulatedKey:presharedKey:presharedKeyIdentifier:)](<recipient/init(privatekey_ciphersuite_info_encapsulatedkey_presharedkey_presharedkeyidentifier_).md>) — Creates a recipient in preshared key (PSK) mode.

### Instance Methods

- [exportSecret(context:outputByteCount:)](<recipient/exportsecret(context_outputbytecount_).md>) — Exports a secret given domain-separation context and the desired output length.
- [open(_:)](<recipient/open(__).md>) — Decrypts a message, if the ciphertext is valid.
- [open(_:authenticating:)](<recipient/open(__authenticating_).md>) — Decrypts a message, if the ciphertext is valid, verifying the integrity of additional authentication data.

## See Also

### Sending and receiving messages

- [Sender](sender.md) — A type that represents the sending side of an HPKE message exchange.

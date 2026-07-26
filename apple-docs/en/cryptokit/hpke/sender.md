---
title: HPKE.Sender
framework: Apple CryptoKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/hpke/sender
source_url: 'https://developer.apple.com/documentation/cryptokit/hpke/sender'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/hpke/sender.json'
content_hash: 'sha256:20eccc0bdabe19d6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [HPKE](../hpke.md)

# HPKE.Sender

<sub>Structure</sub>

A type that represents the sending side of an HPKE message exchange.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Sender
```

## Overview

To create encrypted messages, initialize a `Sender` specifying the appropriate cipher suite, the recipient’s public key, and the additional cryptographic material relevant to your chosen mode of operation. Call [seal(_:)](<sender/seal(__).md>) or [seal(_:authenticating:)](<sender/seal(__authenticating_).md>) on the `Sender` instance for each message in turn to retrieve its ciphertext. The recipient of the messages needs to process them in the same order as the `Sender`, using the same encryption mode, cipher suite, and key schedule information (`info`), as well as the `Sender`’s [encapsulatedKey](sender/encapsulatedkey.md).

## Relationships

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Initializers

- [init(recipientKey:ciphersuite:info:)](<sender/init(recipientkey_ciphersuite_info_)-56p88.md>) — Creates a sender in base mode.
- [init(recipientKey:ciphersuite:info:)](<sender/init(recipientkey_ciphersuite_info_)-swk5.md>) — Creates a sender in base mode.
- [init(recipientKey:ciphersuite:info:authenticatedBy:)](<sender/init(recipientkey_ciphersuite_info_authenticatedby_).md>) — Creates a sender in authentication mode.
- [init(recipientKey:ciphersuite:info:authenticatedBy:presharedKey:presharedKeyIdentifier:)](<sender/init(recipientkey_ciphersuite_info_authenticatedby_presharedkey_presharedkeyidentifier_).md>) — Creates a sender in authentication and preshared key mode.
- [init(recipientKey:ciphersuite:info:presharedKey:presharedKeyIdentifier:)](<sender/init(recipientkey_ciphersuite_info_presharedkey_presharedkeyidentifier_).md>) — Creates a sender in preshared key (PSK) mode.

### Instance Properties

- [encapsulatedKey](sender/encapsulatedkey.md) — The encapsulated symmetric key that the recipient uses to decrypt messages.

### Instance Methods

- [exportSecret(context:outputByteCount:)](<sender/exportsecret(context_outputbytecount_).md>) — Exports a secret given domain-separation context and the desired output length.
- [seal(_:)](<sender/seal(__).md>) — Encrypts the given cleartext message.
- [seal(_:authenticating:)](<sender/seal(__authenticating_).md>) — Encrypts the given cleartext message and attaches additional authenticated data.

## See Also

### Sending and receiving messages

- [Recipient](recipient.md) — A type that represents the receiving side of an HPKE message exchange.

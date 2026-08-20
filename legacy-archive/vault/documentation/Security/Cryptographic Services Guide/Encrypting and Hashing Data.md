---
title: Cryptographic Services Guide
apple_id: TP40011172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/GeneralPurposeCrypto/GeneralPurposeCrypto.html
archived_at: '2026-07-18T02:06:48.039729Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cryptographic Services Guide](About%20Cryptographic%20Services.md)


[Next](Managing%20Keys%2C%20Certificates%2C%20and%20Passwords.md)[Previous](Cryptography%20Concepts%20In%20Depth.md)

# Encrypting and Hashing Data

You typically use asymmetric encryption for sending data across trust boundaries, such as one person sending another person an encrypted email. You also use it for sending a symmetric session key across an insecure communication channel so that you can then use symmetric encryption in further communication. On the other hand, you often use symmetric encryption for data at rest—on your hard drive, for example—and as a session key in a number of encrypted networking schemes.

macOS and iOS provide a number of encryption technologies, including:

- __Keychain Services.__ Use this API, described in _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_, to encrypt and store passwords, keys, and other small secrets in a special database called a keychain. By storing user secrets this way, you ensure that they are kept secure, including in device backups, without having to implement your own encryption algorithms or storage protocols. On a Mac, you can use the Keychain Access app to inspect keychains, as described in [Keychain Access](../Security%20Overview/End-User%20Security%20Features.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzwfvbuqmrqgqwugscejfdeor2d) in _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_.
- __Certificate, Key, and Trust Services.__ This interface provides cryptographic support services, including methods for general encryption and decryption, as well as trust validation. See _[Certificate, Key, and Trust Services Reference](https://developer.apple.com/documentation/security/certificate_key_and_trust_services)_ for details.
- __Cryptographic Message Syntax.__ Use this service to encrypt or add a digital signature to S/MIME messages. S/MIME is a standard for encrypting and signing messages, most commonly used with email. See _[Cryptographic Message Syntax Services Reference](https://developer.apple.com/documentation/security/cryptographic_message_syntax_services)_ for more information.

macOS provides a few additional APIs for performing encryption:

- __Security Transforms API.__ Based on the concept of data flow programming, the Security Transforms API lets you construct graphs of transformations that feed into one another, transparently using Grand Central Dispatch to schedule the resulting work efficiently across multiple CPUs. As the data objects pass through the object graph, callbacks within each individual transform operate on that data, then pass it on to the transform’s output, which may be connected to the input of another transform object, and so on.

  Using the built-in transforms, the Security Transforms API allows you to read files, perform symmetric encryption and decryption, perform asymmetric signing and verifying, and perform Base64 encoding. The Security Transforms API also provides support for creating custom transforms that perform other operations on data. For example, you might create a transform that byte swaps data prior to encrypting it or a transform that encodes the resulting encrypted data for transport.

  For more information, see _Security Transforms Reference_.
- __CDSA/CSSM.__ This open source security architecture provides a wide array of security services, including fine-grained access permissions, authentication of users’ identities, encryption, and secure data storage. However, this interface is deprecated starting in macOS 10.7, and should not be used for any new apps.

[Next](Managing%20Keys%2C%20Certificates%2C%20and%20Passwords.md)[Previous](Cryptography%20Concepts%20In%20Depth.md)


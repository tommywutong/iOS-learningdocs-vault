---
title: Cryptographic Services Guide
apple_id: TP40011172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html
archived_at: '2026-07-18T02:06:48.112310Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md)


[Next](Cryptography%20Concepts%20In%20Depth.md)

# About Cryptographic Services

macOS and iOS contain a number of technologies that provide cryptographic services—encryption and decryption, hashing, random number generation, secure network communication, and so on. These technologies can be used to secure data at rest (when stored on your hard drive or other media), secure data in transit, determine the identity of a third party, and build additional security technologies.

![../Art/CrytoServices-IntroArt-120412_2x.png](attachments/Art/CrytoServices-IntroArt-120412_2x.png)![../Art/CrytoServices-IntroArt-120412_2x.png](attachments/Art/CrytoServices-IntroArt-120412_2x.png)

Some of the cryptographic services provided by iOS and macOS include:

- Encryption and decryption (both general-purpose and special-purpose)
- Key management using keychains
- Cryptographically strong random number generation
- Secure communication (SSL and TLS)
- Secure storage using FileVault and iOS File Protection

### Encryption, Signing and Verifying, and Digital Certificates Can Protect Data from Prying Eyes

There are two main types of encryption: symmetric encryption, in which a single shared key is used for encrypting and decrypting data, and asymmetric encryption, in which you use one key to encrypt data and a separate (but related) key to decrypt the data. You can use a hash to detect modifications to a piece of data. You can combine hashes with asymmetric keys to create a digital signature that, when verified against a digital certificate, proves the source of a piece of data. Digital certificates, in turn, are verified by verifying the signature of the party that signed the certificate, then verifying that party’s certificate, and so on until you reach a certificate that you trust inherently, called an _anchor certificate_.

### macOS and iOS Provide Encryption and Hashing APIs

macOS and iOS provide a number of APIs for encrypting and hashing data, including Keychain Services; Cryptographic Message Syntax Services; Certificate, Key, and Trust Services; and Security Transforms.

### Keychains Help You Store Secret Information

If your app stores encryption keys, passwords, certificates, and other security-related information, use a keychain. Keychains provide secure storage for small pieces of information so that is not accessible by other apps running on the system, and so that it is accessible only after the user has logged in or unlocked the device. macOS and iOS provide two APIs for working with the keychain and keys obtained from the keychain: Certificate, Key, and Trust Services and Keychain Services.

### macOS and iOS Provide Cryptographically Secure Random Number Generation

Some cryptographic tasks require you to generate cryptographically strong pseudorandom numbers. Use the Randomization Services API to generate these numbers.

### macOS and iOS Provide Secure Network Communication APIs

Transmitting data securely requires a secure communications channel. macOS and iOS provide a number of APIs for establishing secure communications channels, including the URL Loading System, socket streams in Core Foundation and Foundation, and Secure Transport.

### Deprecated Technologies

Although the CDSA and CSSM API is deprecated in macOS 10.7 and later, its documentation is provided as an appendix.

Before reading this document, you should be familiar with the concepts in _[Security Overview](../Security%20Overview/About%20Software%20Security.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridgmbqgaydsnzw)_ and _[Secure Coding Guide](../Secure%20Coding%20Guide/Introduction%20to%20Secure%20Coding%20Guide.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgazdimjv)_.

For more information about macOS authentication and authorization (built on top of encryption technologies), read _[Authentication, Authorization, and Permissions Guide](../Authentication%2C%20Authorization%2C%20and%20Permissions%20Guide/About%20Authentication%2C%20Authorization%2C%20and%20Permissions.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqgeytembq)_.

[Next](Cryptography%20Concepts%20In%20Depth.md)


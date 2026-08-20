---
title: Cryptographic Services Guide
apple_id: TP40011172
resource_type: Guide
platform: tvOS|iOS|macOS
topic: Security
technology: Security
published: '2018-06-04'
source_url: https://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/KeyManagementAPIs/KeyManagementAPIs.html
archived_at: '2026-07-18T02:06:48.443793Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Cryptographic Services Guide](About%20Cryptographic%20Services.md)


[Next](Generating%20Random%20Numbers.md)[Previous](Encrypting%20and%20Hashing%20Data.md)

# Managing Keys, Certificates, and Passwords

The _keychain_ provides storage for passwords, encryption keys, certificates, and other small pieces of data. Some of these items are inherently secret, like private keys and passwords, while others are not, such as certificates. After storing data in the keychain, you can be confident that untrusted apps cannot access that data. Further, device backups contain only encrypted versions of the secret data.

Use the following APIs to work with keychain items:

- __Keychain Services.__ Use Keychain Services to explicitly add, delete, and edit keychain items, and—in macOS only—manage collections of keychains. See _[Keychain Services Reference](https://developer.apple.com/documentation/security/keychain_services)_ for details.
- __Certificate, Key, and Trust Services.__ Manage certificates, public and private keys, symmetric keys, and trust policies. In particular, you can:

  - Create certificates and asymmetric keys.
  - Add certificates and keys to keychains.
  - Retrieve information about a certificate, such as the private key associated with it, the owner, and so on.
  - Convert certificates to and from portable representations.
  - Create and manipulate trust policies and evaluate a specific certificate using a specified set of trust policies.
  - Add anchor certificates.
  - Generate or verify a digital signature for a block of data.
  - Encrypt or decrypt a block of data.

  Certificate, Key, and Trust Services operates on certificates that conform to the X.509 ITU standard, uses the keychain for storage and retrieval of certificates and keys, and uses the trust policies provided by Apple. See _[Certificate, Key, and Trust Services Reference](https://developer.apple.com/documentation/security/certificate_key_and_trust_services)_ for more information.
- __Security Interface.__ To display the contents of a certificate in an macOS user interface, you can use the [SFCertificatePanel](https://developer.apple.com/documentation/securityinterface/sfcertificatepanel) and [SFCertificateView](https://developer.apple.com/documentation/securityinterface/sfcertificateview) classes. In addition, the [SFCertificateTrustPanel](https://developer.apple.com/documentation/securityinterface/sfcertificatetrustpanel) class displays trust decisions and lets the user edit trust decisions.

[Next](Generating%20Random%20Numbers.md)[Previous](Encrypting%20and%20Hashing%20Data.md)


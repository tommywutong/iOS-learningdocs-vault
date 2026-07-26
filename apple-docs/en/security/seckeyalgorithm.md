---
title: SecKeyAlgorithm
framework: Security
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/security/seckeyalgorithm
source_url: 'https://developer.apple.com/documentation/security/seckeyalgorithm'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/security/seckeyalgorithm.json'
content_hash: 'sha256:29eef33cf6e1df91'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Security](../security.md)

# SecKeyAlgorithm

<sub>Structure</sub>

The algorithms that cryptographic keys enable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct SecKeyAlgorithm
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Elliptic curve encryption standard X963

- [kSecKeyAlgorithmECIESEncryptionStandardX963SHA1AESGCM](seckeyalgorithm/eciesencryptionstandardx963sha1aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardX963SHA224AESGCM](seckeyalgorithm/eciesencryptionstandardx963sha224aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardX963SHA256AESGCM](seckeyalgorithm/eciesencryptionstandardx963sha256aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardX963SHA384AESGCM](seckeyalgorithm/eciesencryptionstandardx963sha384aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardX963SHA512AESGCM](seckeyalgorithm/eciesencryptionstandardx963sha512aesgcm.md)

### Elliptic curve encryption standard variable IVX963

- [kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA224AESGCM](seckeyalgorithm/eciesencryptionstandardvariableivx963sha224aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA256AESGCM](seckeyalgorithm/eciesencryptionstandardvariableivx963sha256aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA384AESGCM](seckeyalgorithm/eciesencryptionstandardvariableivx963sha384aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionStandardVariableIVX963SHA512AESGCM](seckeyalgorithm/eciesencryptionstandardvariableivx963sha512aesgcm.md)

### Elliptic curve encryption cofactor variable IVX963

- [kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA224AESGCM](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha224aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA256AESGCM](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha256aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA384AESGCM](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha384aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorVariableIVX963SHA512AESGCM](seckeyalgorithm/eciesencryptioncofactorvariableivx963sha512aesgcm.md)

### Elliptic curve encryption cofactor X963

- [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA1AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha1aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA224AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha224aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA256AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha256aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA384AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha384aesgcm.md)
- [kSecKeyAlgorithmECIESEncryptionCofactorX963SHA512AESGCM](seckeyalgorithm/eciesencryptioncofactorx963sha512aesgcm.md)

### Elliptic curve signature RFC4754

- [kSecKeyAlgorithmECDSASignatureRFC4754](seckeyalgorithm/ecdsasignaturerfc4754.md) _(deprecated)_

### Elliptic curve signature digest RFC4754

- [kSecKeyAlgorithmECDSASignatureDigestRFC4754](seckeyalgorithm/ecdsasignaturedigestrfc4754.md) — An algorithm for generating message digest signatures.
- [kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA1](seckeyalgorithm/ecdsasignaturedigestrfc4754sha1.md) — An algorithm for generating signatures of SHA1 message digests.
- [kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA224](seckeyalgorithm/ecdsasignaturedigestrfc4754sha224.md) — An algorithm for generating signatures of SHA224 message digests.
- [kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA256](seckeyalgorithm/ecdsasignaturedigestrfc4754sha256.md) — An algorithm for generating signatures of SHA256 message digests.
- [kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA384](seckeyalgorithm/ecdsasignaturedigestrfc4754sha384.md) — An algorithm for generating signatures of SHA384 message digests.
- [kSecKeyAlgorithmECDSASignatureDigestRFC4754SHA512](seckeyalgorithm/ecdsasignaturedigestrfc4754sha512.md) — An algorithm for generating signatures of SHA512 message digests.

### Elliptic curve signature message RFC4754

- [kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA1](seckeyalgorithm/ecdsasignaturemessagerfc4754sha1.md) — An algorithm for generating message signatures by calculating and signing the SHA1 message digest.
- [kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA224](seckeyalgorithm/ecdsasignaturemessagerfc4754sha224.md) — An algorithm for generating message signatures by calculating and signing the SHA224 message digest.
- [kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA256](seckeyalgorithm/ecdsasignaturemessagerfc4754sha256.md) — An algorithm for generating message signatures by calculating and signing the SHA256 message digest.
- [kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA384](seckeyalgorithm/ecdsasignaturemessagerfc4754sha384.md) — An algorithm for generating message signatures by calculating and signing the SHA384 message digest.
- [kSecKeyAlgorithmECDSASignatureMessageRFC4754SHA512](seckeyalgorithm/ecdsasignaturemessagerfc4754sha512.md) — An algorithm for generating message signatures by calculating and signing the SHA512 message digest.

### Elliptic curve signature digest X962

- [kSecKeyAlgorithmECDSASignatureDigestX962](seckeyalgorithm/ecdsasignaturedigestx962.md)
- [kSecKeyAlgorithmECDSASignatureDigestX962SHA1](seckeyalgorithm/ecdsasignaturedigestx962sha1.md)
- [kSecKeyAlgorithmECDSASignatureDigestX962SHA224](seckeyalgorithm/ecdsasignaturedigestx962sha224.md)
- [kSecKeyAlgorithmECDSASignatureDigestX962SHA256](seckeyalgorithm/ecdsasignaturedigestx962sha256.md)
- [kSecKeyAlgorithmECDSASignatureDigestX962SHA384](seckeyalgorithm/ecdsasignaturedigestx962sha384.md)
- [kSecKeyAlgorithmECDSASignatureDigestX962SHA512](seckeyalgorithm/ecdsasignaturedigestx962sha512.md)

### Elliptic curve signature message X962

- [kSecKeyAlgorithmECDSASignatureMessageX962SHA1](seckeyalgorithm/ecdsasignaturemessagex962sha1.md)
- [kSecKeyAlgorithmECDSASignatureMessageX962SHA224](seckeyalgorithm/ecdsasignaturemessagex962sha224.md)
- [kSecKeyAlgorithmECDSASignatureMessageX962SHA256](seckeyalgorithm/ecdsasignaturemessagex962sha256.md)
- [kSecKeyAlgorithmECDSASignatureMessageX962SHA384](seckeyalgorithm/ecdsasignaturemessagex962sha384.md)
- [kSecKeyAlgorithmECDSASignatureMessageX962SHA512](seckeyalgorithm/ecdsasignaturemessagex962sha512.md)

### Elliptic curve key exchange

- [kSecKeyAlgorithmECDHKeyExchangeCofactor](seckeyalgorithm/ecdhkeyexchangecofactor.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandard](seckeyalgorithm/ecdhkeyexchangestandard.md)
- [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA1](seckeyalgorithm/ecdhkeyexchangecofactorx963sha1.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA1](seckeyalgorithm/ecdhkeyexchangestandardx963sha1.md)
- [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA224](seckeyalgorithm/ecdhkeyexchangecofactorx963sha224.md)
- [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA256](seckeyalgorithm/ecdhkeyexchangecofactorx963sha256.md)
- [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA384](seckeyalgorithm/ecdhkeyexchangecofactorx963sha384.md)
- [kSecKeyAlgorithmECDHKeyExchangeCofactorX963SHA512](seckeyalgorithm/ecdhkeyexchangecofactorx963sha512.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA224](seckeyalgorithm/ecdhkeyexchangestandardx963sha224.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA256](seckeyalgorithm/ecdhkeyexchangestandardx963sha256.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA384](seckeyalgorithm/ecdhkeyexchangestandardx963sha384.md)
- [kSecKeyAlgorithmECDHKeyExchangeStandardX963SHA512](seckeyalgorithm/ecdhkeyexchangestandardx963sha512.md)

### RSA encryption

- [kSecKeyAlgorithmRSAEncryptionRaw](seckeyalgorithm/rsaencryptionraw.md)
- [kSecKeyAlgorithmRSAEncryptionPKCS1](seckeyalgorithm/rsaencryptionpkcs1.md)

### RSA encryption OAEP

- [kSecKeyAlgorithmRSAEncryptionOAEPSHA1](seckeyalgorithm/rsaencryptionoaepsha1.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA224](seckeyalgorithm/rsaencryptionoaepsha224.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA256](seckeyalgorithm/rsaencryptionoaepsha256.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA384](seckeyalgorithm/rsaencryptionoaepsha384.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA512](seckeyalgorithm/rsaencryptionoaepsha512.md)

### RSA encryption OAEP AESGCM

- [kSecKeyAlgorithmRSAEncryptionOAEPSHA1AESGCM](seckeyalgorithm/rsaencryptionoaepsha1aesgcm.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA224AESGCM](seckeyalgorithm/rsaencryptionoaepsha224aesgcm.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA256AESGCM](seckeyalgorithm/rsaencryptionoaepsha256aesgcm.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA384AESGCM](seckeyalgorithm/rsaencryptionoaepsha384aesgcm.md)
- [kSecKeyAlgorithmRSAEncryptionOAEPSHA512AESGCM](seckeyalgorithm/rsaencryptionoaepsha512aesgcm.md)

### RSA signature raw

- [kSecKeyAlgorithmRSASignatureRaw](seckeyalgorithm/rsasignatureraw.md)

### RSA signature digest PKCS1v15

- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15Raw](seckeyalgorithm/rsasignaturedigestpkcs1v15raw.md)
- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA1](seckeyalgorithm/rsasignaturedigestpkcs1v15sha1.md)
- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA224](seckeyalgorithm/rsasignaturedigestpkcs1v15sha224.md)
- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA256](seckeyalgorithm/rsasignaturedigestpkcs1v15sha256.md)
- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA384](seckeyalgorithm/rsasignaturedigestpkcs1v15sha384.md)
- [kSecKeyAlgorithmRSASignatureDigestPKCS1v15SHA512](seckeyalgorithm/rsasignaturedigestpkcs1v15sha512.md)

### RSA signature message PKCS1v15

- [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA1](seckeyalgorithm/rsasignaturemessagepkcs1v15sha1.md)
- [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA224](seckeyalgorithm/rsasignaturemessagepkcs1v15sha224.md)
- [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA256](seckeyalgorithm/rsasignaturemessagepkcs1v15sha256.md)
- [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA384](seckeyalgorithm/rsasignaturemessagepkcs1v15sha384.md)
- [kSecKeyAlgorithmRSASignatureMessagePKCS1v15SHA512](seckeyalgorithm/rsasignaturemessagepkcs1v15sha512.md)

### RSA signature digest PSS

- [kSecKeyAlgorithmRSASignatureDigestPSSSHA1](seckeyalgorithm/rsasignaturedigestpsssha1.md)
- [kSecKeyAlgorithmRSASignatureDigestPSSSHA224](seckeyalgorithm/rsasignaturedigestpsssha224.md)
- [kSecKeyAlgorithmRSASignatureDigestPSSSHA256](seckeyalgorithm/rsasignaturedigestpsssha256.md)
- [kSecKeyAlgorithmRSASignatureDigestPSSSHA384](seckeyalgorithm/rsasignaturedigestpsssha384.md)
- [kSecKeyAlgorithmRSASignatureDigestPSSSHA512](seckeyalgorithm/rsasignaturedigestpsssha512.md)

### RSA signature message PSS

- [kSecKeyAlgorithmRSASignatureMessagePSSSHA1](seckeyalgorithm/rsasignaturemessagepsssha1.md)
- [kSecKeyAlgorithmRSASignatureMessagePSSSHA224](seckeyalgorithm/rsasignaturemessagepsssha224.md)
- [kSecKeyAlgorithmRSASignatureMessagePSSSHA256](seckeyalgorithm/rsasignaturemessagepsssha256.md)
- [kSecKeyAlgorithmRSASignatureMessagePSSSHA384](seckeyalgorithm/rsasignaturemessagepsssha384.md)
- [kSecKeyAlgorithmRSASignatureMessagePSSSHA512](seckeyalgorithm/rsasignaturemessagepsssha512.md)

### Initializers

- [init(rawValue:)](<seckeyalgorithm/init(rawvalue_).md>)

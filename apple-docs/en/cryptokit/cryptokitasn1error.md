---
title: CryptoKitASN1Error
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/cryptokitasn1error
source_url: 'https://developer.apple.com/documentation/cryptokit/cryptokitasn1error'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/cryptokitasn1error.json'
content_hash: 'sha256:3626968fcc255dd4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# CryptoKitASN1Error

<sub>Enumeration</sub>

Errors from decoding ASN.1 content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CryptoKitASN1Error
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reporting errors

- [CryptoKitASN1Error.invalidASN1IntegerEncoding](cryptokitasn1error/invalidasn1integerencoding.md) — An ASN.1 integer doesn’t use the minimum number of bytes for its encoding.
- [CryptoKitASN1Error.invalidASN1Object](cryptokitasn1error/invalidasn1object.md) — The format of the parsed ASN.1 object doesn’t match the format required for the data type being decoded.
- [CryptoKitASN1Error.invalidFieldIdentifier](cryptokitasn1error/invalidfieldidentifier.md) — The ASN.1 tag for this field is invalid or unsupported.
- [CryptoKitASN1Error.invalidObjectIdentifier](cryptokitasn1error/invalidobjectidentifier.md) — An ASN.1 object identifier is invalid.
- [CryptoKitASN1Error.invalidPEMDocument](cryptokitasn1error/invalidpemdocument.md) — The string doesn’t parse as a PEM document.
- [CryptoKitASN1Error.truncatedASN1Field](cryptokitasn1error/truncatedasn1field.md) — An ASN.1 field is truncated.
- [CryptoKitASN1Error.unexpectedFieldType](cryptokitasn1error/unexpectedfieldtype.md) — The ASN.1 tag for the parsed field doesn’t match the required format.
- [CryptoKitASN1Error.unsupportedFieldLength](cryptokitasn1error/unsupportedfieldlength.md) — The encoding used for the field length is unsupported.

## See Also

### Errors

- [CryptoKitError](cryptokiterror.md) — General cryptography errors used by CryptoKit.

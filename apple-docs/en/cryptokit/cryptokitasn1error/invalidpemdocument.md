---
title: CryptoKitASN1Error.invalidPEMDocument
framework: Apple CryptoKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/cryptokitasn1error/invalidpemdocument
source_url: 'https://developer.apple.com/documentation/cryptokit/cryptokitasn1error/invalidpemdocument'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/cryptokitasn1error/invalidpemdocument.json'
content_hash: 'sha256:082f869a7f2dd527'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [CryptoKitASN1Error](../cryptokitasn1error.md)

# CryptoKitASN1Error.invalidPEMDocument

<sub>Case</sub>

The string doesn’t parse as a PEM document.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidPEMDocument
```

## See Also

### Reporting errors

- [CryptoKitASN1Error.invalidASN1IntegerEncoding](invalidasn1integerencoding.md) — An ASN.1 integer doesn’t use the minimum number of bytes for its encoding.
- [CryptoKitASN1Error.invalidASN1Object](invalidasn1object.md) — The format of the parsed ASN.1 object doesn’t match the format required for the data type being decoded.
- [CryptoKitASN1Error.invalidFieldIdentifier](invalidfieldidentifier.md) — The ASN.1 tag for this field is invalid or unsupported.
- [CryptoKitASN1Error.invalidObjectIdentifier](invalidobjectidentifier.md) — An ASN.1 object identifier is invalid.
- [CryptoKitASN1Error.truncatedASN1Field](truncatedasn1field.md) — An ASN.1 field is truncated.
- [CryptoKitASN1Error.unexpectedFieldType](unexpectedfieldtype.md) — The ASN.1 tag for the parsed field doesn’t match the required format.
- [CryptoKitASN1Error.unsupportedFieldLength](unsupportedfieldlength.md) — The encoding used for the field length is unsupported.

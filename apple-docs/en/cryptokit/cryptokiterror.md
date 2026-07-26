---
title: CryptoKitError
framework: Apple CryptoKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/cryptokit/cryptokiterror
source_url: 'https://developer.apple.com/documentation/cryptokit/cryptokiterror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/cryptokiterror.json'
content_hash: 'sha256:a8fe1e949092fe33'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Apple CryptoKit](../cryptokit.md)

# CryptoKitError

<sub>Enumeration</sub>

General cryptography errors used by CryptoKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum CryptoKitError
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Reporting errors

- [CryptoKitError.incorrectKeySize](cryptokiterror/incorrectkeysize.md) — The key size is incorrect.
- [CryptoKitError.invalidParameter](cryptokiterror/invalidparameter.md) — The parameter is invalid.
- [CryptoKitError.incorrectParameterSize](cryptokiterror/incorrectparametersize.md) — The parameter size is incorrect.
- [CryptoKitError.underlyingCoreCryptoError(error:)](<cryptokiterror/underlyingcorecryptoerror(error_).md>) — The underlying corecrypto library is unable to complete the requested action.
- [CryptoKitError.authenticationFailure](cryptokiterror/authenticationfailure.md) — The authentication tag or signature is incorrect.
- [CryptoKitError.wrapFailure](cryptokiterror/wrapfailure.md) — The framework can’t wrap the specified key.
- [CryptoKitError.unwrapFailure](cryptokiterror/unwrapfailure.md) — The framework can’t unwrap the specified key.

## See Also

### Errors

- [CryptoKitASN1Error](cryptokitasn1error.md) — Errors from decoding ASN.1 content.

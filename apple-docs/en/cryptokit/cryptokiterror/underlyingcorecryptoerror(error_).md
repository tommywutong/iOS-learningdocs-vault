---
title: 'CryptoKitError.underlyingCoreCryptoError(error:)'
framework: Apple CryptoKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/cryptokit/cryptokiterror/underlyingcorecryptoerror(error:)'
source_url: 'https://developer.apple.com/documentation/cryptokit/cryptokiterror/underlyingcorecryptoerror(error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/cryptokit/cryptokiterror/underlyingcorecryptoerror%28error%3A%29.json'
content_hash: 'sha256:a55f59269e7d367d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Apple CryptoKit](../../cryptokit.md) · [CryptoKitError](../cryptokiterror.md)

# CryptoKitError.underlyingCoreCryptoError(error:)

<sub>Case</sub>

The underlying corecrypto library is unable to complete the requested action.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case underlyingCoreCryptoError(error: Int32)
```

## See Also

### Reporting errors

- [CryptoKitError.incorrectKeySize](incorrectkeysize.md) — The key size is incorrect.
- [CryptoKitError.invalidParameter](invalidparameter.md) — The parameter is invalid.
- [CryptoKitError.incorrectParameterSize](incorrectparametersize.md) — The parameter size is incorrect.
- [CryptoKitError.authenticationFailure](authenticationfailure.md) — The authentication tag or signature is incorrect.
- [CryptoKitError.wrapFailure](wrapfailure.md) — The framework can’t wrap the specified key.
- [CryptoKitError.unwrapFailure](unwrapfailure.md) — The framework can’t unwrap the specified key.

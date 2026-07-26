---
title: VerificationResult.VerificationError
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/verificationerror
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/verificationerror'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/verificationerror.json'
content_hash: 'sha256:e2fc6ab888e3912a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [VerificationResult](../verificationresult.md)

# VerificationResult.VerificationError

<sub>Enumeration</sub>

Error cases for StoreKit JWS verification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum VerificationError
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Error](../../swift/error.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [LocalizedError](../../foundation/localizederror.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error Codes

- [VerificationResult.VerificationError.invalidCertificateChain](verificationerror/invalidcertificatechain.md) — An error indicating that the certificate chain is invalid.
- [VerificationResult.VerificationError.invalidDeviceVerification](verificationerror/invaliddeviceverification.md) — An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](verificationerror/invalidencoding.md) — An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.invalidSignature](verificationerror/invalidsignature.md) — An error that indicates that the signature didn’t match the header and payload.
- [VerificationResult.VerificationError.missingRequiredProperties](verificationerror/missingrequiredproperties.md) — An error that indicates the header or payload are missing information that’s required to verify the signature.
- [VerificationResult.VerificationError.revokedCertificate](verificationerror/revokedcertificate.md) — An error that indicates the certificate chain includes a revoked certificate.

## See Also

### JWS verification

- [VerificationResult](../verificationresult.md) — A type that describes the result of a StoreKit verification.

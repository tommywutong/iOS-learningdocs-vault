---
title: VerificationResult.VerificationError.revokedCertificate
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/verificationerror/revokedcertificate
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/verificationerror/revokedcertificate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/verificationerror/revokedcertificate.json'
content_hash: 'sha256:2f299bae1c7a3d9c'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [VerificationResult](../../verificationresult.md) · [VerificationError](../verificationerror.md)

# VerificationResult.VerificationError.revokedCertificate

<sub>Case</sub>

An error that indicates the certificate chain includes a revoked certificate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case revokedCertificate
```

## Discussion

In some cases, this error may resolve if you try again later.

## See Also

### Error Codes

- [VerificationResult.VerificationError.invalidCertificateChain](invalidcertificatechain.md) — An error indicating that the certificate chain is invalid.
- [VerificationResult.VerificationError.invalidDeviceVerification](invaliddeviceverification.md) — An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](invalidencoding.md) — An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.invalidSignature](invalidsignature.md) — An error that indicates that the signature didn’t match the header and payload.
- [VerificationResult.VerificationError.missingRequiredProperties](missingrequiredproperties.md) — An error that indicates the header or payload are missing information that’s required to verify the signature.

---
title: VerificationResult.VerificationError.invalidCertificateChain
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/verificationresult/verificationerror/invalidcertificatechain
source_url: 'https://developer.apple.com/documentation/storekit/verificationresult/verificationerror/invalidcertificatechain'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/verificationresult/verificationerror/invalidcertificatechain.json'
content_hash: 'sha256:646f253ac0546002'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [VerificationResult](../../verificationresult.md) · [VerificationError](../verificationerror.md)

# VerificationResult.VerificationError.invalidCertificateChain

<sub>Case</sub>

An error indicating that the certificate chain is invalid.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case invalidCertificateChain
```

## Discussion

This error may occur if one or more certificates in the certiificate chain are expired or from an untrusted source.

## See Also

### Error Codes

- [VerificationResult.VerificationError.invalidDeviceVerification](invaliddeviceverification.md) — An error that indicates the signed value wasn’t generated for the current device.
- [VerificationResult.VerificationError.invalidEncoding](invalidencoding.md) — An error that indicates the signature, certificate chain, or other part of value uses invalid encoding.
- [VerificationResult.VerificationError.invalidSignature](invalidsignature.md) — An error that indicates that the signature didn’t match the header and payload.
- [VerificationResult.VerificationError.missingRequiredProperties](missingrequiredproperties.md) — An error that indicates the header or payload are missing information that’s required to verify the signature.
- [VerificationResult.VerificationError.revokedCertificate](revokedcertificate.md) — An error that indicates the certificate chain includes a revoked certificate.

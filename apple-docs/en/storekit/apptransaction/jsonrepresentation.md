---
title: jsonRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, macOS 13.0+, tvOS 16.0+, visionOS 1.0+, watchOS 9.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/apptransaction/jsonrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/apptransaction/jsonrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/apptransaction/jsonrepresentation.json'
content_hash: 'sha256:5f4f949124959a32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [AppTransaction](../apptransaction.md)

# jsonRepresentation

<sub>Instance Property</sub>

The JSON representation of the app transaction information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jsonRepresentation: Data { get }
```

## Discussion

The [jsonRepresentation](jsonrepresentation.md) is UTF-8 string data that contains the same information as the properties of the [AppTransaction](../apptransaction.md). You can use this JSON data to decode the app transaction information into your own data type instead of using [AppTransaction](../apptransaction.md) properties directly.

The JSON Web Signature (JWS) Compact Serialization for the [AppTransaction](../apptransaction.md) is available in the [jwsRepresentation](../verificationresult/jwsrepresentation-6ma59.md) property of the [VerificationResult](../verificationresult.md). The JWS string consists of three Base64URL-encoded components, separated by a period: a header, a payload, and a signature. The [jsonRepresentation](jsonrepresentation.md) is the Base64URL-decoded payload component.

> [!note] Note
> If you send the app transaction to your server or store it, use the [jwsRepresentation](../verificationresult/jwsrepresentation-178oj.md) and validate the signature before parsing it.

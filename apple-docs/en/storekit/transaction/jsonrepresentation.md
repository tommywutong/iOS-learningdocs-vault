---
title: jsonRepresentation
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, macOS 12.0+, tvOS 15.0+, visionOS 1.0+, watchOS 8.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/transaction/jsonrepresentation
source_url: 'https://developer.apple.com/documentation/storekit/transaction/jsonrepresentation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/transaction/jsonrepresentation.json'
content_hash: 'sha256:e152be791b60e18d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [Transaction](../transaction.md)

# jsonRepresentation

<sub>Instance Property</sub>

The JSON representation of the transaction information.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var jsonRepresentation: Data { get }
```

## Discussion

The [jsonRepresentation](jsonrepresentation.md) is UTF-8 string data that has the same JSON schema as the [JWSTransactionDecodedPayload](../../appstoreserverapi/jwstransactiondecodedpayload.md) object. You can use this data to decode the transaction information into your own data type instead of using the [Transaction](../transaction.md) value and its [Transaction properties](../transaction-properties.md) directly.

The JSON Web Signature (JWS) Compact Serialization for the transaction is available in the [jwsRepresentation](../verificationresult/jwsrepresentation-21vgo.md) property of the [VerificationResult](../verificationresult.md). The JWS string consists of three Base64URL-encoded components, separated by a period: a header, a payload, and a signature. The [jsonRepresentation](jsonrepresentation.md) is the Base64URL-decoded payload component.

> [!note] Note
> If you send the transaction to your server or store it, use the [jwsRepresentation](../verificationresult/jwsrepresentation-21vgo.md) and validate the signature before parsing it.

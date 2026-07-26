---
title: 'init(keyID:nonce:timestamp:signature:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.4+（26.0 起废弃）, iPadOS 17.4+（26.0 起废弃）, macOS 14.4+（26.0 起废弃）, tvOS 17.4+（26.0 起废弃）, visionOS 1.1+（26.0 起废弃）, watchOS 10.4+（26.0 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: '/documentation/storekit/product/subscriptionoffer/signature/init(keyid:nonce:timestamp:signature:)'
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature/init(keyid:nonce:timestamp:signature:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/signature/init%28keyid%3Anonce%3Atimestamp%3Asignature%3A%29.json'
content_hash: 'sha256:2bfc8419ea1efda3'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionOffer](../../subscriptionoffer.md) · [Signature](../signature.md)

# init(keyID:nonce:timestamp:signature:)

<sub>Initializer</sub>

Creates a subscription offer signature instance.

> [!warning] Deprecated
> Sign promotional offers with JWS and use PurchaseOption.promotionalOffer(_:compactJWS:) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(keyID: String, nonce: UUID, timestamp: Int, signature: Data)
```

## Parameters

- `keyID` — A string that identifies the private key you use to generate the signature. You set up this key in App Store Connect. For more information, see [Generate keys for in-app purchases](https://developer.apple.com/help/app-store-connect/configure-in-app-purchase-settings/generate-keys-for-in-app-purchases).

- `nonce` — A one-time UUID value that your server generates. Generate a new nonce for each signature. The string representation of the nonce you use in the signature must be lowercase.

- `timestamp` — A timestamp your server generates in UNIX time format, in milliseconds. The timestamp keeps the offer active for 24 hours.

- `signature` — The cryptographic signature your server generates to sign the promotional offer.

---
title: signature
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.4+（26.0 起废弃）, iPadOS 17.4+（26.0 起废弃）, macOS 14.4+（26.0 起废弃）, tvOS 17.4+（26.0 起废弃）, visionOS 1.1+（26.0 起废弃）, watchOS 10.4+（26.0 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptionoffer/signature/signature
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature/signature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/signature/signature.json'
content_hash: 'sha256:d62573b480ebb842'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [StoreKit](../../../../storekit.md) · [Product](../../../product.md) · [SubscriptionOffer](../../subscriptionoffer.md) · [Signature](../signature.md)

# signature

<sub>Instance Property</sub>

A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription.

> [!warning] Deprecated
> Sign promotional offers with JWS and use PurchaseOption.promotionalOffer(_:compactJWS:) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var signature: Data
```

## See Also

### Getting signature elements

- [keyID](keyid.md) — A string that identifies the private key you use to generate the cryptographic signature. _(deprecated)_
- [nonce](nonce.md) — A one-time UUID your server generates for the promotional offer. _(deprecated)_
- [timestamp](timestamp.md) — A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature. _(deprecated)_

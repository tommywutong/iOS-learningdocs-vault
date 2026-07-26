---
title: Product.SubscriptionOffer.Signature
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.4+（26.0 起废弃）, iPadOS 17.4+（26.0 起废弃）, macOS 14.4+（26.0 起废弃）, tvOS 17.4+（26.0 起废弃）, visionOS 1.1+（26.0 起废弃）, watchOS 10.4+（26.0 起废弃）]
languages: [swift, swift, swift, swift]
beta: false
deprecated: true
doc_path: /documentation/storekit/product/subscriptionoffer/signature
source_url: 'https://developer.apple.com/documentation/storekit/product/subscriptionoffer/signature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/product/subscriptionoffer/signature.json'
content_hash: 'sha256:f64f569ae1a679d4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [Product](../../product.md) · [SubscriptionOffer](../subscriptionoffer.md)

# Product.SubscriptionOffer.Signature

<sub>Structure</sub>

A cryptographic signature for a promotional offer.

> [!warning] Deprecated
> Sign promotional offers with JWS and use PurchaseOption.promotionalOffer(_:compactJWS:) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Signature
```

## Overview

For information about promotional offers, see [Implementing promotional offers in your app](../../implementing-promotional-offers-in-your-app.md).

The App Store Server Library provides a function that produces signatures for promotional offers. For more information, see [Simplifying your implementation by using the App Store Server Library](../../../appstoreserverapi/simplifying-your-implementation-by-using-the-app-store-server-library.md).

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### Creating subscription offer signatures

- [init(keyID:nonce:timestamp:signature:)](<signature/init(keyid_nonce_timestamp_signature_).md>) — Creates a subscription offer signature instance. _(deprecated)_

### Getting signature elements

- [keyID](signature/keyid.md) — A string that identifies the private key you use to generate the cryptographic signature. _(deprecated)_
- [nonce](signature/nonce.md) — A one-time UUID your server generates for the promotional offer. _(deprecated)_
- [signature](signature/signature.md) — A cryptographic signature your server generates to sign a promotional offer for an auto-renewable subscription. _(deprecated)_
- [timestamp](signature/timestamp.md) — A timestamp your server generates in UNIX time format, in milliseconds, that indicates the time the server generated the signature. _(deprecated)_

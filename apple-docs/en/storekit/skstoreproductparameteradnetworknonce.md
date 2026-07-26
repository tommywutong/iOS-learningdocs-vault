---
title: SKStoreProductParameterAdNetworkNonce
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, tvOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworknonce
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworknonce'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworknonce.json'
content_hash: 'sha256:519c1fcc2f018c5a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkNonce

<sub>Global Variable</sub>

The key that represents a random value to use for added security.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkNonce: String
```

## Discussion

The value for this key is an [NSUUID](../foundation/nsuuid.md). Ad networks generate a random value for this key at the time of the ad impression.

> [!important] Important
> When you generate the signature value ([SKStoreProductParameterAdNetworkAttributionSignature](skstoreproductparameteradnetworkattributionsignature.md)), you must sign the nonce as an all-lowercase UUID string representation.

## See Also

### Required keys

- [SKStoreProductParameterAdNetworkIdentifier](skstoreproductparameteradnetworkidentifier.md) — The key that represents the advertising network’s unique identifier.
- [SKStoreProductParameterAdNetworkCampaignIdentifier](skstoreproductparameteradnetworkcampaignidentifier.md) — The key that represents the advertising network’s campaign.
- [SKStoreProductParameterAdNetworkTimestamp](skstoreproductparameteradnetworktimestamp.md) — The key that represents the UNIX time, in milliseconds, of the ad impression.
- [SKStoreProductParameterAdNetworkAttributionSignature](skstoreproductparameteradnetworkattributionsignature.md) — The key that represents the advertising network’s cryptographic signature to use for install validation.

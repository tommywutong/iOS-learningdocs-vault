---
title: SKStoreProductParameterAdNetworkTimestamp
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, tvOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworktimestamp
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworktimestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworktimestamp.json'
content_hash: 'sha256:29ae22a533536be8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkTimestamp

<sub>Global Variable</sub>

The key that represents the UNIX time, in milliseconds, of the ad impression.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkTimestamp: String
```

## Discussion

The value for this key is an [NSNumber](../foundation/nsnumber.md). Ad networks generate the timestamp, represented as UNIX time in milliseconds, at the time you’re preparing to serve the ad.

## See Also

### Required keys

- [SKStoreProductParameterAdNetworkIdentifier](skstoreproductparameteradnetworkidentifier.md) — The key that represents the advertising network’s unique identifier.
- [SKStoreProductParameterAdNetworkCampaignIdentifier](skstoreproductparameteradnetworkcampaignidentifier.md) — The key that represents the advertising network’s campaign.
- [SKStoreProductParameterAdNetworkNonce](skstoreproductparameteradnetworknonce.md) — The key that represents a random value to use for added security.
- [SKStoreProductParameterAdNetworkAttributionSignature](skstoreproductparameteradnetworkattributionsignature.md) — The key that represents the advertising network’s cryptographic signature to use for install validation.

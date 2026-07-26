---
title: SKStoreProductParameterAdNetworkCampaignIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, tvOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworkcampaignidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkcampaignidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworkcampaignidentifier.json'
content_hash: 'sha256:d931b67dbffcaf2a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkCampaignIdentifier

<sub>Global Variable</sub>

The key that represents the advertising network’s campaign.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkCampaignIdentifier: String
```

## Discussion

The value for this key is an [NSNumber](../foundation/nsnumber.md). Ad networks determine their own campaign identifiers, which must be an integer `>=1` and `<=100`.

Use [SKStoreProductParameterAdNetworkSourceIdentifier](skstoreproductparameteradnetworksourceidentifier.md) instead of this value to generate version 4 and later signatures.

## See Also

### Required keys

- [SKStoreProductParameterAdNetworkIdentifier](skstoreproductparameteradnetworkidentifier.md) — The key that represents the advertising network’s unique identifier.
- [SKStoreProductParameterAdNetworkTimestamp](skstoreproductparameteradnetworktimestamp.md) — The key that represents the UNIX time, in milliseconds, of the ad impression.
- [SKStoreProductParameterAdNetworkNonce](skstoreproductparameteradnetworknonce.md) — The key that represents a random value to use for added security.
- [SKStoreProductParameterAdNetworkAttributionSignature](skstoreproductparameteradnetworkattributionsignature.md) — The key that represents the advertising network’s cryptographic signature to use for install validation.

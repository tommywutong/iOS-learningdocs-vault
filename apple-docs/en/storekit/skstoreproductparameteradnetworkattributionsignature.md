---
title: SKStoreProductParameterAdNetworkAttributionSignature
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, tvOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworkattributionsignature
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkattributionsignature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworkattributionsignature.json'
content_hash: 'sha256:6513e5e4962c467a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkAttributionSignature

<sub>Global Variable</sub>

The key that represents the advertising network’s cryptographic signature to use for install validation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkAttributionSignature: String
```

## Discussion

The value for this key is an [NSString](../foundation/nsstring.md). The ad network creates the cryptographic signature, used to sign ads. For instructions on generating this value, see [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md).

## See Also

### Required keys

- [SKStoreProductParameterAdNetworkIdentifier](skstoreproductparameteradnetworkidentifier.md) — The key that represents the advertising network’s unique identifier.
- [SKStoreProductParameterAdNetworkCampaignIdentifier](skstoreproductparameteradnetworkcampaignidentifier.md) — The key that represents the advertising network’s campaign.
- [SKStoreProductParameterAdNetworkTimestamp](skstoreproductparameteradnetworktimestamp.md) — The key that represents the UNIX time, in milliseconds, of the ad impression.
- [SKStoreProductParameterAdNetworkNonce](skstoreproductparameteradnetworknonce.md) — The key that represents a random value to use for added security.

---
title: SKStoreProductParameterAdNetworkIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 11.3+, iPadOS 11.3+, Mac Catalyst 13.1+, tvOS 11.3+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworkidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworkidentifier.json'
content_hash: 'sha256:bdb3a071149bc9fe'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkIdentifier

<sub>Global Variable</sub>

The key that represents the advertising network’s unique identifier.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkIdentifier: String
```

## Discussion

The value for this key is an [NSString](../foundation/nsstring.md).

Ad networks obtain an ad network identifier during registration. Ad networks are responsible for sharing their ad network IDs with participating app developers. Apps that display ads and need to initiate the app install validation process must include the ad network ID in their `Info.plist`. For more information see [Registering an ad network](registering-an-ad-network.md) and `Configuring Apps`.

## See Also

### Required keys

- [SKStoreProductParameterAdNetworkCampaignIdentifier](skstoreproductparameteradnetworkcampaignidentifier.md) — The key that represents the advertising network’s campaign.
- [SKStoreProductParameterAdNetworkTimestamp](skstoreproductparameteradnetworktimestamp.md) — The key that represents the UNIX time, in milliseconds, of the ad impression.
- [SKStoreProductParameterAdNetworkNonce](skstoreproductparameteradnetworknonce.md) — The key that represents a random value to use for added security.
- [SKStoreProductParameterAdNetworkAttributionSignature](skstoreproductparameteradnetworkattributionsignature.md) — The key that represents the advertising network’s cryptographic signature to use for install validation.

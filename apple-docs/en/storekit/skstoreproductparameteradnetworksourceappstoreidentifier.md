---
title: SKStoreProductParameterAdNetworkSourceAppStoreIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworksourceappstoreidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworksourceappstoreidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworksourceappstoreidentifier.json'
content_hash: 'sha256:7b47e7e0f66a86dc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkSourceAppStoreIdentifier

<sub>Global Variable</sub>

The key that represents the App Store ID of the app that displays the ad.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkSourceAppStoreIdentifier: String
```

## Discussion

The value for this key is an [NSNumber](../foundation/nsnumber.md). Provide the App Store item identifier of the app that’s displaying the ad.

During testing, if you’re using a development-signed build to display the ads and not an app from App Store, use `0` as the item identifier.

## See Also

### Required keys for SKAdNetwork 2 and later

- [SKStoreProductParameterAdNetworkVersion](skstoreproductparameteradnetworkversion.md) — The key that represents the version of the ad network API.

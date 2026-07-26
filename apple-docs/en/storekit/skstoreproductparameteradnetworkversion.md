---
title: SKStoreProductParameterAdNetworkVersion
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworkversion
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworkversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworkversion.json'
content_hash: 'sha256:6d8a7160181cc7b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkVersion

<sub>Global Variable</sub>

The key that represents the version of the ad network API.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkVersion: String
```

## Discussion

The value for this key is an [NSString](../foundation/nsstring.md). Set this key to version number “`4.0`”, “`3.0`”, “`2.2"`, `“2.1"`, or `"2.0"`. Use the highest available version whenever possible. For version availability, see [SKAdNetwork release notes](skadnetwork-release-notes.md).

Ad networks use this key and the other [Ad network install-validation keys](ad-network-install-validation-keys.md) when signing ads. For more information, see [Generating the signature to validate StoreKit-rendered ads](generating-the-signature-to-validate-storekit-rendered-ads.md).

## See Also

### Required keys for SKAdNetwork 2 and later

- [SKStoreProductParameterAdNetworkSourceAppStoreIdentifier](skstoreproductparameteradnetworksourceappstoreidentifier.md) — The key that represents the App Store ID of the app that displays the ad.

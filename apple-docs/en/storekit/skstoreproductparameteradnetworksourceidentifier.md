---
title: SKStoreProductParameterAdNetworkSourceIdentifier
framework: StoreKit
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+, tvOS 16.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skstoreproductparameteradnetworksourceidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skstoreproductparameteradnetworksourceidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skstoreproductparameteradnetworksourceidentifier.json'
content_hash: 'sha256:428c1d3afdd07f3e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKStoreProductParameterAdNetworkSourceIdentifier

<sub>Global Variable</sub>

A four-digit integer that ad networks define to represent the ad campaign.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
let SKStoreProductParameterAdNetworkSourceIdentifier: String
```

## Discussion

This key is available for ad impressions that use SKAdNetwork 4 and later. The [SKStoreProductParameterAdNetworkSourceIdentifier](skstoreproductparameteradnetworksourceidentifier.md), also known as the _hierarchical source identifier_, replaces and extends the campaign identifier value, [SKStoreProductParameterAdNetworkCampaignIdentifier](skstoreproductparameteradnetworkcampaignidentifier.md).

Ad networks and developers define the meaning of the hierarchical source identifier. This string represents an integer of up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the [sourceIdentifier](skadimpression/sourceidentifier.md) in the first winning postback, depending on the ad impression’s postback data tier. For more information about the value you may get in the postback, see [Receiving postbacks in multiple conversion windows](receiving-postbacks-in-multiple-conversion-windows.md).

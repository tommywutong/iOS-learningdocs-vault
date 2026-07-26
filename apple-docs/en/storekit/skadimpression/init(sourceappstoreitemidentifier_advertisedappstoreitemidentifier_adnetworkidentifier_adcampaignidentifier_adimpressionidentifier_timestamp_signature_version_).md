---
title: 'init(sourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:)'
framework: StoreKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/storekit/skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:)'
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/init(sourceappstoreitemidentifier:advertisedappstoreitemidentifier:adnetworkidentifier:adcampaignidentifier:adimpressionidentifier:timestamp:signature:version:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/init%28sourceappstoreitemidentifier%3Aadvertisedappstoreitemidentifier%3Aadnetworkidentifier%3Aadcampaignidentifier%3Aadimpressionidentifier%3Atimestamp%3Asignature%3Aversion%3A%29.json'
content_hash: 'sha256:f548a5f63e87cd99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# init(sourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:)

<sub>Initializer</sub>

Creates an ad impression object using the supplied values.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
init(sourceAppStoreItemIdentifier: NSNumber, advertisedAppStoreItemIdentifier: NSNumber, adNetworkIdentifier: String, adCampaignIdentifier: NSNumber, adImpressionIdentifier: String, timestamp: NSNumber, signature: String, version: String)
```

## See Also

### Creating a signature

- [version](version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

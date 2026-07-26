---
title: adCampaignIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/adcampaignidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/adcampaignidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/adcampaignidentifier.json'
content_hash: 'sha256:15c6f7f61f6dee61'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# adCampaignIdentifier

<sub>Instance Property</sub>

A number that represents the advertising network’s campaign.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var adCampaignIdentifier: NSNumber { get set }
```

## Discussion

Ad networks set their own campaign identifiers, which must be an integer `>=1` and `<=100.`

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

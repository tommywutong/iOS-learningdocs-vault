---
title: sourceAppStoreItemIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/sourceappstoreitemidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/sourceappstoreitemidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/sourceappstoreitemidentifier.json'
content_hash: 'sha256:d4f1eaafe4274d95'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# sourceAppStoreItemIdentifier

<sub>Instance Property</sub>

The App Store ID of the app that displays the ad.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var sourceAppStoreItemIdentifier: NSNumber { get set }
```

## Discussion

Set this property to the App Store item identifier of the app that’s displaying the ad.

If you’re using a development-signed build to display the ads and not an app from App Store during testing, use `0` as the item identifier.

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

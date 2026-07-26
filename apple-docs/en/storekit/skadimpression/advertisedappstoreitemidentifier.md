---
title: advertisedAppStoreItemIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/advertisedappstoreitemidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/advertisedappstoreitemidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/advertisedappstoreitemidentifier.json'
content_hash: 'sha256:e613a09f890a23ab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# advertisedAppStoreItemIdentifier

<sub>Instance Property</sub>

The App Store ID of the app that the ad impression advertises.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var advertisedAppStoreItemIdentifier: NSNumber { get set }
```

## Discussion

Set this property to the App Store item identifier of the app that you’re advertising.

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

---
title: adNetworkIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/adnetworkidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/adnetworkidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/adnetworkidentifier.json'
content_hash: 'sha256:9894966d1fe41787'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# adNetworkIdentifier

<sub>Instance Property</sub>

A string that represents the advertising network’s unique identifier.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var adNetworkIdentifier: String { get set }
```

## Discussion

Set this property to your ad network ID.

Ad networks obtain an ad network identifier during registration. Ad networks must share their ad network identifiers with participating app developers. Apps that display ads must include the ad network ID in their `Info.plist` to initiate the app install validation process. For more information about acquiring your ad network ID, see [Registering an ad network](../registering-an-ad-network.md).

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](version.md) — The version of the SKAdNetwork API.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

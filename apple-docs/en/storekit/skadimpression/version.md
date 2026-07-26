---
title: version
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/version
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/version'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/version.json'
content_hash: 'sha256:e6ae04444e1531dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# version

<sub>Instance Property</sub>

The version of the SKAdNetwork API.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var version: String { get set }
```

## Discussion

Set this instance property to the SKAdNetwork version you’re using to sign the view-through ad impression. View-through ads are available starting in version 2.2. For more information about versions and availability, see [SKAdNetwork release notes](../skadnetwork-release-notes.md).

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

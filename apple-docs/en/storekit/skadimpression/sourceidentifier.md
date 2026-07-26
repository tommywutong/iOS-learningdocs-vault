---
title: sourceIdentifier
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.1+, iPadOS 16.1+, Mac Catalyst 16.1+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression/sourceidentifier
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression/sourceidentifier'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression/sourceidentifier.json'
content_hash: 'sha256:dbff534b4a38e1e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKAdImpression](../skadimpression.md)

# sourceIdentifier

<sub>Instance Property</sub>

A four-digit integer that ad networks define to represent the ad campaign.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var sourceIdentifier: NSNumber { get set }
```

## Discussion

The [sourceIdentifier](sourceidentifier.md) key is available for ad impressions that use SKAdNetwork 4 and later. The [sourceIdentifier](sourceidentifier.md), also known as the _hierarchical source identifier_, replaces and extends the campaign identifier value, [adCampaignIdentifier](adcampaignidentifier.md).

Ad networks and developers define the meaning of the hierarchical source identifier. This integer can have up to four digits. You can encode information about your advertisement in each set of digits; you may receive two, three, or all four digits of the [sourceIdentifier](sourceidentifier.md) in the first winning postback, depending on the ad impression’s postback data tier. For more information about the value you may get in the postback, see [Receiving postbacks in multiple conversion windows](../receiving-postbacks-in-multiple-conversion-windows.md).

> [!note] Note
> An install-validation postback represents this integer as a string in its `source-identifier` parameter. For more details about the parameters of an install-validation postback, see [Identifying the parameters in install-validation postbacks](../identifying-the-parameters-in-install-validation-postbacks.md).

## See Also

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [adCampaignIdentifier](adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

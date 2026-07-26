---
title: SKAdImpression
framework: StoreKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skadimpression
source_url: 'https://developer.apple.com/documentation/storekit/skadimpression'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skadimpression.json'
content_hash: 'sha256:3db582da8360321c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKAdImpression

<sub>Class</sub>

A class that defines an ad impression for a view-through ad.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class SKAdImpression
```

## Overview

Create a `SKAdImpression` instance when you’re preparing to present a view-through ad. In the instance, you set:

- Values known to you, including your ad network ID, the App Store IDs of the source app and the advertised app, and the version.
- A value you determine – the campaign ID.
- Values you generate, including the timestamp, a nonce (ad-impression identifier), and the cryptographic signature.

For information about generating the cryptographic signature, see [Generating the signature to validate view-through ads](generating-the-signature-to-validate-view-through-ads.md).

Use your `SKAdImpression` instance when you call [+ startImpression:completionHandler:](<skadnetwork/startimpression(__completionhandler_).md>) to begin presenting your view-through ad. Use the same instance when you call [+ endImpression:completionHandler:](<skadnetwork/endimpression(__completionhandler_).md>) to end the ad presentation.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing a signature

- [signature](skadimpression/signature.md) — The advertising network’s cryptographic signature for the ad impression.

### Creating a signature

- [- initWithSourceAppStoreItemIdentifier:advertisedAppStoreItemIdentifier:adNetworkIdentifier:adCampaignIdentifier:adImpressionIdentifier:timestamp:signature:version:](<skadimpression/init(sourceappstoreitemidentifier_advertisedappstoreitemidentifier_adnetworkidentifier_adcampaignidentifier_adimpressionidentifier_timestamp_signature_version_).md>) — Creates an ad impression object using the supplied values.
- [version](skadimpression/version.md) — The version of the SKAdNetwork API.
- [adNetworkIdentifier](skadimpression/adnetworkidentifier.md) — A string that represents the advertising network’s unique identifier.
- [sourceIdentifier](skadimpression/sourceidentifier.md) — A four-digit integer that ad networks define to represent the ad campaign.
- [adCampaignIdentifier](skadimpression/adcampaignidentifier.md) — A number that represents the advertising network’s campaign.
- [advertisedAppStoreItemIdentifier](skadimpression/advertisedappstoreitemidentifier.md) — The App Store ID of the app that the ad impression advertises.
- [adImpressionIdentifier](skadimpression/adimpressionidentifier.md) — A random value to use for added security.
- [sourceAppStoreItemIdentifier](skadimpression/sourceappstoreitemidentifier.md) — The App Store ID of the app that displays the ad.
- [timestamp](skadimpression/timestamp.md) — A number that represents the UNIX time, in milliseconds, of the ad impression.

### Describing ads

- [adType](skadimpression/adtype.md) — The type of the ad.
- [adDescription](skadimpression/addescription.md) — A human-readable description of the ad.
- [adPurchaserName](skadimpression/adpurchasername.md) — The name of the entity that purchased the ad.

## See Also

### Ad impressions and installation validations

- [Understanding AdAttributionKit and SKAdNetwork interoperability](../adattributionkit/adattributionkit-skadnetwork-interoperability.md) — Learn how attribution APIs interact to deliver ad impressions.
- [SKAdNetwork](skadnetwork.md) — A class that validates advertisement-driven app installations.

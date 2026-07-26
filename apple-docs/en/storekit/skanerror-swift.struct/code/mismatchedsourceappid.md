---
title: SKANError.Code.mismatchedSourceAppId
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/code/mismatchedsourceappid
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/mismatchedsourceappid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/code/mismatchedsourceappid.json'
content_hash: 'sha256:addfa5b8c9d74f3e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKANError](../../skanerror-swift.struct.md) · [Code](../code.md)

# SKANError.Code.mismatchedSourceAppId

<sub>Case</sub>

The source app identifier in the ad impression doesn’t match the app identifier in the source app.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case mismatchedSourceAppId
```

## Discussion

Check that the [sourceAppStoreItemIdentifier](../../skadimpression/sourceappstoreitemidentifier.md) you provide in the [SKAdImpression](../../skadimpression.md) object matches the app identifier of the app displaying the ad.

## See Also

### Error Codes

- [SKANErrorAdNetworkIdMissing](adnetworkidmissing.md) — The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANErrorImpressionMissingRequiredValue](impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [SKANErrorImpressionNotFound](impressionnotfound.md) — The system can’t find the ad impression.
- [SKANErrorImpressionTooShort](impressiontooshort.md)
- [SKANErrorInvalidAdvertisedAppId](invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [SKANErrorInvalidCampaignId](invalidcampaignid.md) — The campaign identifier that you provided is invalid.
- [SKANErrorInvalidConversionValue](invalidconversionvalue.md) — The conversion value is invalid.
- [SKANErrorInvalidSourceAppId](invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [SKANErrorInvalidVersion](invalidversion.md) — The SKAdNetwork version number is invalid.
- [SKANErrorUnknown](unknown.md) — An unknown error occurred.
- [SKANErrorUnsupported](unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.

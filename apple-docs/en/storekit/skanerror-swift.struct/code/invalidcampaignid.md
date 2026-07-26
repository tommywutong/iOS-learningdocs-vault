---
title: SKANError.Code.invalidCampaignId
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/code/invalidcampaignid
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/invalidcampaignid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/code/invalidcampaignid.json'
content_hash: 'sha256:b035c7e384a6d19e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKANError](../../skanerror-swift.struct.md) · [Code](../code.md)

# SKANError.Code.invalidCampaignId

<sub>Case</sub>

The campaign identifier that you provided is invalid.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case invalidCampaignId
```

## Discussion

Check that the campaign identifier is a valid value. For more information, see [SKStoreProductParameterAdNetworkCampaignIdentifier](../../skstoreproductparameteradnetworkcampaignidentifier.md) for StoreKit-rendered ads, and [adCampaignIdentifier](../../skadimpression/adcampaignidentifier.md) for view-through ads.

## See Also

### Error Codes

- [SKANErrorAdNetworkIdMissing](adnetworkidmissing.md) — The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANErrorImpressionMissingRequiredValue](impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [SKANErrorImpressionNotFound](impressionnotfound.md) — The system can’t find the ad impression.
- [SKANErrorImpressionTooShort](impressiontooshort.md)
- [SKANErrorInvalidAdvertisedAppId](invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [SKANErrorInvalidConversionValue](invalidconversionvalue.md) — The conversion value is invalid.
- [SKANErrorInvalidSourceAppId](invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [SKANErrorInvalidVersion](invalidversion.md) — The SKAdNetwork version number is invalid.
- [SKANErrorMismatchedSourceAppId](mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANErrorUnknown](unknown.md) — An unknown error occurred.
- [SKANErrorUnsupported](unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.

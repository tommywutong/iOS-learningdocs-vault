---
title: SKANError.Code.adNetworkIdMissing
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/code/adnetworkidmissing
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/adnetworkidmissing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/code/adnetworkidmissing.json'
content_hash: 'sha256:fd3c246dcf689057'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKANError](../../skanerror-swift.struct.md) · [Code](../code.md)

# SKANError.Code.adNetworkIdMissing

<sub>Case</sub>

The ad network identifier in the ad impression doesn’t match the value in the information property list.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case adNetworkIdMissing
```

## Discussion

The value you specify for your ad network identifier in your ad impresion must match the value in the `Info.plist`. ``An app that participates in ad campaigns by displaying ads must include the ad network identifiers in its `Info.plist`. For more information, see [Configuring a source app](../../configuring-a-source-app.md).

## See Also

### Error Codes

- [SKANErrorImpressionMissingRequiredValue](impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [SKANErrorImpressionNotFound](impressionnotfound.md) — The system can’t find the ad impression.
- [SKANErrorImpressionTooShort](impressiontooshort.md)
- [SKANErrorInvalidAdvertisedAppId](invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [SKANErrorInvalidCampaignId](invalidcampaignid.md) — The campaign identifier that you provided is invalid.
- [SKANErrorInvalidConversionValue](invalidconversionvalue.md) — The conversion value is invalid.
- [SKANErrorInvalidSourceAppId](invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [SKANErrorInvalidVersion](invalidversion.md) — The SKAdNetwork version number is invalid.
- [SKANErrorMismatchedSourceAppId](mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANErrorUnknown](unknown.md) — An unknown error occurred.
- [SKANErrorUnsupported](unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.

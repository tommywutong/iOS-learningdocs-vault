---
title: SKANError.Code.invalidVersion
framework: StoreKit
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/code/invalidversion
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/invalidversion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/code/invalidversion.json'
content_hash: 'sha256:7da5b5cb024b9bb5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [StoreKit](../../../storekit.md) · [SKANError](../../skanerror-swift.struct.md) · [Code](../code.md)

# SKANError.Code.invalidVersion

<sub>Case</sub>

The SKAdNetwork version number is invalid.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
case invalidVersion
```

## Discussion

Ad networks provide an SKAdNetwork version number when preparing an ad impression, in [SKStoreProductParameterAdNetworkVersion](../../skstoreproductparameteradnetworkversion.md) or [version](../../skadimpression/version.md). Check that the version number is valid and that you follow the version-specific instructions to generate a signature. For more information about versions, see [SKAdNetwork release notes](../../skadnetwork-release-notes.md).

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
- [SKANErrorMismatchedSourceAppId](mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANErrorUnknown](unknown.md) — An unknown error occurred.
- [SKANErrorUnsupported](unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.

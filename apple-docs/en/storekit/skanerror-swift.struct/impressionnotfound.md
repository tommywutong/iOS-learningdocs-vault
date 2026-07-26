---
title: impressionNotFound
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/impressionnotfound
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/impressionnotfound'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/impressionnotfound.json'
content_hash: 'sha256:d964be9157d83e41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKANError](../skanerror-swift.struct.md)

# impressionNotFound

<sub>Type Property</sub>

The system can’t find the ad impression.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
static var impressionNotFound: SKANError.Code { get }
```

## Discussion

This error may occur if an app calls [+ endImpression:completionHandler:](<../skadnetwork/endimpression(__completionhandler_).md>) before calling [+ startImpression:completionHandler:](<../skadnetwork/startimpression(__completionhandler_).md>).

## See Also

### Getting Error Codes

- [adNetworkIdMissing](adnetworkidmissing.md) — The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [impressionMissingRequiredValue](impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [impressionTooShort](impressiontooshort.md)
- [invalidAdvertisedAppId](invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [invalidCampaignId](invalidcampaignid.md) — The campaign identifier that you provided is invalid.
- [invalidConversionValue](invalidconversionvalue.md) — The conversion value is invalid.
- [invalidSourceAppId](invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [invalidVersion](invalidversion.md) — The SKAdNetwork version number is invalid.
- [mismatchedSourceAppId](mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [unknown](unknown.md) — An unknown error occurred.
- [unsupported](unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.
- [Code](code.md) — Constants that indicate the type of error for an ad network attribution operation.

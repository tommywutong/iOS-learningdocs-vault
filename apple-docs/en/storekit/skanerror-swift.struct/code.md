---
title: SKANError.Code
framework: StoreKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct/code
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct/code.json'
content_hash: 'sha256:3f12e7ccb52ec5a1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKANError](../skanerror-swift.struct.md)

# SKANError.Code

<sub>Enumeration</sub>

Constants that indicate the type of error for an ad network attribution operation.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
enum Code
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Error Codes

- [SKANErrorAdNetworkIdMissing](code/adnetworkidmissing.md) — The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANErrorImpressionMissingRequiredValue](code/impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [SKANErrorImpressionNotFound](code/impressionnotfound.md) — The system can’t find the ad impression.
- [SKANErrorImpressionTooShort](code/impressiontooshort.md)
- [SKANErrorInvalidAdvertisedAppId](code/invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [SKANErrorInvalidCampaignId](code/invalidcampaignid.md) — The campaign identifier that you provided is invalid.
- [SKANErrorInvalidConversionValue](code/invalidconversionvalue.md) — The conversion value is invalid.
- [SKANErrorInvalidSourceAppId](code/invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [SKANErrorInvalidVersion](code/invalidversion.md) — The SKAdNetwork version number is invalid.
- [SKANErrorMismatchedSourceAppId](code/mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANErrorUnknown](code/unknown.md) — An unknown error occurred.
- [SKANErrorUnsupported](code/unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.

### Initializers

- [init(rawValue:)](<code/init(rawvalue_).md>)

## See Also

### Error handling

- [SKANErrorDomain](../skanerrordomain.md) — A string that identifies the SKAdNetwork error domain.
- [SKANError](../skanerror-swift.struct.md) — An error that an ad network attribution operation returns.

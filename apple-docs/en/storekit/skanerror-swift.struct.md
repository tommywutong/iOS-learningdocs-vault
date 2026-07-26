---
title: SKANError
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/storekit/skanerror-swift.struct
source_url: 'https://developer.apple.com/documentation/storekit/skanerror-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skanerror-swift.struct.json'
content_hash: 'sha256:dd7ca9639dfe415a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKANError

<sub>Structure</sub>

An error that an ad network attribution operation returns.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
struct SKANError
```

## Relationships

- **Conforms To**: [CustomNSError](../foundation/customnserror.md), [Equatable](../swift/equatable.md), [Error](../swift/error.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting Error Codes

- [adNetworkIdMissing](skanerror-swift.struct/adnetworkidmissing.md) — The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [impressionMissingRequiredValue](skanerror-swift.struct/impressionmissingrequiredvalue.md) — A required value is missing from a view-through ad impression.
- [impressionNotFound](skanerror-swift.struct/impressionnotfound.md) — The system can’t find the ad impression.
- [impressionTooShort](skanerror-swift.struct/impressiontooshort.md)
- [invalidAdvertisedAppId](skanerror-swift.struct/invalidadvertisedappid.md) — The App Store ID of the advertised app is invalid.
- [invalidCampaignId](skanerror-swift.struct/invalidcampaignid.md) — The campaign identifier that you provided is invalid.
- [invalidConversionValue](skanerror-swift.struct/invalidconversionvalue.md) — The conversion value is invalid.
- [invalidSourceAppId](skanerror-swift.struct/invalidsourceappid.md) — The App Store ID of the app displaying the ad is invalid.
- [invalidVersion](skanerror-swift.struct/invalidversion.md) — The SKAdNetwork version number is invalid.
- [mismatchedSourceAppId](skanerror-swift.struct/mismatchedsourceappid.md) — The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [unknown](skanerror-swift.struct/unknown.md) — An unknown error occurred.
- [unsupported](skanerror-swift.struct/unsupported.md) — Your app attempted to use functionality that isn’t supported in the specified version.
- [Code](skanerror-swift.struct/code.md) — Constants that indicate the type of error for an ad network attribution operation.

### Type Properties

- [errorDomain](skanerror-swift.struct/errordomain.md)

## See Also

### Error handling

- [SKANErrorDomain](skanerrordomain.md) — A string that identifies the SKAdNetwork error domain.
- [Code](skanerror-swift.struct/code.md) — Constants that indicate the type of error for an ad network attribution operation.

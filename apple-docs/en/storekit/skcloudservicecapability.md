---
title: SKCloudServiceCapability
framework: StoreKit
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicecapability
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecapability'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecapability.json'
content_hash: 'sha256:af1d222c2e3518c8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [StoreKit](../storekit.md)

# SKCloudServiceCapability

<sub>Structure</sub>

Constants that specify the current capabilities of the customer’s Music library on the device.

> [!warning] Deprecated
> Use MusicSubscription from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
struct SKCloudServiceCapability
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializing

- [init(rawValue:)](<skcloudservicecapability/init(rawvalue_).md>) — Initializes a cloud service capability with the provided raw value. _(deprecated)_

### Identifying Cloud Service Capabilities

- [SKCloudServiceCapabilityMusicCatalogPlayback](skcloudservicecapability/musiccatalogplayback.md) — The device allows playback of Apple Music catalog tracks. _(deprecated)_
- [SKCloudServiceCapabilityMusicCatalogSubscriptionEligible](skcloudservicecapability/musiccatalogsubscriptioneligible.md) — The device allows subscription to the Apple Music catalog. _(deprecated)_
- [SKCloudServiceCapabilityAddToCloudMusicLibrary](skcloudservicecapability/addtocloudmusiclibrary.md) — The device allows tracks to be added to the user’s music library. _(deprecated)_

## See Also

### Determining capabilities

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md) — Determine which Apple Music capabilities are available on a customer’s device.
- [- requestUserTokenForDeveloperToken:completionHandler:](<skcloudservicecontroller/requestusertoken(fordevelopertoken_completionhandler_).md>) — Returns a user token that you use to access personalized Apple Music content. _(deprecated)_
- [- requestStorefrontCountryCodeWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontcountrycode(completionhandler_).md>) — Gets the country code for the storefront associated with a customer’s iTunes account. _(deprecated)_
- [- requestCapabilitiesWithCompletionHandler:](<skcloudservicecontroller/requestcapabilities(completionhandler_).md>) — Gets the current capabilities associated with the Music library on the device. _(deprecated)_
- [- requestStorefrontIdentifierWithCompletionHandler:](<skcloudservicecontroller/requeststorefrontidentifier(completionhandler_).md>) — Gets the device’s storefront identifier. _(deprecated)_
- [- requestPersonalizationTokenForClientToken:withCompletionHandler:](<skcloudservicecontroller/requestpersonalizationtoken(forclienttoken_withcompletionhandler_).md>) _(deprecated)_

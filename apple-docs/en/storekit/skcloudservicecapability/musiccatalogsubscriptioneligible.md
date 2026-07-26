---
title: musicCatalogSubscriptionEligible
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.1+（18.0 起废弃）, iPadOS 10.1+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 10.1+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicecapability/musiccatalogsubscriptioneligible
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecapability/musiccatalogsubscriptioneligible'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecapability/musiccatalogsubscriptioneligible.json'
content_hash: 'sha256:f626bfafa9f2d0f3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceCapability](../skcloudservicecapability.md)

# musicCatalogSubscriptionEligible

<sub>Type Property</sub>

The device allows subscription to the Apple Music catalog.

> [!warning] Deprecated
> Use the canBecomeSubscriber property of MusicSubscription from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var musicCatalogSubscriptionEligible: SKCloudServiceCapability { get }
```

## See Also

### Identifying Cloud Service Capabilities

- [SKCloudServiceCapabilityMusicCatalogPlayback](musiccatalogplayback.md) — The device allows playback of Apple Music catalog tracks. _(deprecated)_
- [SKCloudServiceCapabilityAddToCloudMusicLibrary](addtocloudmusiclibrary.md) — The device allows tracks to be added to the user’s music library. _(deprecated)_

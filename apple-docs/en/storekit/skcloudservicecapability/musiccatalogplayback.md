---
title: musicCatalogPlayback
framework: StoreKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 9.3+（18.0 起废弃）, iPadOS 9.3+（18.0 起废弃）, Mac Catalyst 13.0+（18.0 起废弃）, macOS 11.0+（15.0 起废弃）, tvOS 9.3+（18.0 起废弃）, watchOS 7.0+（11.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/storekit/skcloudservicecapability/musiccatalogplayback
source_url: 'https://developer.apple.com/documentation/storekit/skcloudservicecapability/musiccatalogplayback'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/storekit/skcloudservicecapability/musiccatalogplayback.json'
content_hash: 'sha256:5f54b072b8dd6e4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [StoreKit](../../storekit.md) · [SKCloudServiceCapability](../skcloudservicecapability.md)

# musicCatalogPlayback

<sub>Type Property</sub>

The device allows playback of Apple Music catalog tracks.

> [!warning] Deprecated
> Use MusicSubscription from MusicKit.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, watchOS</sub>

```swift
static var musicCatalogPlayback: SKCloudServiceCapability { get }
```

## See Also

### Identifying Cloud Service Capabilities

- [SKCloudServiceCapabilityMusicCatalogSubscriptionEligible](musiccatalogsubscriptioneligible.md) — The device allows subscription to the Apple Music catalog. _(deprecated)_
- [SKCloudServiceCapabilityAddToCloudMusicLibrary](addtocloudmusiclibrary.md) — The device allows tracks to be added to the user’s music library. _(deprecated)_

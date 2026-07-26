---
title: AVPlayerInterstitialEventAssetListResponseStatus.available
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/available
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/available'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/available.json'
content_hash: 'sha256:2ee83a1f7d1abe64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventAssetListResponseStatus](../avplayerinterstitialeventassetlistresponsestatus.md)

# AVPlayerInterstitialEventAssetListResponseStatus.available

<sub>Case</sub>

Indicates that a valid asset list response is available.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case available
```

## Discussion

You can retrieve the value by querying the [assetListResponse](../avplayerinterstitialevent/assetlistresponse.md) property of the interstitial event.

## See Also

### Status values

- [AVPlayerInterstitialEventAssetListResponseStatusCleared](cleared.md) — Indicates that the system cleared the asset list response.
- [AVPlayerInterstitialEventAssetListResponseStatusUnavailable](unavailable.md) — Indicates that the asset list response is unavailable.

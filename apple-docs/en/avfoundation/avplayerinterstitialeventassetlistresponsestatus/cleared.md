---
title: AVPlayerInterstitialEventAssetListResponseStatus.cleared
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/cleared
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/cleared'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus/cleared.json'
content_hash: 'sha256:b994c5252a950881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventAssetListResponseStatus](../avplayerinterstitialeventassetlistresponsestatus.md)

# AVPlayerInterstitialEventAssetListResponseStatus.cleared

<sub>Case</sub>

Indicates that the system cleared the asset list response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case cleared
```

## Discussion

This status indicates that the interstital event’s [assetListResponse](../avplayerinterstitialevent/assetlistresponse.md) property is `nil`.

## See Also

### Status values

- [AVPlayerInterstitialEventAssetListResponseStatusAvailable](available.md) — Indicates that a valid asset list response is available.
- [AVPlayerInterstitialEventAssetListResponseStatusUnavailable](unavailable.md) — Indicates that the asset list response is unavailable.

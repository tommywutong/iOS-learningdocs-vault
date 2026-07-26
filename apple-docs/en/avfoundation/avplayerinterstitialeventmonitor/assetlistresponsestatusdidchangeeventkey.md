---
title: assetListResponseStatusDidChangeEventKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeeventkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeeventkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeeventkey.json'
content_hash: 'sha256:7c063262f0ef0846'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# assetListResponseStatusDidChangeEventKey

<sub>Type Property</sub>

A key to retrieve the interstitial event that has an asset list response status change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let assetListResponseStatusDidChangeEventKey: String
```

## Discussion

Use this key to retrieve the [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md) object that has an updates asset list response.

## See Also

### User information keys

- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey](assetlistresponsestatusdidchangestatuskey.md) — A key to retrieve the asset list response status.
- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey](assetlistresponsestatusdidchangeerrorkey.md) — A key to retrieve the error related to a change in an interstitial event’s asset list response.

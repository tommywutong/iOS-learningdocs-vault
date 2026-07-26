---
title: assetListResponseStatusDidChangeErrorKey
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeerrorkey
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeerrorkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangeerrorkey.json'
content_hash: 'sha256:b74a9904f8682059'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# assetListResponseStatusDidChangeErrorKey

<sub>Type Property</sub>

A key to retrieve the error related to a change in an interstitial event’s asset list response.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let assetListResponseStatusDidChangeErrorKey: String
```

## Discussion

This key only exists in the notification’s [userInfo](../../foundation/notification/userinfo.md) dictionary when the status is [AVPlayerInterstitialEventAssetListResponseStatusUnavailable](../avplayerinterstitialeventassetlistresponsestatus/unavailable.md). Use it to retrieve an error object that provides information about the failure to read the asset list.

## See Also

### User information keys

- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeEventKey](assetlistresponsestatusdidchangeeventkey.md) — A key to retrieve the interstitial event that has an asset list response status change.
- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey](assetlistresponsestatusdidchangestatuskey.md) — A key to retrieve the asset list response status.

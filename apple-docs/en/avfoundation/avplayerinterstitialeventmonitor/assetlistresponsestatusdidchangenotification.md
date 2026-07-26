---
title: assetListResponseStatusDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.json'
content_hash: 'sha256:49051bb8551bbec5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEventMonitor](../avplayerinterstitialeventmonitor.md)

# assetListResponseStatusDidChangeNotification

<sub>Type Property</sub>

A notification the system posts when the status of an interstitial event’s asset list response changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class let assetListResponseStatusDidChangeNotification: NSNotification.Name
```

## Discussion

Notifications of this type provide a [userInfo](../../foundation/notification/userinfo.md) dictionary that can contain values for the keys listed below.

## Topics

### User information keys

- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeEventKey](assetlistresponsestatusdidchangeeventkey.md) — A key to retrieve the interstitial event that has an asset list response status change.
- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeStatusKey](assetlistresponsestatusdidchangestatuskey.md) — A key to retrieve the asset list response status.
- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeErrorKey](assetlistresponsestatusdidchangeerrorkey.md) — A key to retrieve the error related to a change in an interstitial event’s asset list response.

## See Also

### Monitoring the asset list response

- [AVPlayerInterstitialEventAssetListResponseStatus](../avplayerinterstitialeventassetlistresponsestatus.md) — Constants that describe the status of the asset list response for an interstitial event.

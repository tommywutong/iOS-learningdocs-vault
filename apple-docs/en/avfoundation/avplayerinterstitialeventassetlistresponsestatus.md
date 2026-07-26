---
title: AVPlayerInterstitialEventAssetListResponseStatus
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialeventassetlistresponsestatus.json'
content_hash: 'sha256:a00d02d224e470cc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVPlayerInterstitialEventAssetListResponseStatus

<sub>Enumeration</sub>

Constants that describe the status of the asset list response for an interstitial event.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum AVPlayerInterstitialEventAssetListResponseStatus
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Status values

- [AVPlayerInterstitialEventAssetListResponseStatusAvailable](avplayerinterstitialeventassetlistresponsestatus/available.md) — Indicates that a valid asset list response is available.
- [AVPlayerInterstitialEventAssetListResponseStatusCleared](avplayerinterstitialeventassetlistresponsestatus/cleared.md) — Indicates that the system cleared the asset list response.
- [AVPlayerInterstitialEventAssetListResponseStatusUnavailable](avplayerinterstitialeventassetlistresponsestatus/unavailable.md) — Indicates that the asset list response is unavailable.

### Initializers

- [init(rawValue:)](<avplayerinterstitialeventassetlistresponsestatus/init(rawvalue_).md>)

## See Also

### Monitoring the asset list response

- [AVPlayerInterstitialEventMonitorAssetListResponseStatusDidChangeNotification](avplayerinterstitialeventmonitor/assetlistresponsestatusdidchangenotification.md) — A notification the system posts when the status of an interstitial event’s asset list response changes.

---
title: assetListResponse
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.4+, iPadOS 16.4+, Mac Catalyst 16.4+, macOS 13.3+, tvOS 16.4+, visionOS 1.0+, watchOS 9.4+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerinterstitialevent/assetlistresponse
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerinterstitialevent/assetlistresponse'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerinterstitialevent/assetlistresponse.json'
content_hash: 'sha256:aa4aad5179047810'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerInterstitialEvent](../avplayerinterstitialevent.md)

# assetListResponse

<sub>Instance Property</sub>

The asset list JSON response as a dictionary.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var assetListResponse: [AnyHashable : any Sendable]? { get }
```

## Discussion

The value of this property is `nil` if there is no asset list loaded for the event. If this value is `nil` and the event’s [templateItems](templateitems.md) is empty, then an asset list read is expected. If this value is `nil` and [templateItems](templateitems.md) isn’t empty, an asset list read isn’t expected.

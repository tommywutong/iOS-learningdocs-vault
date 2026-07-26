---
title: nowPlayingInfo
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayeritem/nowplayinginfo
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayeritem/nowplayinginfo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayeritem/nowplayinginfo.json'
content_hash: 'sha256:da8550d446313061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerItem](../avplayeritem.md)

# nowPlayingInfo

<sub>Instance Property</sub>

The current now playing information for the player item.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var nowPlayingInfo: [String : Any]? { get set }
```

## Discussion

Setting this value to `nil` clears the player item’s now playing information.

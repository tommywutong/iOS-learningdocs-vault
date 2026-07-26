---
title: isObservationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayer/isobservationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayer/isobservationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayer/isobservationenabled.json'
content_hash: 'sha256:17b9b3d23f687436'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayer](../avplayer.md)

# isObservationEnabled

<sub>Type Property</sub>

AVPlayer and other AVFoundation types can optionally be observed using Swift Observation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
nonisolated class var isObservationEnabled: Bool { get set }
```

## Discussion

When set to YES, new instances of AVPlayer, AVQueuePlayer, AVPlayerItem, and AVPlayerItemTrack are observable with Swift Observation. The default value is NO (not observable).  An exception is thrown if this property is set YES after initializing any objects of these types, or if it is set to NO after any observable objects are initialized.  In other words, all objects of these types must either be observable or not observable in an application instance.

For more information regarding management of class objects in SwiftUI, please refer to https://developer.apple.com/documentation/swiftui/state.

---
title: status
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/status-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/status-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/status-swift.property.json'
content_hash: 'sha256:6b76c5cc391d9b23'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# status

<sub>Instance Property</sub>

A status that indicates the object’s ability to loop playback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var status: AVPlayerLooper.Status { get }
```

## Discussion

When the value of this property is [AVPlayerLooperStatusFailed](status-swift.enum/failed.md) or [AVPlayerLooperStatusCancelled](status-swift.enum/cancelled.md), you can no longer use the looper for playback. You need to create a new instance to begin looping again.

This property is key-value observable.

## See Also

### Observing looping state

- [loopCount](loopcount.md) — The number of times the object played the media.
- [Status](status-swift.enum.md) — Status constants that indicate whether a looper can successfully perform looping playback.

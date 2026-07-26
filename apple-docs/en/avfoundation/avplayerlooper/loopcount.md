---
title: loopCount
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avplayerlooper/loopcount
source_url: 'https://developer.apple.com/documentation/avfoundation/avplayerlooper/loopcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avplayerlooper/loopcount.json'
content_hash: 'sha256:30aeeb8ee00caf7b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVPlayerLooper](../avplayerlooper.md)

# loopCount

<sub>Instance Property</sub>

The number of times the object played the media.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var loopCount: Int { get }
```

## Discussion

This value starts at 0 and increments as the player continues to loop the replica player items.

This property is key-value observable.

## See Also

### Observing looping state

- [status](status-swift.property.md) — A status that indicates the object’s ability to loop playback.
- [Status](status-swift.enum.md) — Status constants that indicate whether a looper can successfully perform looping playback.

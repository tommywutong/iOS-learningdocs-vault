---
title: startTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturereactioneffectstate/starttime
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/starttime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturereactioneffectstate/starttime.json'
content_hash: 'sha256:4a31ea4ae6be1598'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)

# startTime

<sub>Instance Property</sub>

The presentation time of the first frame where the system renders the effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var startTime: CMTime { get }
```

## See Also

### Configuring the effect state

- [reactionType](reactiontype.md) — The type of reaction.
- [AVCaptureReactionType](../avcapturereactiontype.md) — Constants that indicate the type of reaction that an effect can perform.
- [endTime](endtime.md) — The presentation time of the first frame following the end of a reaction effect.

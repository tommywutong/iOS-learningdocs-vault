---
title: reactionType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturereactioneffectstate/reactiontype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/reactiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturereactioneffectstate/reactiontype.json'
content_hash: 'sha256:089ba72cfd45380c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)

# reactionType

<sub>Instance Property</sub>

The type of reaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var reactionType: AVCaptureReactionType { get }
```

## Discussion

There may be multiple reactions of the same type at a given time. Some may come from calls to [- performEffectForReaction:](<../avcapturedevice/performeffect(for_).md>) and others from gesture detection.

## See Also

### Configuring the effect state

- [AVCaptureReactionType](../avcapturereactiontype.md) — Constants that indicate the type of reaction that an effect can perform.
- [startTime](starttime.md) — The presentation time of the first frame where the system renders the effect.
- [endTime](endtime.md) — The presentation time of the first frame following the end of a reaction effect.

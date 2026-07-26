---
title: endTime
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturereactioneffectstate/endtime
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate/endtime'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturereactioneffectstate/endtime.json'
content_hash: 'sha256:e408e3317b884729'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md)

# endTime

<sub>Instance Property</sub>

The presentation time of the first frame following the end of a reaction effect.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var endTime: CMTime { get }
```

## Discussion

The value is [invalid](../../coremedia/cmtime/invalid.md) while the effect is in progress, but changes to a valid time when the reaction effect completes and the system removes it from the list of [reactionEffectsInProgress](../avcapturedevice/reactioneffectsinprogress.md).

## See Also

### Configuring the effect state

- [reactionType](reactiontype.md) — The type of reaction.
- [AVCaptureReactionType](../avcapturereactiontype.md) — Constants that indicate the type of reaction that an effect can perform.
- [startTime](starttime.md) — The presentation time of the first frame where the system renders the effect.

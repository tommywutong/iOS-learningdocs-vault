---
title: canPerformReactionEffects
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/canperformreactioneffects
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/canperformreactioneffects'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/canperformreactioneffects.json'
content_hash: 'sha256:5e401c2f9e6341c0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# canPerformReactionEffects

<sub>Instance Property</sub>

A Boolean value that indicates whether you can perform reaction effects on a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var canPerformReactionEffects: Bool { get }
```

## Discussion

This value is [true](../../swift/true.md) when a device’s [reactionEffectsEnabled](reactioneffectsenabled.md) and its active format’s [reactionEffectsSupported](format/reactioneffectssupported.md) property values are [true](../../swift/true.md).

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [availableReactionTypes](availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

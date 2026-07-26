---
title: reactionEffectsInProgress
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/reactioneffectsinprogress
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectsinprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/reactioneffectsinprogress.json'
content_hash: 'sha256:2af4afb8a3c1f652'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# reactionEffectsInProgress

<sub>Instance Property</sub>

An array of reaction effects that the device is currently performing, sorted by timestamp.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var reactionEffectsInProgress: [AVCaptureReactionEffectState] { get }
```

## Discussion

Key-value observe this property to determine when reaction effects begin and end. If your key-value observing callback provides old and new values, any in-progress reaction effects in the new array have a value of [invalid](../../coremedia/cmtime/invalid.md) for their [endTime](../avcapturereactioneffectstate/endtime.md) property value. Completed reaction effects are only in the old array, and have their [endTime](../avcapturereactioneffectstate/endtime.md) property value set to the presentation time of the first frame where the reaction effect was no longer present.

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

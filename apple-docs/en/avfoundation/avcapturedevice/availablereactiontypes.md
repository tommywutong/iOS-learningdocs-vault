---
title: availableReactionTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/availablereactiontypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/availablereactiontypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/availablereactiontypes.json'
content_hash: 'sha256:fb853937be5ab421'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# availableReactionTypes

<sub>Instance Property</sub>

A set of reactions types that a device supports performing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var availableReactionTypes: Set<AVCaptureReactionType> { get }
```

## Discussion

The list may differ between devices, and may change for a specific device when it’s active format changes.

This property is key-value observable.

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [reactionEffectGesturesEnabled](reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

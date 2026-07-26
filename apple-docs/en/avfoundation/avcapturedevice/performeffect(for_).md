---
title: 'performEffect(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/performeffect(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/performeffect(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/performeffect%28for%3A%29.json'
content_hash: 'sha256:5a74a819330327a3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# performEffect(for:)

<sub>Instance Method</sub>

Performs the specified reaction type on the video stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func performEffect(for reactionType: AVCaptureReactionType)
```

## Parameters

- `reactionType` — A reaction type to perform. Specifying a type that doesn’t exists within the set of [availableReactionTypes](availablereactiontypes.md) for the device results in an exception.

## Discussion

The entries in the [reactionEffectsInProgress](reactioneffectsinprogress.md) property may not reflect one-to-one with calls to this method. Depending on reaction style or resource limits, the system may coalesce overlapping reactions of the same type by extending an existing reaction rather than overlaying a new one.

> [!note] Note
> Calling this method has no effect when the value of [canPerformReactionEffects](canperformreactioneffects.md) is [false](../../swift/false.md). In this case, VoIP apps should transmit and display reactions outside of the video feed.

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [reactionEffectsInProgress](reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

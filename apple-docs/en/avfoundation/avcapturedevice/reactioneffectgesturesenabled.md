---
title: reactionEffectGesturesEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/reactioneffectgesturesenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectgesturesenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/reactioneffectgesturesenabled.json'
content_hash: 'sha256:1767fe6243ae1192'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# reactionEffectGesturesEnabled

<sub>Type Property</sub>

A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var reactionEffectGesturesEnabled: Bool { get }
```

## Discussion

This property reflects the enabled state of Gestures in Control Center.

Gesture detection runs only when the device’s active format supports reaction effects, which you determine by querying the value of the format’s [reactionEffectsSupported](format/reactioneffectssupported.md) property.

This property is key-value observable.

> [!note] Note
> Your app can call [- performEffectForReaction:](<performeffect(for_).md>)independently the value of this property. The system intermixes reaction effects from either source.

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [- performEffectForReaction:](<performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

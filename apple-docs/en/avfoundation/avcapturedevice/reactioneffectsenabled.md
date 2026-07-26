---
title: reactionEffectsEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/reactioneffectsenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/reactioneffectsenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/reactioneffectsenabled.json'
content_hash: 'sha256:39ce2783fa181965'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# reactionEffectsEnabled

<sub>Type Property</sub>

A Boolean value that indicates whether the app supports performing reaction effects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var reactionEffectsEnabled: Bool { get }
```

## Discussion

The system only renders reaction effects when the device’s active format supports the feature, which you determine by querying the value of its [reactionEffectsSupported](format/reactioneffectssupported.md) property.

In macOS, the system enables reaction effects for all apps by default. In iOS, it enables them by default only for video conferencing apps (apps that enable the Voice over IP option in their [UIBackgroundModes](../../bundleresources/information-property-list/uibackgroundmodes.md) configuration). Apps that don’t use this background mode may opt in to this feature by adding the following key to the `Info.plist` file.

```swift
<key>NSCameraReactionEffectsEnabled</key>
<true/>
```

## See Also

### Performing reaction effects

- [canPerformReactionEffects](canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](../avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

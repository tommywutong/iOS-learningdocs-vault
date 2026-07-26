---
title: AVCaptureReactionEffectState
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturereactioneffectstate
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturereactioneffectstate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturereactioneffectstate.json'
content_hash: 'sha256:25b9925e4e47d468'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureReactionEffectState

<sub>Class</sub>

An object that reports the state of a reaction effect performed on a capture device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class AVCaptureReactionEffectState
```

## Overview

Obtain an instance of this class by querying a capture device’s [reactionEffectsInProgress](avcapturedevice/reactioneffectsinprogress.md) property. The system adds new entries to this array when you call [- performEffectForReaction:](<avcapturedevice/performeffect(for_).md>) or by gesture detection in the capture stream when the value of [reactionEffectGesturesEnabled](avcapturedevice/reactioneffectgesturesenabled.md) is [true](../swift/true.md).

The system renders the effect before providing frames to your app, and these status objects let you know when it performs the effect.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Configuring the effect state

- [reactionType](avcapturereactioneffectstate/reactiontype.md) — The type of reaction.
- [AVCaptureReactionType](avcapturereactiontype.md) — Constants that indicate the type of reaction that an effect can perform.
- [startTime](avcapturereactioneffectstate/starttime.md) — The presentation time of the first frame where the system renders the effect.
- [endTime](avcapturereactioneffectstate/endtime.md) — The presentation time of the first frame following the end of a reaction effect.

## See Also

### Performing reaction effects

- [reactionEffectsEnabled](avcapturedevice/reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](avcapturedevice/canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](avcapturedevice/availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](avcapturedevice/reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<avcapturedevice/performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](avcapturedevice/reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.

---
title: System video effects and microphone modes
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/system-video-effects-and-microphone-modes
source_url: 'https://developer.apple.com/documentation/avfoundation/system-video-effects-and-microphone-modes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/system-video-effects-and-microphone-modes.json'
content_hash: 'sha256:34c2f54eb2096ee6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# System video effects and microphone modes

<sub>API Collection</sub>

Configure the state of system video effects like Center Stage, and inspect enhancements the system applies to microphone audio.

## Topics

### Performing reaction effects

- [reactionEffectsEnabled](avcapturedevice/reactioneffectsenabled.md) — A Boolean value that indicates whether the app supports performing reaction effects.
- [canPerformReactionEffects](avcapturedevice/canperformreactioneffects.md) — A Boolean value that indicates whether you can perform reaction effects on a capture device.
- [availableReactionTypes](avcapturedevice/availablereactiontypes.md) — A set of reactions types that a device supports performing.
- [reactionEffectGesturesEnabled](avcapturedevice/reactioneffectgesturesenabled.md) — A Boolean value that indicates whether gesture detection triggers reaction effects on the video stream.
- [- performEffectForReaction:](<avcapturedevice/performeffect(for_).md>) — Performs the specified reaction type on the video stream.
- [reactionEffectsInProgress](avcapturedevice/reactioneffectsinprogress.md) — An array of reaction effects that the device is currently performing, sorted by timestamp.
- [AVCaptureReactionEffectState](avcapturereactioneffectstate.md) — An object that reports the state of a reaction effect performed on a capture device.

### Configuring Center Stage

- [centerStageActive](avcapturedevice/iscenterstageactive.md) — A Boolean value that indicates whether Center Stage is active on a device.
- [centerStageEnabled](avcapturedevice/iscenterstageenabled.md) — A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [centerStageRectOfInterest](avcapturedevice/centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [centerStageControlMode](avcapturedevice/centerstagecontrolmode-swift.type.property.md) — A value that indicates the current mode of Center Stage control.
- [CenterStageControlMode](avcapturedevice/centerstagecontrolmode-swift.enum.md) — Constants that indicate the current Center Stage control mode.

### Configuring Studio Light

- [studioLightActive](avcapturedevice/isstudiolightactive.md) — A Boolean value that indicates whether Studio Light is active on a device.
- [studioLightEnabled](avcapturedevice/isstudiolightenabled.md) — A Boolean value that indicates whether a user enabled Studio Light on a device.

### Inspecting the Portrait Effect settings

- [portraitEffectActive](avcapturedevice/isportraiteffectactive.md) — A Boolean value that indicates whether the Portrait video effect is active on a device.
- [portraitEffectEnabled](avcapturedevice/isportraiteffectenabled.md) — A Boolean value that indicates whether the user enabled the Portrait video effect in Control Center.

### Inspecting the microphone mode

- [activeMicrophoneMode](avcapturedevice/activemicrophonemode.md) — The device’s active microphone mode.
- [preferredMicrophoneMode](avcapturedevice/preferredmicrophonemode.md) — The microphone mode that the user selects in Control Center.
- [MicrophoneMode](avcapturedevice/microphonemode.md) — Constants that define the available microphone modes.

### Presenting the configuration user interface

- [+ showSystemUserInterface:](<avcapturedevice/showsystemuserinterface(__).md>) — Displays the system’s user interface to configure video effects or microphone modes.
- [SystemUserInterface](avcapturedevice/systemuserinterface.md) — Constants that describe the capture device configuration user interfaces.

### Configuring background replacement

- [backgroundReplacementActive](avcapturedevice/isbackgroundreplacementactive.md) — A Boolean value that indicates whether Background Replacement is currently active on a capture device.
- [backgroundReplacementEnabled](avcapturedevice/isbackgroundreplacementenabled.md) — A class property that indicates whether a person enables the Background Replacement feature for this app.

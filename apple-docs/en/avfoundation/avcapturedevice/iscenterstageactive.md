---
title: isCenterStageActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/iscenterstageactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscenterstageactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iscenterstageactive.json'
content_hash: 'sha256:e0a82b9cdb261217'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isCenterStageActive

<sub>Instance Property</sub>

A Boolean value that indicates whether Center Stage is active on a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCenterStageActive: Bool { get }
```

## Discussion

When Center Stage is active, the camera automatically pans, tightens, or widens the field of view as it requires to keep people optimally framed. If an app or a user enables Center Stage, this property value is [true](../../swift/true.md) if the device supports the feature in its current configuration.

The system imposes the following restrictions on a device when Center Stage is active:

- It limits the range of values the device supports for its [minAvailableVideoZoomFactor](minavailablevideozoomfactor.md) and [maxAvailableVideoZoomFactor](maxavailablevideozoomfactor.md) properties to those of the active capture format’s [videoMinZoomFactorForCenterStage](format/videominzoomfactorforcenterstage.md) and [videoMaxZoomFactorForCenterStage](format/videomaxzoomfactorforcenterstage.md), respectively.
- It limits the [activeVideoMinFrameDuration](activevideominframeduration.md) and [activeVideoMaxFrameDuration](activevideomaxframeduration.md) to the value set by the active capture format’s [videoFrameRateRangeForCenterStage](format/videoframeraterangeforcenterstage.md) property.

The system deactivates Center Stage in the following cases:

- You enable depth data delivery on a capture output, such as [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) or [AVCapturePhotoOutput](../avcapturephotooutput.md).
- The device supports geometric distortion correction, but you haven’t enabled it by setting the value of [geometricDistortionCorrectionEnabled](isgeometricdistortioncorrectionenabled.md) to [true](../../swift/true.md).

This property is key-value observable.

## See Also

### Configuring Center Stage

- [centerStageEnabled](iscenterstageenabled.md) — A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [centerStageRectOfInterest](centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [centerStageControlMode](centerstagecontrolmode-swift.type.property.md) — A value that indicates the current mode of Center Stage control.
- [CenterStageControlMode](centerstagecontrolmode-swift.enum.md) — Constants that indicate the current Center Stage control mode.

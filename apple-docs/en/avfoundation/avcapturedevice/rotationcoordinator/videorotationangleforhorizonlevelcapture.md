---
title: videoRotationAngleForHorizonLevelCapture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.json'
content_hash: 'sha256:1e09001de25866c4'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# videoRotationAngleForHorizonLevelCapture

<sub>Instance Property</sub>

An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoRotationAngleForHorizonLevelCapture: CGFloat { get }
```

## Discussion

Your app can get immediate rotation angle updates from the rotation coordinator with key-value observation (KVO) of this property. The system calls key-value observation code on the main queue so that it has the same behavior as the [videoRotationAngleForHorizonLevelPreview](videorotationangleforhorizonlevelpreview.md) property.

Apps typically apply the property’s value to an [AVCaptureConnection](../../avcaptureconnection.md) instance’s [videoRotationAngle](../../avcaptureconnection/videorotationangle.md) property, such as saving photos and videos with the correction rotation with [AVCapturePhotoOutput](../../avcapturephotooutput.md) and [AVCaptureMovieFileOutput](../../avcapturemoviefileoutput.md), respectively.

Alternatively, if your app uses an [AVCaptureVideoDataOutput](../../avcapturevideodataoutput.md) instance with an [AVAssetWriter](../../avassetwriter.md), such as for recording custom videos with effects, don’t rotate the video with [AVCaptureConnection](../../avcaptureconnection.md). Instead, set the rotation with an [AVAssetWriterInput](../../avassetwriterinput.md) instance’s [transform](../../avassetwriterinput/transform.md) property, which alters the output file’s metadata. With this approach, video-playing apps apply the rotation during playback, which uses less energy than rotating each frame with the capture connection.

> [!note] Note
> Your app needs to convert the [videoRotationAngleForHorizonLevelCapture](videorotationangleforhorizonlevelcapture.md) value from degrees to radians for an asset writer input’s transform, which is a [CGAffineTransform](../../../coregraphics/cgaffinetransform.md).

## See Also

### Compensating for a device’s rotation

- [videoRotationAngleForHorizonLevelPreview](videorotationangleforhorizonlevelpreview.md) — An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.

---
title: videoRotationAngleForHorizonLevelPreview
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.json'
content_hash: 'sha256:1839faf8213d8acb'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [RotationCoordinator](../rotationcoordinator.md)

# videoRotationAngleForHorizonLevelPreview

<sub>Instance Property</sub>

An angle the coordinator provides your app to apply to the preview layer so that it’s level relative to gravity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoRotationAngleForHorizonLevelPreview: CGFloat { get }
```

## Discussion

Your app can get immediate rotation angle updates from the rotation coordinator with key-value observation (KVO) for this property. You can immediately update your app’s UI from its key-value observation code because the rotation coordinator notifies your app on the main queue.

> [!important] Important
> Avoid unnecessary delays and visual artifacts by updating your app’s UI directly from an observer that monitors the property.

Apps typically apply the property’s value to an [AVCaptureConnection](../../avcaptureconnection.md) instance’s [videoRotationAngle](../../avcaptureconnection/videorotationangle.md) property, such as displaying a camera preview with the correction for an [AVCaptureVideoPreviewLayer](../../avcapturevideopreviewlayer.md) instance.

Alternatively, if your app uses an [AVCaptureVideoDataOutput](../../avcapturevideodataoutput.md) instance to display a custom camera preview, such as with effects, don’t rotate the video with [AVCaptureConnection](../../avcaptureconnection.md). Instead, set the rotation in your [CALayer](../../../quartzcore/calayer.md) instance’s [transform](../../../quartzcore/calayer/transform.md) property, such as with an [AVSampleBufferDisplayLayer](../../avsamplebufferdisplaylayer.md) instance. This approach uses less energy than rotating each frame with the capture connection.

> [!note] Note
> Your app needs to convert the [videoRotationAngleForHorizonLevelPreview](videorotationangleforhorizonlevelpreview.md) value from degrees to radians for an asset writer layer’s transform, which is a [CATransform3D](../../../quartzcore/catransform3d.md).

## See Also

### Compensating for a device’s rotation

- [videoRotationAngleForHorizonLevelCapture](videorotationangleforhorizonlevelcapture.md) — An angle the coordinator provides your app to apply to photos or videos it captures with the device so that they’re level relative to gravity.

---
title: videoRotationAngle
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/videorotationangle
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videorotationangle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videorotationangle.json'
content_hash: 'sha256:44ecc24daf5f043d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoRotationAngle

<sub>Instance Property</sub>

A rotation angle the connection applies to a video flowing through it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var videoRotationAngle: CGFloat { get set }
```

## Discussion

Your app can set a video rotation angle that it gets from an [RotationCoordinator](../avcapturedevice/rotationcoordinator.md) instance’s [videoRotationAngleForHorizonLevelCapture](../avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) or [videoRotationAngleForHorizonLevelPreview](../avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) property. The rotation angle only applies to video or depth connections, similar to [videoMirrored](isvideomirrored.md), and can be any angle that [- isVideoRotationAngleSupported:](<isvideorotationanglesupported(__).md>) returns [true](../../swift/true.md) for.

Not all capture connections rotate each frame. For example, a video connection to an [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md) or [AVCapturePhotoOutput](../avcapturephotooutput.md) instance applies a rotation with a QuickTime track matrix or with EXIF tags, respectively.

Capture connections to [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) and [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) instances rotate video frames they provide to their [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) and [- depthDataOutput:didOutputDepthData:timestamp:connection:](<../avcapturedepthdataoutputdelegate/depthdataoutput(__didoutput_timestamp_connection_).md>) delegate methods, respectively. Each [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) instance uses hardware acceleration to rotate every frame.

> [!tip] Tip
> Avoid potential performance issues by only rotating video with a capture connection when necessary.

You can rotate the video of a movie file you record with an [AVAssetWriter](../avassetwriter.md) instance by applying the rotation to an [AVAssetWriterInput](../avassetwriterinput.md) instance’s [transform](../avassetwriterinput/transform.md) property. This approach avoids the performance costs that come with rotating each video frame.

> [!note] Note
> Your app needs to convert the [videoRotationAngleForHorizonLevelCapture](../avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelcapture.md) or [videoRotationAngleForHorizonLevelPreview](../avcapturedevice/rotationcoordinator/videorotationangleforhorizonlevelpreview.md) value from degrees to radians for transform properties.

## See Also

### Rotating a video

- [- isVideoRotationAngleSupported:](<isvideorotationanglesupported(__).md>) — Returns a Boolean value that indicates whether the connection supports a rotation angle.

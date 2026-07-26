---
title: isVideoMirrored
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureconnection/isvideomirrored
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/isvideomirrored'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/isvideomirrored.json'
content_hash: 'sha256:2f9782a4f3a8f18f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# isVideoMirrored

<sub>Instance Property</sub>

A Boolean value that indicates whether the connection horizontally flips the video flowing through it.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isVideoMirrored: Bool { get set }
```

## Discussion

You can apply a mirror-image effect to a video flowing through the connection by setting the value to [true](../../swift/true.md). The mirroring effect only applies to video or depth connections, similar to [videoRotationAngle](videorotationangle.md), and if [supportsVideoMirroring](isvideomirroringsupported.md) is [true](../../swift/true.md).

Not all capture connections mirror each frame. For example, a video connection to an [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md) or [AVCapturePhotoOutput](../avcapturephotooutput.md) instance applies the mirror effect with a QuickTime track matrix or with EXIF tags, respectively.

Capture connections to [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) and [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) instances mirror video frames they provide to their [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) and [- depthDataOutput:didOutputDepthData:timestamp:connection:](<../avcapturedepthdataoutputdelegate/depthdataoutput(__didoutput_timestamp_connection_).md>) delegate methods, respectively. Each [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) instance uses hardware acceleration to mirror every frame.

> [!tip] Tip
> Avoid potential performance issues by only mirroring video with a capture connection when necessary.

You can mirror the video of a movie file you record with an [AVAssetWriter](../avassetwriter.md) instance by applying a scale factor to the [transform](../avassetwriterinput/transform.md) property of its [AVAssetWriterInput](../avassetwriterinput.md). For example, you can horizontally flip an image by scaling the x-axis by `-1`. This approach avoids the performance costs that come with rotating each video frame.

```swift
func horizontallyFlipInput(_ assetInput: AVAssetWriterInput) {
    let horiztonalFlip = CGAffineTransform(scaleX: -1.0, y: 1.0)

    assetInput.transform = assetInput.transform.concatenating(horiztonalFlip)
}
```

## See Also

### Mirroring a video

- [supportsVideoMirroring](isvideomirroringsupported.md) — A Boolean value that indicates whether the connection supports video mirroring.
- [automaticallyAdjustsVideoMirroring](automaticallyadjustsvideomirroring.md) — A Boolean value that indicates whether you can enable mirroring based on a session’s configuration.

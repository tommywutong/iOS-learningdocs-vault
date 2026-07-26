---
title: videoOrientation
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（17.0 起废弃）, iPadOS 4.0+（17.0 起废弃）, Mac Catalyst 14.0+（17.0 起废弃）, macOS 10.7+（14.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureconnection/videoorientation
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureconnection/videoorientation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureconnection/videoorientation.json'
content_hash: 'sha256:7cd727215e303029'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureConnection](../avcaptureconnection.md)

# videoOrientation

<sub>Instance Property</sub>

An orientation that tells the connection how to rotate a video flowing through it.

> [!warning] Deprecated
> See [videoRotationAngle](videorotationangle.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var videoOrientation: AVCaptureVideoOrientation { get set }
```

## Discussion

The property only applies to a video connection.

If the value of [supportsVideoOrientation](isvideoorientationsupported.md) is [true](../../swift/true.md), you can set `videoOrientation` to rotate the video buffers consumed by the connection’s output. Setting `videoOrientation` doesn’t necessarily result in a physical rotation of video buffers. For example, a video connection to an [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md) object handles orientation using a QuickTime track matrix. A video connection to an [AVCaptureStillImageOutput](../avcapturestillimageoutput.md) object handles orientation using EXIF tags.

[AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) clients may receive physically rotated pixel buffers in their [- captureOutput:didOutputSampleBuffer:fromConnection:](<../avcapturevideodataoutputsamplebufferdelegate/captureoutput(__didoutput_from_).md>) delegate callback. The `AVCaptureVideoDataOutput` hardware accelerates the rotation operation and supports all four [AVCaptureVideoOrientation](../avcapturevideoorientation.md) modes. A client sets `videoOrientation` or [videoMirrored](isvideomirrored.md) on the video data output’s video [AVCaptureConnection](../avcaptureconnection.md) to request physical buffer rotation.

> [!important] Important
> Physically rotating buffers comes with a performance cost, so only request rotation when necessary. If you want to write rotated video to a movie file using [AVAssetWriter](../avassetwriter.md), set the [transform](../avassetwriterinput/transform.md) property on the [AVAssetWriterInput](../avassetwriterinput.md) instead.

## See Also

### Deprecated

- [videoStabilizationEnabled](isvideostabilizationenabled.md) — A Boolean value that indicates whether video stabilization is active for the connection. _(deprecated)_
- [enablesVideoStabilizationWhenAvailable](enablesvideostabilizationwhenavailable.md) — A Boolean value that indicates whether the system enables video stabilization when it’s available. _(deprecated)_
- [supportsVideoOrientation](isvideoorientationsupported.md) — A Boolean value that indicates whether the connection supports changing the orientation of the video. _(deprecated)_
- [AVCaptureVideoOrientation](../avcapturevideoorientation.md) — Constants indicating video orientation. _(deprecated)_

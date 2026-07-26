---
title: 'canAddOutput(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturesession/canaddoutput(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturesession/canaddoutput(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturesession/canaddoutput%28_%3A%29.json'
content_hash: 'sha256:e990168b59bce4b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureSession](../avcapturesession.md)

# canAddOutput(_:)

<sub>Instance Method</sub>

Determines whether you can add an output to a session.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func canAddOutput(_ output: AVCaptureOutput) -> Bool
```

## Parameters

- `output` — An output to add to the session.

## Return Value

[true](../../swift/true.md) if you can add the output; otherwise [false](../../swift/false.md).

## Discussion

In iOS and Mac Catalyst, the system imposes the following limitations on the combinations of outputs a capture session may contain:

- An app may add only a single output of a particular type. For apps that link against iOS 16 or later, this restriction no longer applies to [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md).
- Prior to iOS 16, you can add an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) and an [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md) to the same session, but only one may have its connection active. If you attempt to enable both connections, the system chooses the movie file output as the active connection and disables the video data output’s connection. For apps that link against iOS 16 or later, this restriction no longer exists.
- Similarly, prior to iOS 16, you can add an [AVCaptureAudioDataOutput](../avcaptureaudiodataoutput.md) and an [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md) to the same session, but only one may have its connection active. If you attempt to enable both connections, the system chooses the movie file output and disables the audio data output’s connection. For apps that link against iOS 16 or later, this restriction no longer exists.
- An app can’t add an [AVCapturePhotoOutput](../avcapturephotooutput.md) and [AVCaptureStillImageOutput](../avcapturestillimageoutput.md) to the same session.

> [!important] Important
> If you configure a capture session to use more than one [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md) instance, monitor the value of the capture session’s [hardwareCost](hardwarecost.md) property and reconfigure the session as appropriate.

## See Also

### Configuring outputs

- [outputs](outputs.md) — The output destinations to which a captures session sends its data.
- [- addOutput:](<addoutput(__).md>) — Adds an output to the capture session.
- [- removeOutput:](<removeoutput(__).md>) — Removes an output from a capture session.

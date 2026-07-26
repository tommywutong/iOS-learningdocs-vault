---
title: isCinematicVideoCaptureSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/iscinematicvideocapturesupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/iscinematicvideocapturesupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/iscinematicvideocapturesupported.json'
content_hash: 'sha256:cf65ce9f75806b20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# isCinematicVideoCaptureSupported

<sub>Instance Property</sub>

A BOOL value specifying whether Cinematic Video capture is supported.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isCinematicVideoCaptureSupported: Bool { get }
```

## Discussion

With Cinematic Video capture, you get a simulated depth-of-field effect that keeps your subjects (people, pets, and more) in sharp focus while applying a pleasing blur to the background (or foreground). Depending on the focus mode (see [CinematicVideoFocusMode](../avcapturedevice/cinematicvideofocusmode.md) for detail), the camera either uses machine learning to automatically detect and focus on subjects in the scene, or it fixes focus on a subject until it exits the scene. Cinematic Videos can be played back and edited using the Cinematic framework.

You can adjust the video’s simulated aperture before starting a recording using the [simulatedAperture](simulatedaperture.md) property. With Cinematic Video specific focus methods on [AVCaptureDevice](../avcapturedevice.md), you can dynamically control focus transitions.

Movie files captured with Cinematic Video enabled can be played back and edited with the [Cinematic framework] (https://developer.apple.com/documentation/cinematic/playing-and-editing-cinematic-mode-video?language=objc).

This property returns `true` if the session’s current configuration allows Cinematic Video capture. When switching cameras or formats, this property may change. When this property changes from `true` to `false`, [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) also reverts to `false`. If you’ve previously opted in for Cinematic Video capture and then change configuration, you may need to set [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) to `true` again. This property is key-value observable.

> [!note] Note
> [AVCaptureDepthDataOutput](../avcapturedepthdataoutput.md) is not supported when [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) is set to `true`. Running an [AVCaptureSession](../avcapturesession.md) with both of these features throws an `NSInvalidArgumentException`.

## See Also

### Configuring Cinematic video capture

- [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) — A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.
- [simulatedAperture](simulatedaperture.md) — Shallow depth of field simulated aperture.

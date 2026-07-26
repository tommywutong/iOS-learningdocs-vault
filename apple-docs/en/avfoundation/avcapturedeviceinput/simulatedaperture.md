---
title: simulatedAperture
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/simulatedaperture
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/simulatedaperture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/simulatedaperture.json'
content_hash: 'sha256:cbf14cd075963aab'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# simulatedAperture

<sub>Instance Property</sub>

Shallow depth of field simulated aperture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var simulatedAperture: Float { get set }
```

## Discussion

When capturing a Cinematic Video, use this property to control the amount of blur in the simulated depth of field effect.

This property only takes effect when [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) is set to `true`.

> [!important] Important
> Setting this property to a value less than the `AVCaptureDevice/activeFormat/minSimulatedAperture` or greater than the `AVCaptureDevice/activeFormat/maxSimulatedAperture` throws an `NSRangeException`. you may only set this property if `AVCaptureDevice/activeFormat/minSimulatedAperture` returns a non-zero value, otherwise an `NSInvalidArgumentException` is thrown. You must set this property before starting a Cinematic Video capture. If you attempt to set it while a recording is in progress, an `NSInvalidArgumentException` is thrown.

This property is initialized to the associated `AVCaptureDevice/activeFormat/defaultSimulatedAperture`.

This property is key-value observable.

## See Also

### Configuring Cinematic video capture

- [cinematicVideoCaptureSupported](iscinematicvideocapturesupported.md) — A BOOL value specifying whether Cinematic Video capture is supported.
- [cinematicVideoCaptureEnabled](iscinematicvideocaptureenabled.md) — A BOOL value specifying whether the Cinematic Video effect is being applied to any movie file output, video data output, metadata output, or video preview layer added to the capture session.

---
title: activeFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/activeformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/activeformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/activeformat.json'
content_hash: 'sha256:740e2db885aa1771'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# activeFormat

<sub>Instance Property</sub>

The capture format in use by the device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var activeFormat: AVCaptureDevice.Format { get set }
```

## Discussion

In iOS, a device’s active format and a capture session’s [sessionPreset](../avcapturesession/sessionpreset.md) are mutually exclusive. If you set a device’s active format, the session to which it’s attached changes its preset to [AVCaptureSessionPresetInputPriority](../avcapturesession/preset/inputpriority.md). Likewise if you set a preset on a capture session, the session assumes control of its input devices, and configures their active format appropriately.

> [!note] Note
> Audio devices don’t expose any user-configurable formats in iOS. To configure audio input on iOS, use [AVAudioSession](../../avfaudio/avaudiosession.md) and its related APIs instead.

Set the [activeFormat](activeformat.md), [activeVideoMinFrameDuration](activevideominframeduration.md), and [activeVideoMaxFrameDuration](activevideomaxframeduration.md) properties simultaneously by performing the configuration between calls to the session’s [- beginConfiguration](<../avcapturesession/beginconfiguration().md>) and [- commitConfiguration](<../avcapturesession/commitconfiguration().md>) methods.

```swift
// Configure capture session.
captureSession.beginConfiguration()

do {
    try device.lockForConfiguration()
    
    // Set the device's active format.
    device.activeFormat = // a supported format.
    
    // Set the device's min/max frame duration.
    device.activeVideoMinFrameDuration = // a supported minimum duration.
    device.activeVideoMaxFrameDuration = // a supported maximum duration.
    
    device.unlockForConfiguration()
} catch {
    // Handle error.
}

// Apply the changes to the session.
captureSession.commitConfiguration()
```

If you configure a session to use an active format intended for high resolution still photography, and you apply zoom, orientation, or format changes to an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md), the system may not meet the target framerate.

This property is key-value observable.

## See Also

### Configuring capture formats

- [formats](formats.md) — The capture formats a device supports.
- [activeDepthDataFormat](activedepthdataformat.md) — The currently active depth data format of the capture device.
- [Format](format.md) — A class that defines media formats and capture settings that capture devices support.

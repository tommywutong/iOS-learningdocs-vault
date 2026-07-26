---
title: 'photoOutput(_:willCapturePhotoFor:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willcapturephotofor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Awillcapturephotofor%3A%29.json'
content_hash: 'sha256:b200365e37e51704'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:willCapturePhotoFor:)

<sub>Instance Method</sub>

Notifies the delegate that photo capture is about to occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, willCapturePhotoFor resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Parameters

- `output` — The photo output performing the capture.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## Discussion

The photo output calls this method as close as possible to the initial moment of capture. If the shutter sound is enabled, this call occurs immediately after the photo output begins playing the shutter sound.

> [!note] Note
> Live Photo capture disables the shutter sound. In some regions, the device’s mute switch can disable the shutter sound.

## See Also

### Monitoring capture progress

- [- captureOutput:willBeginCaptureForResolvedSettings:](<photooutput(__willbegincapturefor_).md>) — Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [- captureOutput:didCapturePhotoForResolvedSettings:](<photooutput(__didcapturephotofor_).md>) — Notifies the delegate that the photo has been taken.
- [- captureOutput:didFinishCaptureForResolvedSettings:error:](<photooutput(__didfinishcapturefor_error_).md>) — Notifies the delegate that the capture process is complete.

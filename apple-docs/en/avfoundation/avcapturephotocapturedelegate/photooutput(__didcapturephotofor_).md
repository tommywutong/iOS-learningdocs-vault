---
title: 'photoOutput(_:didCapturePhotoFor:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didcapturephotofor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidcapturephotofor%3A%29.json'
content_hash: 'sha256:12c6936adbf3ffb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didCapturePhotoFor:)

<sub>Instance Method</sub>

Notifies the delegate that the photo has been taken.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didCapturePhotoFor resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Parameters

- `output` — The photo output performing the capture.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## Discussion

The photo output calls this method as soon as the first step of capture ends—that is, at the end of the photographic exposure time.

## See Also

### Monitoring capture progress

- [- captureOutput:willBeginCaptureForResolvedSettings:](<photooutput(__willbegincapturefor_).md>) — Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [- captureOutput:willCapturePhotoForResolvedSettings:](<photooutput(__willcapturephotofor_).md>) — Notifies the delegate that photo capture is about to occur.
- [- captureOutput:didFinishCaptureForResolvedSettings:error:](<photooutput(__didfinishcapturefor_error_).md>) — Notifies the delegate that the capture process is complete.

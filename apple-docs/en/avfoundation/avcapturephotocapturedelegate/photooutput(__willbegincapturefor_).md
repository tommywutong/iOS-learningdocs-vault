---
title: 'photoOutput(_:willBeginCaptureFor:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:willbegincapturefor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Awillbegincapturefor%3A%29.json'
content_hash: 'sha256:26fca578638355e5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:willBeginCaptureFor:)

<sub>Instance Method</sub>

Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, willBeginCaptureFor resolvedSettings: AVCaptureResolvedPhotoSettings)
```

## Parameters

- `output` — The photo output performing the capture.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

## Discussion

The photo output calls this method when it has committed to a choice of settings and will soon begin the capture process. This call occurs as early as possible after your call to the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method, letting you know what to expect for other delegate method calls related to the same capture.

Use this method and the [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) it provides to find out at the earliest possible opportunity which values the photo output has chosen for automatic settings, and what the output dimensions for captured images and movies will be. For example, if you requested capture with the [flashMode](../avcapturephotosettings/flashmode.md) property set to [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md), the resolved photo settings’ [flashEnabled](../avcaptureresolvedphotosettings/isflashenabled.md) property indicates whether the flash will fire during capture.

## See Also

### Monitoring capture progress

- [- captureOutput:willCapturePhotoForResolvedSettings:](<photooutput(__willcapturephotofor_).md>) — Notifies the delegate that photo capture is about to occur.
- [- captureOutput:didCapturePhotoForResolvedSettings:](<photooutput(__didcapturephotofor_).md>) — Notifies the delegate that the photo has been taken.
- [- captureOutput:didFinishCaptureForResolvedSettings:error:](<photooutput(__didfinishcapturefor_error_).md>) — Notifies the delegate that the capture process is complete.

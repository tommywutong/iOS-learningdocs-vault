---
title: 'photoOutput(_:didFinishCaptureFor:error:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotocapturedelegate/photooutput(_:didfinishcapturefor:error:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotocapturedelegate/photooutput%28_%3Adidfinishcapturefor%3Aerror%3A%29.json'
content_hash: 'sha256:c9b5bfe7bec7d346'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md)

# photoOutput(_:didFinishCaptureFor:error:)

<sub>Instance Method</sub>

Notifies the delegate that the capture process is complete.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
optional func photoOutput(_ output: AVCapturePhotoOutput, didFinishCaptureFor resolvedSettings: AVCaptureResolvedPhotoSettings, error: (any Error)?)
```

## Parameters

- `output` — The photo output performing the capture.

- `resolvedSettings` — An object describing the settings used for this capture. Match this object’s [uniqueID](../avcapturephotosettings/uniqueid.md) value to the [uniqueID](../avcapturephotosettings/uniqueid.md) property of the photo settings object you initiated capture with to determine which capture request this delegate call corresponds to. You can also use this object to find out which values the photo output has chosen for automatic settings.

- `error` — If the capture process did not complete successfully, an error object describing the failure; otherwise, `nil`.

## Discussion

The photo output calls this method when the entire capture process has finished, and no more delegate messages will be sent for this capture request. Use this time to clean up any resources you’ve allocated that relate to this capture request.

## See Also

### Monitoring capture progress

- [- captureOutput:willBeginCaptureForResolvedSettings:](<photooutput(__willbegincapturefor_).md>) — Notifies the delegate that the capture output has resolved settings and will soon begin its capture process.
- [- captureOutput:willCapturePhotoForResolvedSettings:](<photooutput(__willcapturephotofor_).md>) — Notifies the delegate that photo capture is about to occur.
- [- captureOutput:didCapturePhotoForResolvedSettings:](<photooutput(__didcapturephotofor_).md>) — Notifies the delegate that the photo has been taken.

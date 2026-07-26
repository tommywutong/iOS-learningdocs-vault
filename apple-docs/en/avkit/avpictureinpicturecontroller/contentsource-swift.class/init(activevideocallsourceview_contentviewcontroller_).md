---
title: 'init(activeVideoCallSourceView:contentViewController:)'
framework: AVKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init(activevideocallsourceview:contentviewcontroller:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/contentsource-swift.class/init%28activevideocallsourceview%3Acontentviewcontroller%3A%29.json'
content_hash: 'sha256:c4e5806d31d5db0f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVKit](../../../avkit.md) · [AVPictureInPictureController](../../avpictureinpicturecontroller.md) · [ContentSource](../contentsource-swift.class.md)

# init(activeVideoCallSourceView:contentViewController:)

<sub>Initializer</sub>

Creates a content source with an active video call.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
init(activeVideoCallSourceView sourceView: UIView, contentViewController: AVPictureInPictureVideoCallViewController)
```

## Parameters

- `sourceView` — A view that contains the content of the video call.

- `contentViewController` — The view controller to appear in the system’s Picture in Picture window.

## Discussion

The instance is only valid for the duration of the call.

> [!important] Important
> In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [isMultitaskingCameraAccessEnabled](../../../avfoundation/avcapturesession/ismultitaskingcameraaccessenabled.md) property. Apps that have a deployment target earlier than iOS 16 require the [com.apple.developer.avfoundation.multitasking-camera-access](../../../bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement to use the camera in PiP mode.

## See Also

### Creating a Content Source

- [- initWithPlayerLayer:](<init(playerlayer_).md>) — Creates a content source with a player layer.
- [- initWithSampleBufferDisplayLayer:playbackDelegate:](<init(samplebufferdisplaylayer_playbackdelegate_).md>) — Creates a content source with a sample buffer display layer.

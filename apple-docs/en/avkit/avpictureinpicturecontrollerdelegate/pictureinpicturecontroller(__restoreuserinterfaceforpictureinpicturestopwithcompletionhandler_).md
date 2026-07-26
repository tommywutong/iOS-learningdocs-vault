---
title: 'pictureInPictureController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)'
framework: AVKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller(_:restoreuserinterfaceforpictureinpicturestopwithcompletionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontrollerdelegate/pictureinpicturecontroller%28_%3Arestoreuserinterfaceforpictureinpicturestopwithcompletionhandler%3A%29.json'
content_hash: 'sha256:f9875011f50e24ee'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureControllerDelegate](../avpictureinpicturecontrollerdelegate.md)

# pictureInPictureController(_:restoreUserInterfaceForPictureInPictureStopWithCompletionHandler:)

<sub>Instance Method</sub>

Tells the delegate to restore the user interface before Picture in Picture stops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController, restoreUserInterfaceForPictureInPictureStopWithCompletionHandler completionHandler: @escaping @Sendable (Bool) -> Void)
```

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
optional func pictureInPictureController(_ pictureInPictureController: AVPictureInPictureController) async -> Bool
```

## Parameters

- `pictureInPictureController` — The delegating controller.

- `completionHandler` — You must call the completion handler with a value of `true` to allow the system to finish restoring your player user interface.

## Discussion

Implement this method if your player user interface requires configuration or layout to return to its default state.

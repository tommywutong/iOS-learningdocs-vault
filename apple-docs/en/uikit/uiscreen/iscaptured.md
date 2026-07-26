---
title: isCaptured
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（27.0 起废弃）, iPadOS 11.0+（27.0 起废弃）, Mac Catalyst 13.1+（27.0 起废弃）, tvOS 11.0+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uiscreen/iscaptured
source_url: 'https://developer.apple.com/documentation/uikit/uiscreen/iscaptured'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiscreen/iscaptured.json'
content_hash: 'sha256:5eb21c8dda5acb91'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIScreen](../uiscreen.md)

# isCaptured

<sub>Instance Property</sub>

A Boolean value that indicates whether the system is actively cloning the screen to another destination.

> [!warning] Deprecated
> Use [sceneCaptureState](../uitraitcollection/scenecapturestate.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isCaptured: Bool { get }
```

## Discussion

A value of `YES` indicates the system is actively recording, mirroring, or using AirPlay to stream the contents of the screen.

Observe this property and optionally take an appropriate action in your app to prevent the capture of your content. For example, a media app might stop any current media playback and present a dialog to the user describing the reason for the pause.

> [!important] Important
> The system doesn’t include video content encrypted using [FairPlay Streaming](https://developer.apple.com/streaming/fps/) (FPS) when recording, mirroring, or using AirPlay to stream the contents of the screen. However, although it blacks out FPS-encrypted video content, it includes FPS-encrypted audio content. To prevent the system from recording the audio portion, observe the `isCaptured` property and take appropriate action in your app as described above.

UIKit sends the [UIScreenCapturedDidChangeNotification](captureddidchangenotification.md) notification when the capture status of the screen changes.

## See Also

### Related Documentation

- [UIApplicationUserDidTakeScreenshotNotification](../uiapplication/userdidtakescreenshotnotification.md) — A notification that posts when a person takes a screenshot on the device.

### Detecting screen capture

- [mirroredScreen](mirrored.md) — The screen an external display mirrors from.

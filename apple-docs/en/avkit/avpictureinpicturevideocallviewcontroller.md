---
title: AVPictureInPictureVideoCallViewController
framework: AVKit
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturevideocallviewcontroller
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturevideocallviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturevideocallviewcontroller.json'
content_hash: 'sha256:7bcb6182370e57c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVKit](../avkit.md)

# AVPictureInPictureVideoCallViewController

<sub>Class</sub>

A view controller that presents content from a video call in Picture in Picture.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
class AVPictureInPictureVideoCallViewController
```

## Overview

> [!important] Important
> In iOS 16 and later, you can use the camera in Picture in Picture mode by enabling a capture session’s [isMultitaskingCameraAccessEnabled](../avfoundation/avcapturesession/ismultitaskingcameraaccessenabled.md) property. Apps that have a deployment target earlier than iOS 16 require the [com.apple.developer.avfoundation.multitasking-camera-access](../bundleresources/entitlements/com.apple.developer.avfoundation.multitasking-camera-access.md) entitlement to use the camera in PiP mode.

## Relationships

- **Inherits From**: [UIViewController](../uikit/uiviewcontroller.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCoding](../foundation/nscoding.md), [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [NSTouchBarProvider](../appkit/nstouchbarprovider.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md), [UIAppearanceContainer](../uikit/uiappearancecontainer.md), [UIContentContainer](../uikit/uicontentcontainer.md), [UIFocusEnvironment](../uikit/uifocusenvironment.md), [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md), [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md), [UIStateRestoring](../uikit/uistaterestoring.md), [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md), [UITraitEnvironment](../uikit/uitraitenvironment.md), [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

### Accessing the Active Call Presentation

- [activeVideoCallSourceView](avpictureinpicturecontroller/contentsource-swift.class/activevideocallsourceview.md) — The view that contains the video content of the call.
- [activeVideoCallContentViewController](avpictureinpicturecontroller/contentsource-swift.class/activevideocallcontentviewcontroller.md) — The view controller that presents the video call content.

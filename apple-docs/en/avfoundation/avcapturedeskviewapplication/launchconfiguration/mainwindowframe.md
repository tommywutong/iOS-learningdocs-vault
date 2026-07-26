---
title: mainWindowFrame
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/mainwindowframe
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/mainwindowframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/mainwindowframe.json'
content_hash: 'sha256:a5d24c4a63177b7b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDeskViewApplication](../../avcapturedeskviewapplication.md) · [LaunchConfiguration](../launchconfiguration.md)

# mainWindowFrame

<sub>Instance Property</sub>

The frame for Desk View after it launches.

<sub>Mac Catalyst, macOS</sub>

```swift
var mainWindowFrame: CGRect { get set }
```

## Discussion

The default value is [zero](../../../corefoundation/cgrect/zero.md), which tells the system to use the previously set frame. The system uses global screen coordinates to display the frame. When Desk View launches from a native macOS app, the window origin is bottom-left. When it launches from a [Mac Catalyst](../../../uikit/mac-catalyst.md) app, the window origin is top-left.

## See Also

### Customizing the presentation

- [requiresSetUpModeCompletion](requiressetupmodecompletion.md) — A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

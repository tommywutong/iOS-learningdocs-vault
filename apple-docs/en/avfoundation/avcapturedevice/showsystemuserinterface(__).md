---
title: 'showSystemUserInterface(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/showsystemuserinterface(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/showsystemuserinterface(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/showsystemuserinterface%28_%3A%29.json'
content_hash: 'sha256:cf32cb4ab6872066'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# showSystemUserInterface(_:)

<sub>Type Method</sub>

Displays the system’s user interface to configure video effects or microphone modes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class func showSystemUserInterface(_ systemUserInterface: AVCaptureDevice.SystemUserInterface)
```

## Parameters

- `systemUserInterface` — The system user interface to present.

## Discussion

Use this method to prompt the user to make changes to Video Effects (such as Center Stage or Portrait Effect) or Microphone Modes. It presents the system user interface and deep links to the appropriate module.

Calling this method isn’t a blocking operation. After the system presents the indicated user interface, control returns immediately to the app.

## See Also

### Presenting the configuration user interface

- [SystemUserInterface](systemuserinterface.md) — Constants that describe the capture device configuration user interfaces.

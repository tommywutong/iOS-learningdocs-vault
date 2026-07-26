---
title: requiresSetUpModeCompletion
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 16.1+, macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeskviewapplication/launchconfiguration/requiressetupmodecompletion.json'
content_hash: 'sha256:78ad1c36f9200f04'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDeskViewApplication](../../avcapturedeskviewapplication.md) · [LaunchConfiguration](../launchconfiguration.md)

# requiresSetUpModeCompletion

<sub>Instance Property</sub>

A Boolean value that specifies whether the system requires the user to complete setup mode before it executes the completion handler.

<sub>Mac Catalyst, macOS</sub>

```swift
var requiresSetUpModeCompletion: Bool { get set }
```

## Discussion

The default value is [false](../../../swift/false.md), which tells the system to execute the completion handler as soon as it displays Desk View. If [true](../../../swift/true.md), the system executes the completion handler after the user completes setup and starts Desk View.

## See Also

### Customizing the presentation

- [mainWindowFrame](mainwindowframe.md) — The frame for Desk View after it launches.

---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturecontrol/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturecontrol/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturecontrol/isenabled.json'
content_hash: 'sha256:b651981be824fa73'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureControl](../avcapturecontrol.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether this control supports user interaction.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Controls support user interaction by default. You can temporarily disable user interaction on a control without removing it from a capture session by setting it’s enabled state to `false`.

The default value is `true`.

> [!note] Note
> Apps can programmatically change the value of a control while in a disabled state.

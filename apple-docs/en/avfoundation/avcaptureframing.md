---
title: AVCaptureFraming
framework: AVFoundation
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureframing
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureframing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureframing.json'
content_hash: 'sha256:ab4ef3fcbdb7a18f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCaptureFraming

<sub>Class</sub>

A framing, consisting of an aspect ratio and a zoom factor.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
class AVCaptureFraming
```

## Overview

An [AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md) provides framing recommendations using this object.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting a framing

- [aspectRatio](avcaptureframing/aspectratio.md) — An aspect ratio.
- [zoomFactor](avcaptureframing/zoomfactor.md) — A zoom factor.

## See Also

### Configuring smart framing

- [smartFramingMonitor](avcapturedevice/smartframingmonitor.md) — A monitor owned by the device that recommends an optimal framing based on the content in the scene.
- [AVCaptureSmartFramingMonitor](avcapturesmartframingmonitor.md) — An object associated with a capture device that monitors the scene and suggests an optimal framing.

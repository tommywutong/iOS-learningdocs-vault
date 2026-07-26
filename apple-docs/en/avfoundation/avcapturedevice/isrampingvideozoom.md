---
title: isRampingVideoZoom
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isrampingvideozoom
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isrampingvideozoom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isrampingvideozoom.json'
content_hash: 'sha256:5858b21e6db21d6f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isRampingVideoZoom

<sub>Instance Property</sub>

A Boolean value that indicates whether a zoom transition is in progress.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isRampingVideoZoom: Bool { get }
```

## Discussion

Key-value observe this property to determine when a zoom transitions begins or ends.

---
title: delegate
framework: AVKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avkit/avpictureinpicturecontroller/delegate
source_url: 'https://developer.apple.com/documentation/avkit/avpictureinpicturecontroller/delegate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avkit/avpictureinpicturecontroller/delegate.json'
content_hash: 'sha256:00c9aeb865aeae32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVKit](../../avkit.md) · [AVPictureInPictureController](../avpictureinpicturecontroller.md)

# delegate

<sub>Instance Property</sub>

A delegate object for a Picture in Picture controller.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
weak var delegate: (any AVPictureInPictureControllerDelegate)? { get set }
```

## See Also

### Accessing the Delegate Object

- [AVPictureInPictureControllerDelegate](../avpictureinpicturecontrollerdelegate.md) — A protocol to adopt to respond to Picture in Picture events.

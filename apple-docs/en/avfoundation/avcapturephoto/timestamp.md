---
title: timestamp
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/timestamp
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/timestamp'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/timestamp.json'
content_hash: 'sha256:91a6f02694b28163'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# timestamp

<sub>Instance Property</sub>

The time at which the image was captured.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var timestamp: CMTime { get }
```

## Discussion

This timestamp is always synchronized to the [masterClock](../avcapturesession/masterclock.md) time of the [AVCaptureSession](../avcapturesession.md) object to which the photo output is connected.

## See Also

### Resolving photo capture requests

- [resolvedSettings](resolvedsettings.md) — The settings object that was used to request this photo capture.
- [photoCount](photocount.md) — The 1-based index of this photo capture relative to other results from the same capture request.

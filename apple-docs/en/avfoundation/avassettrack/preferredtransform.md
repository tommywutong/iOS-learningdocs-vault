---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+（16.0 起废弃）, iPadOS 4.0+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, macOS 10.7+（13.0 起废弃）, tvOS 9.0+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）, watchOS 1.0+（9.0 起废弃）]
languages: [swift, occ, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avassettrack/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avassettrack/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avassettrack/preferredtransform.json'
content_hash: 'sha256:32c64a3f56a4d339'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVAssetTrack](../avassettrack.md)

# preferredTransform

<sub>Instance Property</sub>

The track’s transform preference to apply to its visual content during presentation or processing.

> [!warning] Deprecated
> Load the value of [preferredTransform](../avpartialasyncproperty/preferredtransform-90jdn.md) asynchronously instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get }
```

## Discussion

The value of this property is typically, but not always, [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md).

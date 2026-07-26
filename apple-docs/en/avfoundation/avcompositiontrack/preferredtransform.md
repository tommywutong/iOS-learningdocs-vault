---
title: preferredTransform
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcompositiontrack/preferredtransform
source_url: 'https://developer.apple.com/documentation/avfoundation/avcompositiontrack/preferredtransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcompositiontrack/preferredtransform.json'
content_hash: 'sha256:6391af4dacacd207'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCompositionTrack](../avcompositiontrack.md)

# preferredTransform

<sub>Instance Property</sub>

The track’s transform preference to apply to its visual content during presentation or processing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var preferredTransform: CGAffineTransform { get }
```

## Discussion

The value of this property is typically, but not always, [CGAffineTransformIdentity](../../coregraphics/cgaffinetransformidentity.md).

## See Also

### Accessing visual characteristics

- [naturalSize](naturalsize.md) — The natural dimensions of the media data that the track references.

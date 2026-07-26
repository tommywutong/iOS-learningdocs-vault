---
title: timeRange
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/scene/timerange
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene/timerange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/scene/timerange.json'
content_hash: 'sha256:44de86479e182390'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptionRenderer](../../avcaptionrenderer.md) · [Scene](../scene.md)

# timeRange

<sub>Instance Property</sub>

The time range during which the system doesn’t modify the scene.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var timeRange: CMTimeRange { get }
```

## See Also

### Inspecting the scene

- [hasActiveCaptions](hasactivecaptions.md) — A Boolean value that indicates whether the scene contains one or more active captions.
- [needsPeriodicRefresh](needsperiodicrefresh.md) — A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

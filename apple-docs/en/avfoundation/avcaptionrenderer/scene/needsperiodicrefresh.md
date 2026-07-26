---
title: needsPeriodicRefresh
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/scene/needsperiodicrefresh
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene/needsperiodicrefresh'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/scene/needsperiodicrefresh.json'
content_hash: 'sha256:55b1c7c83b3fe04b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptionRenderer](../../avcaptionrenderer.md) · [Scene](../scene.md)

# needsPeriodicRefresh

<sub>Instance Property</sub>

A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var needsPeriodicRefresh: Bool { get }
```

## Discussion

If your app isn’t progressing through the content, a single render at the current time is enough.

Choose a refresh rate appropriate for your app. For example, an app may choose rates that match rates of associated video frames or other timing appropriate for the client.

## See Also

### Inspecting the scene

- [timeRange](timerange.md) — The time range during which the system doesn’t modify the scene.
- [hasActiveCaptions](hasactivecaptions.md) — A Boolean value that indicates whether the scene contains one or more active captions.

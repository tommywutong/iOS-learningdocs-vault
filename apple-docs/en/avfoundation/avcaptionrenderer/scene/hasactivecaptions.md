---
title: hasActiveCaptions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 15.0+, macOS 12.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptionrenderer/scene/hasactivecaptions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptionrenderer/scene/hasactivecaptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptionrenderer/scene/hasactivecaptions.json'
content_hash: 'sha256:844b5a5a6aff579f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptionRenderer](../../avcaptionrenderer.md) · [Scene](../scene.md)

# hasActiveCaptions

<sub>Instance Property</sub>

A Boolean value that indicates whether the scene contains one or more active captions.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var hasActiveCaptions: Bool { get }
```

## Discussion

Knowing when the renderer has active captions can be useful to scrub to times where captions are present, or skip scenes where no captions exist.

> [!important] Important
> Don’t use this property value to restrict drawing. Instead, draw an empty fill in [- renderInContext:forTime:](<../render(in_for_).md>) when there aren’t active captions to render.

## See Also

### Inspecting the scene

- [timeRange](timerange.md) — The time range during which the system doesn’t modify the scene.
- [needsPeriodicRefresh](needsperiodicrefresh.md) — A Boolean value that indicates whether the scene requires redrawing while your app progresses through the content.

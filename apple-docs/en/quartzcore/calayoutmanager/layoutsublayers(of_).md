---
title: 'layoutSublayers(of:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayoutmanager/layoutsublayers(of:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayoutmanager/layoutsublayers(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayoutmanager/layoutsublayers%28of%3A%29.json'
content_hash: 'sha256:da021ebfaea51ba9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayoutManager](../calayoutmanager.md)

# layoutSublayers(of:)

<sub>Instance Method</sub>

Override to customize layout of sublayers whenever the layer needs redrawing.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func layoutSublayers(of layer: CALayer)
```

## See Also

### Managing Layout

- [- invalidateLayoutOfLayer:](<invalidatelayout(of_).md>) — Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [- preferredSizeOfLayer:](<preferredsize(of_).md>) — Override to customize layer size.

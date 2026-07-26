---
title: 'preferredSize(of:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayoutmanager/preferredsize(of:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayoutmanager/preferredsize(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayoutmanager/preferredsize%28of%3A%29.json'
content_hash: 'sha256:00ce6d5ab7daa41a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayoutManager](../calayoutmanager.md)

# preferredSize(of:)

<sub>Instance Method</sub>

Override to customize layer size.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func preferredSize(of layer: CALayer) -> CGSize
```

## See Also

### Managing Layout

- [- invalidateLayoutOfLayer:](<invalidatelayout(of_).md>) — Invalidates the layout of a layer so it knows to refresh its content on the next frame.
- [- layoutSublayersOfLayer:](<layoutsublayers(of_).md>) — Override to customize layout of sublayers whenever the layer needs redrawing.

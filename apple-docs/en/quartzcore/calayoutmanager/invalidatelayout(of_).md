---
title: 'invalidateLayout(of:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [Mac Catalyst 13.1+, macOS 10.5+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayoutmanager/invalidatelayout(of:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayoutmanager/invalidatelayout(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayoutmanager/invalidatelayout%28of%3A%29.json'
content_hash: 'sha256:136d800132e2e4ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayoutManager](../calayoutmanager.md)

# invalidateLayout(of:)

<sub>Instance Method</sub>

Invalidates the layout of a layer so it knows to refresh its content on the next frame.

<sub>Mac Catalyst, macOS</sub>

```swift
optional func invalidateLayout(of layer: CALayer)
```

## See Also

### Managing Layout

- [- layoutSublayersOfLayer:](<layoutsublayers(of_).md>) — Override to customize layout of sublayers whenever the layer needs redrawing.
- [- preferredSizeOfLayer:](<preferredsize(of_).md>) — Override to customize layer size.

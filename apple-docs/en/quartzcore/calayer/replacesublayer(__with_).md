---
title: 'replaceSublayer(_:with:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/replacesublayer(_:with:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/replacesublayer(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/replacesublayer%28_%3Awith%3A%29.json'
content_hash: 'sha256:752f0df8e68b8fc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# replaceSublayer(_:with:)

<sub>Instance Method</sub>

Replaces the specified sublayer with a different layer object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func replaceSublayer(_ oldLayer: CALayer, with newLayer: CALayer)
```

## Parameters

- `oldLayer` — The layer to be replaced.

- `newLayer` — The layer with which to replace `oldLayer`.

## Discussion

If `oldLayer` is not in the receiver’s [sublayers](sublayers.md) array, the behavior of this method is undefined.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [superlayer](superlayer.md) — The superlayer of the layer.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.

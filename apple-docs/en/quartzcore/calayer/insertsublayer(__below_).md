---
title: 'insertSublayer(_:below:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/insertsublayer(_:below:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/insertsublayer(_:below:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/insertsublayer%28_%3Abelow%3A%29.json'
content_hash: 'sha256:95554e1232e352ef'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# insertSublayer(_:below:)

<sub>Instance Method</sub>

Inserts the specified sublayer below a different sublayer that already belongs to the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertSublayer(_ layer: CALayer, below sibling: CALayer?)
```

## Parameters

- `layer` — The sublayer to be inserted into the current layer.

- `sibling` — An existing sublayer in the current layer. The layer in `aLayer` is inserted before this layer in the [sublayers](sublayers.md) array, and thus appears behind it visually.

## Discussion

If `sublayer` is not in the receiver’s [sublayers](sublayers.md) array, this method raises an exception.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [superlayer](superlayer.md) — The superlayer of the layer.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

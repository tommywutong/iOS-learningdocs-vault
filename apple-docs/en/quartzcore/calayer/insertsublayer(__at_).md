---
title: 'insertSublayer(_:at:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/insertsublayer(_:at:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/insertsublayer(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/insertsublayer%28_%3Aat%3A%29.json'
content_hash: 'sha256:f6f1e8de3dfa35b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# insertSublayer(_:at:)

<sub>Instance Method</sub>

Inserts the specified layer into the receiver’s list of sublayers at the specified index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertSublayer(_ layer: CALayer, at idx: UInt32)
```

## Parameters

- `layer` — The sublayer to be inserted into the current layer.

- `idx` — The index at which to insert `aLayer`. This value must be a valid 0-based index into the [sublayers](sublayers.md) array.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [superlayer](superlayer.md) — The superlayer of the layer.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

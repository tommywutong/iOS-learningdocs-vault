---
title: 'addSublayer(_:)'
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/quartzcore/calayer/addsublayer(_:)'
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/addsublayer(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/addsublayer%28_%3A%29.json'
content_hash: 'sha256:3c95c24f56a0bc8f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# addSublayer(_:)

<sub>Instance Method</sub>

Appends the layer to the layer’s list of sublayers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addSublayer(_ layer: CALayer)
```

## Parameters

- `layer` — The layer to be added.

## Discussion

If the array in the sublayers property is `nil`, calling this method creates an array for that property and adds the specified layer to it.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [superlayer](superlayer.md) — The superlayer of the layer.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

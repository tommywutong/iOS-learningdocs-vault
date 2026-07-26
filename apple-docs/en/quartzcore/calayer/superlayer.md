---
title: superlayer
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/superlayer
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/superlayer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/superlayer.json'
content_hash: 'sha256:f37b67ef34cb5f02'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# superlayer

<sub>Instance Property</sub>

The superlayer of the layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var superlayer: CALayer? { get }
```

## Discussion

The superlayer manages the layout of its sublayers.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

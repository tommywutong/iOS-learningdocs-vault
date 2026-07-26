---
title: sublayers
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/sublayers
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/sublayers'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/sublayers.json'
content_hash: 'sha256:65115701996a03e7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# sublayers

<sub>Instance Property</sub>

An array containing the layer’s sublayers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var sublayers: [CALayer]? { get set }
```

## Discussion

The sublayers are listed in back to front order. The default value of this property is `nil`.

### Special Considerations

When setting the [sublayers](sublayers.md) property to an array populated with layer objects, each layer in the array must not already have a superlayer—that is, its [superlayer](superlayer.md) property must currently be `nil`.

## See Also

### Managing the layer hierarchy

- [superlayer](superlayer.md) — The superlayer of the layer.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- removeFromSuperlayer](<removefromsuperlayer().md>) — Detaches the layer from its parent layer.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

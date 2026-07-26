---
title: removeFromSuperlayer()
framework: Core Animation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/calayer/removefromsuperlayer()
source_url: 'https://developer.apple.com/documentation/quartzcore/calayer/removefromsuperlayer()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/calayer/removefromsuperlayer%28%29.json'
content_hash: 'sha256:569c5e11d1e1c687'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CALayer](../calayer.md)

# removeFromSuperlayer()

<sub>Instance Method</sub>

Detaches the layer from its parent layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeFromSuperlayer()
```

## Discussion

You can use this method to remove a layer (and all of its sublayers) from a layer hierarchy. This method updates both the superlayer’s list of sublayers and sets this layer’s [superlayer](superlayer.md) property to `nil`.

## See Also

### Managing the layer hierarchy

- [sublayers](sublayers.md) — An array containing the layer’s sublayers.
- [superlayer](superlayer.md) — The superlayer of the layer.
- [- addSublayer:](<addsublayer(__).md>) — Appends the layer to the layer’s list of sublayers.
- [- insertSublayer:atIndex:](<insertsublayer(__at_).md>) — Inserts the specified layer into the receiver’s list of sublayers at the specified index.
- [- insertSublayer:below:](<insertsublayer(__below_).md>) — Inserts the specified sublayer below a different sublayer that already belongs to the receiver.
- [- insertSublayer:above:](<insertsublayer(__above_).md>) — Inserts the specified sublayer above a different sublayer that already belongs to the receiver.
- [- replaceSublayer:with:](<replacesublayer(__with_).md>) — Replaces the specified sublayer with a different layer object.

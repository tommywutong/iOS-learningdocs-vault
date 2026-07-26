---
title: instanceTransform
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/careplicatorlayer/instancetransform
source_url: 'https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancetransform'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/careplicatorlayer/instancetransform.json'
content_hash: 'sha256:aebe79efd1c25739'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAReplicatorLayer](../careplicatorlayer.md)

# instanceTransform

<sub>Instance Property</sub>

The transform matrix applied to the previous instance to produce the current instance. Animatable.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceTransform: CATransform3D { get set }
```

## Discussion

This transform matrix is applied to instance `k-1` to produce instance `k`. The matrix is applied relative to the center of this layer.

Defaults to the identity matrix.

## See Also

### Setting Instance Display Properties

- [instanceCount](instancecount.md) — The number of copies to create, including the source layers.
- [instanceDelay](instancedelay.md) — Specifies the delay, in seconds, between replicated copies. Animatable.

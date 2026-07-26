---
title: instanceCount
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/careplicatorlayer/instancecount
source_url: 'https://developer.apple.com/documentation/quartzcore/careplicatorlayer/instancecount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/careplicatorlayer/instancecount.json'
content_hash: 'sha256:6ba7d3976dfe0657'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAReplicatorLayer](../careplicatorlayer.md)

# instanceCount

<sub>Instance Property</sub>

The number of copies to create, including the source layers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var instanceCount: Int { get set }
```

## Discussion

Default value is `1`, no extra copies are created.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

### Setting Instance Display Properties

- [instanceDelay](instancedelay.md) — Specifies the delay, in seconds, between replicated copies. Animatable.
- [instanceTransform](instancetransform.md) — The transform matrix applied to the previous instance to produce the current instance. Animatable.

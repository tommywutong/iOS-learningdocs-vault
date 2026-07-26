---
title: scrollMode
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/cascrolllayer/scrollmode
source_url: 'https://developer.apple.com/documentation/quartzcore/cascrolllayer/scrollmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/cascrolllayer/scrollmode.json'
content_hash: 'sha256:aa4fbd376d7c58dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAScrollLayer](../cascrolllayer.md)

# scrollMode

<sub>Instance Property</sub>

Defines the axes in which the layer may be scrolled.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var scrollMode: CAScrollLayerScrollMode { get set }
```

## Discussion

The possible values are described in [Scroll Modes](../scroll-modes.md). The default is [kCAScrollBoth](../cascrolllayerscrollmode/both.md).

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

---
title: animations
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/caanimationgroup/animations
source_url: 'https://developer.apple.com/documentation/quartzcore/caanimationgroup/animations'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/caanimationgroup/animations.json'
content_hash: 'sha256:a8078d7c42c10300'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CAAnimationGroup](../caanimationgroup.md)

# animations

<sub>Instance Property</sub>

An array of `CAAnimation` objects to be evaluated in the time space of the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var animations: [CAAnimation]? { get set }
```

## Discussion

The animations run concurrently in the receiver’s time space.

## See Also

### Related Documentation

- [Core Animation Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreAnimation_guide/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004514)

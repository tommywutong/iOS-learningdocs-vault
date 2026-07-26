---
title: type
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransition/type
source_url: 'https://developer.apple.com/documentation/quartzcore/catransition/type'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransition/type.json'
content_hash: 'sha256:4c08a03f2bf2931c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransition](../catransition.md)

# type

<sub>Instance Property</sub>

Specifies the predefined transition type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var type: CATransitionType { get set }
```

## Discussion

The possible values are shown in [Common Transition Types](../common-transition-types.md). This property is ignored if a custom transition is specified in the [filter](filter.md) property. The default is [kCATransitionFade](../catransitiontype/fade.md).

## See Also

### Transition Properties

- [subtype](subtype.md) — Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.

---
title: subtype
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransition/subtype
source_url: 'https://developer.apple.com/documentation/quartzcore/catransition/subtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransition/subtype.json'
content_hash: 'sha256:8b2d67c922c0491f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransition](../catransition.md)

# subtype

<sub>Instance Property</sub>

Specifies an optional subtype that indicates the direction for the predefined motion-based transitions.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var subtype: CATransitionSubtype? { get set }
```

## Discussion

The possible values are shown in  [Common Transition Subtypes](../common-transition-subtypes.md). The default is `nil`.

This property is ignored if a custom transition is specified in the [filter](filter.md) property.

## See Also

### Transition Properties

- [type](type.md) — Specifies the predefined transition type.

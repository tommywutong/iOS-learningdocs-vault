---
title: endProgress
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransition/endprogress
source_url: 'https://developer.apple.com/documentation/quartzcore/catransition/endprogress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransition/endprogress.json'
content_hash: 'sha256:357af8b4cff6faf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransition](../catransition.md)

# endProgress

<sub>Instance Property</sub>

Indicates the end point of the receiver as a fraction of the entire transition.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var endProgress: Float { get set }
```

## Discussion

The value must be greater than or equal to [startProgress](startprogress.md), and not greater than 1.0.  If `endProgress` is less than [startProgress](startprogress.md) the behavior is undefined. The default value is 1.0.

## See Also

### Transition start and end point

- [startProgress](startprogress.md) — Indicates the start point of the receiver as a fraction of the entire transition.

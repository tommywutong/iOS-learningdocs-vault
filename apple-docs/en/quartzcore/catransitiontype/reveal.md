---
title: reveal
framework: Core Animation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/quartzcore/catransitiontype/reveal
source_url: 'https://developer.apple.com/documentation/quartzcore/catransitiontype/reveal'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/quartzcore/catransitiontype/reveal.json'
content_hash: 'sha256:e2120d32c6e485e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Animation](../../quartzcore.md) · [CATransitionType](../catransitiontype.md)

# reveal

<sub>Type Property</sub>

The layer’s content is revealed gradually in the direction specified by the transition subtype.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
static let reveal: CATransitionType
```

## Discussion

The [Common Transition Subtypes](../common-transition-subtypes.md) are used with this transition.

## See Also

### Constants

- [kCATransitionFade](fade.md) — The layer’s content fades as it becomes visible or hidden.
- [kCATransitionMoveIn](movein.md) — The layer’s content slides into place over any existing content.
- [kCATransitionPush](push.md) — The layer’s content pushes any existing content as it slides into place.

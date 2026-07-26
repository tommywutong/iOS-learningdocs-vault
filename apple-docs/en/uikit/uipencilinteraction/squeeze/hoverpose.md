---
title: hoverPose
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.5+, iPadOS 17.5+, Mac Catalyst 17.5+, visionOS 26.2+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipencilinteraction/squeeze/hoverpose
source_url: 'https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze/hoverpose'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipencilinteraction/squeeze/hoverpose.json'
content_hash: 'sha256:7571d73bbb2e62ad'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPencilInteraction](../../uipencilinteraction.md) · [Squeeze](../squeeze.md)

# hoverPose

<sub>Instance Property</sub>

The hover pose of Apple Pencil during a squeeze interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var hoverPose: UIPencilHoverPose? { get }
```

## Discussion

The value of this property is `nil` if Apple Pencil isn’t close enough to the screen to detect a hover, or if the device doesn’t support hover.

## See Also

### Getting information about a squeeze interaction

- [timestamp](timestamp.md) — The timestamp of the squeeze interaction.
- [phase](phase.md) — The phase of a squeeze interaction on Apple Pencil.
- [Phase](../phase.md) — Constants that describe the phases of an interaction on Apple Pencil.
- [UIPencilHoverPose](../../uipencilhoverpose.md) — An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

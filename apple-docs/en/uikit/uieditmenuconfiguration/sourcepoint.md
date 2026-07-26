---
title: sourcePoint
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuconfiguration/sourcepoint
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/sourcepoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuconfiguration/sourcepoint.json'
content_hash: 'sha256:a21f32370f1f3c15'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuConfiguration](../uieditmenuconfiguration.md)

# sourcePoint

<sub>Instance Property</sub>

The source location of the interaction.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourcePoint: CGPoint { get }
```

## Discussion

The system derives the suggested actions list from this point in the interaction’s view. By default, the menu also presents from this location. You can change the presentation source of the menu by implementing the delegate method [- editMenuInteraction:targetRectForConfiguration:](<../uieditmenuinteractiondelegate/editmenuinteraction(__targetrectfor_).md>).

## See Also

### Configuring the menu

- [preferredArrowDirection](preferredarrowdirection.md) — The preferred direction the arrow of the edit menu is pointing.
- [UIEditMenuArrowDirection](../uieditmenuarrowdirection.md) — Constants that describe the direction the arrow of the edit menu is pointing.

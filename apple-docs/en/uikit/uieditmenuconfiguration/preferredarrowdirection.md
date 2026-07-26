---
title: preferredArrowDirection
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uieditmenuconfiguration/preferredarrowdirection
source_url: 'https://developer.apple.com/documentation/uikit/uieditmenuconfiguration/preferredarrowdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uieditmenuconfiguration/preferredarrowdirection.json'
content_hash: 'sha256:1981d0c219238774'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIEditMenuConfiguration](../uieditmenuconfiguration.md)

# preferredArrowDirection

<sub>Instance Property</sub>

The preferred direction the arrow of the edit menu is pointing.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var preferredArrowDirection: UIEditMenuArrowDirection { get set }
```

## Discussion

The default, [UIEditMenuArrowDirectionAutomatic](../uieditmenuarrowdirection/automatic.md), is an arrow pointing up or down at the object of focus, based on its location in the screen.

## See Also

### Configuring the menu

- [UIEditMenuArrowDirection](../uieditmenuarrowdirection.md) — Constants that describe the direction the arrow of the edit menu is pointing.
- [sourcePoint](sourcepoint.md) — The source location of the interaction.

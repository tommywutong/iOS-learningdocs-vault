---
title: textDragInteraction
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdraggable/textdraginteraction
source_url: 'https://developer.apple.com/documentation/uikit/uitextdraggable/textdraginteraction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdraggable/textdraginteraction.json'
content_hash: 'sha256:fa8cca06bcb5598e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDraggable](../uitextdraggable.md)

# textDragInteraction

<sub>Instance Property</sub>

The drag interaction object added by UIKit to the text view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var textDragInteraction: UIDragInteraction? { get }
```

## Discussion

You can set the text drag interaction’s [enabled](../uidraginteraction/isenabled.md) property to [false](../../swift/false.md) if you need to explicitly turn off drag interactions for a UIKit-provided text view.

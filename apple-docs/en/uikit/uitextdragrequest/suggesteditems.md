---
title: suggestedItems
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextdragrequest/suggesteditems
source_url: 'https://developer.apple.com/documentation/uikit/uitextdragrequest/suggesteditems'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextdragrequest/suggesteditems.json'
content_hash: 'sha256:0058f0905cc2048b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextDragRequest](../uitextdragrequest.md)

# suggestedItems

<sub>Instance Property</sub>

An array of drag items that the system provides when the text drag delegate doesn’t provide custom drag items.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var suggestedItems: [UIDragItem] { get }
```

## Discussion

The [suggestedItems](suggesteditems.md) property is always an empty array if the text drag delegate doesn’t implement the [- textDraggableView:itemsForDrag:](<../uitextdragdelegate/textdraggableview(__itemsfordrag_).md>) method.

## See Also

### Getting the drag items

- [existingItems](existingitems.md) — The array of drag items present in a drag session.

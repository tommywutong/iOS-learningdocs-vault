---
title: view
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidragpreview/view
source_url: 'https://developer.apple.com/documentation/uikit/uidragpreview/view'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidragpreview/view.json'
content_hash: 'sha256:768a614cb83dbd28'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDragPreview](../uidragpreview.md)

# view

<sub>Instance Property</sub>

The view associated with the drag item preview.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var view: UIView { get }
```

## Discussion

The drag item preview uses the view to create a visual snapshot that’s displayed while the user drags the item across the screen. Changes you make to the view don’t appear in the preview after the snapshot is taken, and the preview doesn’t make changes or move the view. Any visual changes or movement made by the preview are applied to the snapshot only.

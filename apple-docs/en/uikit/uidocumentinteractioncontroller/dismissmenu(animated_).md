---
title: 'dismissMenu(animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/dismissmenu(animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/dismissmenu(animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/dismissmenu%28animated%3A%29.json'
content_hash: 'sha256:db6330cecc299b36'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# dismissMenu(animated:)

<sub>Instance Method</sub>

Dismisses the currently active menu.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func dismissMenu(animated: Bool)
```

## Parameters

- `animated` — Specify [true](../../swift/true.md) to animate the dismissal of the currently active menu or [false](../../swift/false.md) to dismiss it immediately.

## Discussion

Use this method to dismiss a menu programmatically. The document interaction controller can also dismiss the menu automatically in response to user actions.

## See Also

### Presenting and dismissing menus

- [- presentOptionsMenuFromRect:inView:animated:](<presentoptionsmenu(from_in_animated_).md>) — Displays an options menu and anchors it to the specified location in the view.
- [- presentOptionsMenuFromBarButtonItem:animated:](<presentoptionsmenu(from_animated_).md>) — Displays an options menu and anchors it to the specified bar button item.
- [- presentOpenInMenuFromRect:inView:animated:](<presentopeninmenu(from_in_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified view.
- [- presentOpenInMenuFromBarButtonItem:animated:](<presentopeninmenu(from_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified bar button item.

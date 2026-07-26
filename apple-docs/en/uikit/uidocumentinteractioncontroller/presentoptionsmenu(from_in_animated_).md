---
title: 'presentOptionsMenu(from:in:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentoptionsmenu(from:in:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/presentoptionsmenu%28from%3Ain%3Aanimated%3A%29.json'
content_hash: 'sha256:3fb5d43ed4d92b67'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# presentOptionsMenu(from:in:animated:)

<sub>Instance Method</sub>

Displays an options menu and anchors it to the specified location in the view.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentOptionsMenu(from rect: CGRect, in view: UIView, animated: Bool) -> Bool
```

## Parameters

- `rect` — The location (in the coordinate system of `view`) at which to anchor the menu.

- `view` — The view from which to display the options menu.

- `animated` — Specify [true](../../swift/true.md) to animate the appearance of the menu or [false](../../swift/false.md) to display it immediately.

## Return Value

[true](../../swift/true.md) if the options menu was displayed or [false](../../swift/false.md) if it was not. The options menu may not be displayed in cases where there are no appropriate items to include in the menu.

## Discussion

The contents of the options menu are built dynamically based on three things:

- The type of the document (as specified by the [UTI](uti.md) property)
- The set of installed apps that have registered support for opening documents
- The actions that you have indicated as supported in the document interaction controller delegate’s [- documentInteractionController:canPerformAction:](<../uidocumentinteractioncontrollerdelegate/documentinteractioncontroller(__canperformaction_).md>) method

Options that cannot be performed on the current document are not included in the menu. For example, if the document cannot be opened by any known apps, the menu does not include options for opening it.

This method displays the options menu asynchronously. The menu is dismissed automatically when the user selects one of the available options. You can also dismiss it programmatically using the [- dismissMenuAnimated:](<dismissmenu(animated_).md>) method.

To instead present a menu that contains only a list of apps capable of opening the current document, the [- presentOpenInMenuFromRect:inView:animated:](<presentopeninmenu(from_in_animated_).md>) method instead.

## See Also

### Presenting and dismissing menus

- [- presentOptionsMenuFromBarButtonItem:animated:](<presentoptionsmenu(from_animated_).md>) — Displays an options menu and anchors it to the specified bar button item.
- [- presentOpenInMenuFromRect:inView:animated:](<presentopeninmenu(from_in_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified view.
- [- presentOpenInMenuFromBarButtonItem:animated:](<presentopeninmenu(from_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified bar button item.
- [- dismissMenuAnimated:](<dismissmenu(animated_).md>) — Dismisses the currently active menu.

---
title: 'presentOpenInMenu(from:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+, iPadOS 3.2+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uidocumentinteractioncontroller/presentopeninmenu(from:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentinteractioncontroller/presentopeninmenu(from:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentinteractioncontroller/presentopeninmenu%28from%3Aanimated%3A%29.json'
content_hash: 'sha256:f08c065455178ab7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentInteractionController](../uidocumentinteractioncontroller.md)

# presentOpenInMenu(from:animated:)

<sub>Instance Method</sub>

Displays a menu for opening the document and anchors that menu to the specified bar button item.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func presentOpenInMenu(from item: UIBarButtonItem, animated: Bool) -> Bool
```

## Parameters

- `item` — The bar button item to which to anchor the menu.

- `animated` — Specify [true](../../swift/true.md) to animate the appearance of the menu or [false](../../swift/false.md) to display it immediately.

## Return Value

[true](../../swift/true.md) if this method was able to display the menu or [false](../../swift/false.md) if it was not.

## Discussion

This method is similar to the [- presentOptionsMenuFromBarButtonItem:animated:](<presentoptionsmenu(from_animated_).md>) method, but presents a menu restricted to a list of apps capable of opening the current document. This determination is made based on the document type (as indicated by the [UTI](uti.md) property) and on the document types supported by the installed apps. To support one or more document types, an app must register those types in its `Info.plist` file using the `CFBundleDocumentTypes` key.

If there are no registered apps that support opening the document, the document interaction controller does not display a menu.

This method displays the menu asynchronously. The document interaction controller dismisses the menu automatically when the user selects an appropriate app. You can also dismiss it programmatically using the [- dismissMenuAnimated:](<dismissmenu(animated_).md>) method.

## See Also

### Presenting and dismissing menus

- [- presentOptionsMenuFromRect:inView:animated:](<presentoptionsmenu(from_in_animated_).md>) — Displays an options menu and anchors it to the specified location in the view.
- [- presentOptionsMenuFromBarButtonItem:animated:](<presentoptionsmenu(from_animated_).md>) — Displays an options menu and anchors it to the specified bar button item.
- [- presentOpenInMenuFromRect:inView:animated:](<presentopeninmenu(from_in_animated_).md>) — Displays a menu for opening the document and anchors that menu to the specified view.
- [- dismissMenuAnimated:](<dismissmenu(animated_).md>) — Dismisses the currently active menu.

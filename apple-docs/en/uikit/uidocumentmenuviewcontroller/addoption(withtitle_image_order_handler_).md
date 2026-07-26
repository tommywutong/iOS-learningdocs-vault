---
title: 'addOption(withTitle:image:order:handler:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+（11.0 起废弃）, iPadOS 8.0+（11.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uidocumentmenuviewcontroller/addoption(withtitle:image:order:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uidocumentmenuviewcontroller/addoption(withtitle:image:order:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidocumentmenuviewcontroller/addoption%28withtitle%3Aimage%3Aorder%3Ahandler%3A%29.json'
content_hash: 'sha256:17542a37521275b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md)

# addOption(withTitle:image:order:handler:)

<sub>Instance Method</sub>

Adds a custom menu item to the list of document pickers.

> [!warning] Deprecated
> For more information, see [UIDocumentMenuViewController](../uidocumentmenuviewcontroller.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func addOption(withTitle title: String, image: UIImage?, order: UIDocumentMenuOrder, handler: @escaping () -> Void)
```

## Parameters

- `title` — The custom menu item’s title.

- `image` — The custom menu item’s image.

- `order` — The position of this menu item. See [UIDocumentMenuOrder](../uidocumentmenuorder.md) for possible values.

- `handler` — A block that is called when the user selects this custom menu item.

## See Also

### Configuring a document menu

- [UIDocumentMenuOrder](../uidocumentmenuorder.md) — The insertion point for custom menu items. _(deprecated)_

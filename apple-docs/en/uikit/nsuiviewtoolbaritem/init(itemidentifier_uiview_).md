---
title: 'init(itemIdentifier:uiView:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [Mac Catalyst 16.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/nsuiviewtoolbaritem/init(itemidentifier:uiview:)'
source_url: 'https://developer.apple.com/documentation/uikit/nsuiviewtoolbaritem/init(itemidentifier:uiview:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/nsuiviewtoolbaritem/init%28itemidentifier%3Auiview%3A%29.json'
content_hash: 'sha256:4f8a051536571471'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [NSUIViewToolbarItem](../nsuiviewtoolbaritem.md)

# init(itemIdentifier:uiView:)

<sub>Initializer</sub>

Creates a toolbar item with the identifier and underlying UIKit view you specify.

<sub>Mac Catalyst</sub>

```swift
init(itemIdentifier identifier: NSToolbarItem.Identifier, uiView: UIView)
```

## Parameters

- `identifier` — The identifier for the toolbar item. You use this value to identify the item within your app, so you don’t need to localize it. For example, your toolbar delegate uses this value to identify the specific toolbar item.

- `uiView` — The UIKit view for the toolbar item.

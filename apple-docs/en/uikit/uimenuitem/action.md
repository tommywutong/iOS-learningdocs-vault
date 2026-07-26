---
title: action
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（16.0 起废弃）, iPadOS 3.2+（16.0 起废弃）, Mac Catalyst 13.1+（16.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uimenuitem/action
source_url: 'https://developer.apple.com/documentation/uikit/uimenuitem/action'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uimenuitem/action.json'
content_hash: 'sha256:e700e35e183ae46c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIMenuItem](../uimenuitem.md)

# action

<sub>Instance Property</sub>

A selector identifying the method of the responder object to invoke for handling of the menu command.

> [!warning] Deprecated
> For more information, see [UIMenuItem](../uimenuitem.md).

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var action: Selector { get set }
```

## Discussion

The action selector cannot be `NULL`.

## See Also

### Accessing menu-item attributes

- [title](title.md) — The title of the menu item. _(deprecated)_

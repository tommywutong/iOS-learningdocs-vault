---
title: handler
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipreviewaction/handler
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewaction/handler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewaction/handler.json'
content_hash: 'sha256:445e11b3e531b6dd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewAction](../uipreviewaction.md)

# handler

<sub>Instance Property</sub>

The block called when the peek quick action is selected by the user.

> [!warning] Deprecated
> For more information, see [UIPreviewAction](../uipreviewaction.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var handler: (any UIPreviewActionItem, UIViewController) -> Void { get }
```

## Discussion

The handler is set when the peek quick action is instantiated; it is immutable.

## See Also

### Creating a peek quick action

- [+ actionWithTitle:style:handler:](<init(title_style_handler_).md>) — Creates a peek quick action using a specified title, style, and handler. _(deprecated)_
- [Style](style.md) — The style for a peek quick action. _(deprecated)_

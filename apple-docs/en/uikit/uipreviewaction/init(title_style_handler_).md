---
title: 'init(title:style:handler:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipreviewaction/init(title:style:handler:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewaction/init(title:style:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewaction/init%28title%3Astyle%3Ahandler%3A%29.json'
content_hash: 'sha256:09ab69fa38c616b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewAction](../uipreviewaction.md)

# init(title:style:handler:)

<sub>Initializer</sub>

Creates a peek quick action using a specified title, style, and handler.

> [!warning] Deprecated
> For more information, see [UIPreviewAction](../uipreviewaction.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(title: String, style: UIPreviewAction.Style, handler: @escaping (UIPreviewAction, UIViewController) -> Void)
```

## Parameters

- `title` — The quick action’s title.

- `style` — The quick action’s style. For a complete list of styles, see the `UIPreviewActionStyle` enumeration in _UIPreviewActionItem Protocol Reference_.

- `handler` — A block that is called when the user selects the peek quick action. The block takes the following parameters: - **action** — The peek quick action selected by the user. - **previewViewController** — The view controller displayed as the peek.

## Return Value

A newly-created peek quick action.

## See Also

### Creating a peek quick action

- [handler](handler.md) — The block called when the peek quick action is selected by the user. _(deprecated)_
- [Style](style.md) — The style for a peek quick action. _(deprecated)_

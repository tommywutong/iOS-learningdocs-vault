---
title: 'init(title:style:actions:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 9.0+（13.0 起废弃）, iPadOS 9.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 9.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipreviewactiongroup/init(title:style:actions:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipreviewactiongroup/init(title:style:actions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipreviewactiongroup/init%28title%3Astyle%3Aactions%3A%29.json'
content_hash: 'sha256:4a4bef095a758228'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPreviewActionGroup](../uipreviewactiongroup.md)

# init(title:style:actions:)

<sub>Initializer</sub>

Creates a peek quick action group using a specified title, style, and array of peek quick actions.

> [!warning] Deprecated
> For more information, see [UIPreviewActionGroup](../uipreviewactiongroup.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
convenience init(title: String, style: UIPreviewAction.Style, actions: [UIPreviewAction])
```

## Parameters

- `title` — The peek quick action group’s title

- `style` — The style for the peek quick action group. When the system presents the group’s submenu, each child quick action is displayed using its own style. The available styles are described in the UIPreviewActionStyle enumeration in [UIPreviewActionItem](../uipreviewactionitem.md).

- `actions` — An array of [UIPreviewAction](../uipreviewaction.md) objects, displayed as the child quick actions for the peek quick action group.

## Return Value

A newly initialized peek quick action group with your specified title, style, and submenu of peek quick actions.

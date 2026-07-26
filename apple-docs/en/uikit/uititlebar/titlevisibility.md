---
title: titleVisibility
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+]
languages: [swift, swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uititlebar/titlevisibility
source_url: 'https://developer.apple.com/documentation/uikit/uititlebar/titlevisibility'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uititlebar/titlevisibility.json'
content_hash: 'sha256:40486e50ee7981e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITitlebar](../uititlebar.md)

# titleVisibility

<sub>Instance Property</sub>

A value that indicates the visibility of the title.

<sub>Mac Catalyst</sub>

```swift
var titleVisibility: UITitlebarTitleVisibility { get set }
```

## Discussion

Setting the title visibility to [UITitlebarTitleVisibilityHidden](../uititlebartitlevisibility/hidden.md) hides only the title displayed in the title bar, not the title bar itself. To remove the title bar from the window, set [titleVisibility](titlevisibility.md) to [UITitlebarTitleVisibilityHidden](../uititlebartitlevisibility/hidden.md) and [toolbar](toolbar.md) to `nil`.

This property defaults to [UITitlebarTitleVisibilityVisible](../uititlebartitlevisibility/visible.md).

## See Also

### Configuring the title bar

- [separatorStyle](separatorstyle.md) — The type of separator that the app displays between the title bar and content of a window.
- [UITitlebarSeparatorStyle](../uititlebarseparatorstyle.md) — Styles that determine the type of separator displayed between the title bar and content of a window.
- [UITitlebarTitleVisibility](../uititlebartitlevisibility.md) — States that determine visibility of the title in the title bar.
- [representedURL](representedurl.md) — A URL of the file or resource represented in the window.

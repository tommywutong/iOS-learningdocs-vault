---
title: 'show(from:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/show(from:)-9i3tw'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:)-9i3tw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/show%28from%3A%29-9i3tw.json'
content_hash: 'sha256:999ad0b7db7d4fda'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# show(from:)

<sub>Instance Method</sub>

Displays an action sheet that originates from the specified tab bar.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func show(from view: UITabBar)
```

## Parameters

- `view` — The tab bar from which the action sheet originates.

## Discussion

The appearance of the action sheet is animated.

On iPad, this method centers the action sheet in the middle of the screen. Generally, if you want to present an action sheet relative to a tab bar in an iPad application, you should use the [- showFromRect:inView:animated:](<show(from_in_animated_).md>) method instead.

## See Also

### Presenting the action sheet

- [- showFromToolbar:](<show(from_)-1p4ap.md>) — Displays an action sheet that originates from the specified toolbar. _(deprecated)_
- [- showInView:](<show(in_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_
- [- showFromBarButtonItem:animated:](<show(from_animated_).md>) — Displays an action sheet that originates from the specified bar button item. _(deprecated)_
- [- showFromRect:inView:animated:](<show(from_in_animated_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_

---
title: 'show(in:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（8.3 起废弃）, iPadOS 2.0+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/show(in:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/show(in:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/show%28in%3A%29.json'
content_hash: 'sha256:6cdec13ab6149366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# show(in:)

<sub>Instance Method</sub>

Displays an action sheet that originates from the specified view.

> [!warning] Deprecated
> For more information, see [UIActionSheet](../uiactionsheet.md).

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func show(in view: UIView)
```

## Parameters

- `view` — The view from which the action sheet originates.

## Discussion

The appearance of the action sheet is animated.

On iPad, this method centers the action sheet in the middle of the screen. Generally, if you want to present an action sheet in an iPad application, you should use the [- showFromRect:inView:animated:](<show(from_in_animated_).md>) method to display the action sheet instead.

## See Also

### Presenting the action sheet

- [- showFromTabBar:](<show(from_)-9i3tw.md>) — Displays an action sheet that originates from the specified tab bar. _(deprecated)_
- [- showFromToolbar:](<show(from_)-1p4ap.md>) — Displays an action sheet that originates from the specified toolbar. _(deprecated)_
- [- showFromBarButtonItem:animated:](<show(from_animated_).md>) — Displays an action sheet that originates from the specified bar button item. _(deprecated)_
- [- showFromRect:inView:animated:](<show(from_in_animated_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_

---
title: 'show(from:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（8.3 起废弃）, iPadOS 3.2+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/show(from:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/show%28from%3Aanimated%3A%29.json'
content_hash: 'sha256:cece2d3e11135323'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# show(from:animated:)

<sub>Instance Method</sub>

Displays an action sheet that originates from the specified bar button item.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func show(from item: UIBarButtonItem, animated: Bool)
```

## Parameters

- `item` — The bar button item from which the action sheet originates.

- `animated` — Specify [true](../../swift/true.md) to animate the presentation of the action sheet or [false](../../swift/false.md) to present it immediately without any animation effects.

## Discussion

On iPad, this method presents the action sheet in a popover and adds the toolbar that owns the button to the popover’s list of passthrough views. Thus, taps in the toolbar result in the action methods of the corresponding toolbar items being called. If you want the popover to be dismissed when a different toolbar item is tapped, you must implement that behavior in your action handler methods.

## See Also

### Presenting the action sheet

- [- showFromTabBar:](<show(from_)-9i3tw.md>) — Displays an action sheet that originates from the specified tab bar. _(deprecated)_
- [- showFromToolbar:](<show(from_)-1p4ap.md>) — Displays an action sheet that originates from the specified toolbar. _(deprecated)_
- [- showInView:](<show(in_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_
- [- showFromRect:inView:animated:](<show(from_in_animated_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_

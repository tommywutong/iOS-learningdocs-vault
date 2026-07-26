---
title: 'show(from:in:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（8.3 起废弃）, iPadOS 3.2+（8.3 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uiactionsheet/show(from:in:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uiactionsheet/show(from:in:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uiactionsheet/show%28from%3Ain%3Aanimated%3A%29.json'
content_hash: 'sha256:79cd34d1ac04eec8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIActionSheet](../uiactionsheet.md)

# show(from:in:animated:)

<sub>Instance Method</sub>

Displays an action sheet that originates from the specified view.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func show(from rect: CGRect, in view: UIView, animated: Bool)
```

## Parameters

- `rect` — The portion of `view` from which to originate the action sheet.

- `view` — The view from which to originate the action sheet.

- `animated` — Specify [true](../../swift/true.md) to animate the presentation of the action sheet or [false](../../swift/false.md) to present it immediately without any animation effects.

## Discussion

On iPad, this method displays the action sheet in a popover whose arrow points to the specified rectangle of the view. The popover does not overlap the specified rectangle.

## See Also

### Presenting the action sheet

- [- showFromTabBar:](<show(from_)-9i3tw.md>) — Displays an action sheet that originates from the specified tab bar. _(deprecated)_
- [- showFromToolbar:](<show(from_)-1p4ap.md>) — Displays an action sheet that originates from the specified toolbar. _(deprecated)_
- [- showInView:](<show(in_).md>) — Displays an action sheet that originates from the specified view. _(deprecated)_
- [- showFromBarButtonItem:animated:](<show(from_animated_).md>) — Displays an action sheet that originates from the specified bar button item. _(deprecated)_

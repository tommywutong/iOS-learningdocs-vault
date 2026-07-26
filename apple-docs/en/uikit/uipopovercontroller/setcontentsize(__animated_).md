---
title: 'setContentSize(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/setcontentsize(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/setcontentsize(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/setcontentsize%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:e9ff82bfeb2c1334'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# setContentSize(_:animated:)

<sub>Instance Method</sub>

Changes the size of the popover’s content view.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setContentSize(_ size: CGSize, animated: Bool)
```

## Parameters

- `size` — The new size to apply to the content view.

- `animated` — Specify [true](../../swift/true.md) if you want the change in size to be animated or [false](../../swift/false.md) if you want the change to appear immediately.

## Discussion

When changing the size of the popover’s content, the width value you specify must be at least 320 points and no more than 600 points. There are no restrictions on the height value. However, both the width and height values you specify may be adjusted to ensure the popup fits on screen and is not covered by the keyboard.

## See Also

### Configuring the popover content

- [contentViewController](contentviewcontroller.md) — The view controller responsible for the content portion of the popover. _(deprecated)_
- [- setContentViewController:animated:](<setcontentview(__animated_).md>) — Sets the view controller responsible for the content portion of the popover. _(deprecated)_
- [popoverContentSize](contentsize.md) — The size of the popover’s content view. _(deprecated)_
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible. _(deprecated)_

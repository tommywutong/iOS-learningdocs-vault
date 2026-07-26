---
title: 'setContentView(_:animated:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/uikit/uipopovercontroller/setcontentview(_:animated:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/setcontentview(_:animated:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/setcontentview%28_%3Aanimated%3A%29.json'
content_hash: 'sha256:b3cc1a432b093308'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# setContentView(_:animated:)

<sub>Instance Method</sub>

Sets the view controller responsible for the content portion of the popover.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setContentView(_ viewController: UIViewController, animated: Bool)
```

## Parameters

- `viewController` — The new view controller whose content should be displayed by the popover.

- `animated` — Specify [true](../../swift/true.md) if the change of view controllers should be animated or [false](../../swift/false.md) if the change should occur immediately.

## See Also

### Configuring the popover content

- [contentViewController](contentviewcontroller.md) — The view controller responsible for the content portion of the popover. _(deprecated)_
- [popoverContentSize](contentsize.md) — The size of the popover’s content view. _(deprecated)_
- [- setPopoverContentSize:animated:](<setcontentsize(__animated_).md>) — Changes the size of the popover’s content view. _(deprecated)_
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible. _(deprecated)_

---
title: contentSize
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/contentsize
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/contentsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/contentsize.json'
content_hash: 'sha256:49f73c332fc2361c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# contentSize

<sub>Instance Property</sub>

The size of the popover’s content view.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var contentSize: CGSize { get set }
```

## Discussion

This property represents the size of the content view that is managed by the view controller in the [contentViewController](contentviewcontroller.md) property. The initial value of this property is set to value in the view controller’s [contentSizeForViewInPopover](../uiviewcontroller/contentsizeforviewinpopover.md) property. Changing the value of this property overrides the default value of the current view controller. The overridden value persists until you assign a new content view controller to the receiver. Thus, if you want to keep your overridden value, you must reassign it after changing the content view controller.

When changing the value of this property, the width value you specify must be at least 320 points and no more than 600 points. There are no restrictions on the height value. However, both the width and height values you specify may be adjusted to ensure the popup fits on screen and is not covered by the keyboard. If you change the value of this property while the popover is visible, the size change is animated.

## See Also

### Configuring the popover content

- [contentViewController](contentviewcontroller.md) — The view controller responsible for the content portion of the popover. _(deprecated)_
- [- setContentViewController:animated:](<setcontentview(__animated_).md>) — Sets the view controller responsible for the content portion of the popover. _(deprecated)_
- [- setPopoverContentSize:animated:](<setcontentsize(__animated_).md>) — Changes the size of the popover’s content view. _(deprecated)_
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible. _(deprecated)_

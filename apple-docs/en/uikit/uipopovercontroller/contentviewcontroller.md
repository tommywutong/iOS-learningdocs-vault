---
title: contentViewController
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/contentviewcontroller
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/contentviewcontroller'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/contentviewcontroller.json'
content_hash: 'sha256:bbe7a5b7f8642462'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# contentViewController

<sub>Instance Property</sub>

The view controller responsible for the content portion of the popover.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var contentViewController: UIViewController { get set }
```

## Discussion

This property is initially set to the view controller passed to the [- initWithContentViewController:](<init(contentviewcontroller_).md>) method. You can change the value of this property later to reflect a new set of content. Changing the value of this property swaps the new view controller in for the old one immediately and does not trigger an animation. If you want to animate the change, use the [- setContentViewController:animated:](<setcontentview(__animated_).md>) method instead.

## See Also

### Configuring the popover content

- [- setContentViewController:animated:](<setcontentview(__animated_).md>) — Sets the view controller responsible for the content portion of the popover. _(deprecated)_
- [popoverContentSize](contentsize.md) — The size of the popover’s content view. _(deprecated)_
- [- setPopoverContentSize:animated:](<setcontentsize(__animated_).md>) — Changes the size of the popover’s content view. _(deprecated)_
- [passthroughViews](passthroughviews.md) — An array of views that the user can interact with while the popover is visible. _(deprecated)_

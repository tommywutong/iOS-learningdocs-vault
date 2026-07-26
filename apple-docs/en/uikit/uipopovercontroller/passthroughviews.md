---
title: passthroughViews
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 3.2+（9.0 起废弃）, iPadOS 3.2+（9.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS（9.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipopovercontroller/passthroughviews
source_url: 'https://developer.apple.com/documentation/uikit/uipopovercontroller/passthroughviews'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopovercontroller/passthroughviews.json'
content_hash: 'sha256:935ef001e8f223b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPopoverController](../uipopovercontroller.md)

# passthroughViews

<sub>Instance Property</sub>

An array of views that the user can interact with while the popover is visible.

> [!warning] Deprecated
> For more information, see [UIPopoverController](../uipopovercontroller.md).

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var passthroughViews: [UIView]? { get set }
```

## Discussion

When a popover is active, interactions with other views are normally disabled until the popover is dismissed. Assigning an array of views to this property allows taps outside of the popover to be handled by the corresponding views.

## See Also

### Configuring the popover content

- [contentViewController](contentviewcontroller.md) — The view controller responsible for the content portion of the popover. _(deprecated)_
- [- setContentViewController:animated:](<setcontentview(__animated_).md>) — Sets the view controller responsible for the content portion of the popover. _(deprecated)_
- [popoverContentSize](contentsize.md) — The size of the popover’s content view. _(deprecated)_
- [- setPopoverContentSize:animated:](<setcontentsize(__animated_).md>) — Changes the size of the popover’s content view. _(deprecated)_

---
title: UIPopoverBackgroundViewMethods
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipopoverbackgroundviewmethods
source_url: 'https://developer.apple.com/documentation/uikit/uipopoverbackgroundviewmethods'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipopoverbackgroundviewmethods.json'
content_hash: 'sha256:8d9e4e514b27e0ec'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPopoverBackgroundViewMethods

<sub>Protocol</sub>

A set of methods that popover background view subclasses must implement.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
protocol UIPopoverBackgroundViewMethods
```

## Overview

The methods in this protocol are called only once when the popover is presented. All methods of this protocol are required.

## Relationships

- **Conforming Types**: [UIPopoverBackgroundView](uipopoverbackgroundview.md)

## Topics

### Returning the content view insets

- [+ contentViewInsets](<uipopoverbackgroundviewmethods/contentviewinsets().md>) — The insets for the content portion of the popover.

### Accessing the arrow metrics

- [+ arrowBase](<uipopoverbackgroundviewmethods/arrowbase().md>) — The width of the arrow triangle at its base.
- [+ arrowHeight](<uipopoverbackgroundviewmethods/arrowheight().md>) — The height of the arrow (measured in points) from its base to its tip.

## See Also

### Popovers

- [Displaying transient content in a popover](displaying-transient-content-in-a-popover.md) — Show a temporary interface on top of your app’s content on iPad.
- [UIPopoverPresentationController](uipopoverpresentationcontroller.md) — An object that manages the display of content in a popover.
- [UIPopoverBackgroundView](uipopoverbackgroundview.md) — The background appearance for a popover.

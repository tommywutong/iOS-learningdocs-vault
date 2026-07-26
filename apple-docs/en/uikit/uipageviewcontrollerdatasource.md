---
title: UIPageViewControllerDataSource
framework: UIKit
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontrollerdatasource
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdatasource.json'
content_hash: 'sha256:ec2a68983e56a475'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [UIKit](../uikit.md)

# UIPageViewControllerDataSource

<sub>Protocol</sub>

The [UIPageViewControllerDataSource](uipageviewcontrollerdatasource.md) protocol is adopted by an object that provides view controllers to the page view controller on an as-needed basis, in response to navigation gestures.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
@MainActor protocol UIPageViewControllerDataSource : NSObjectProtocol
```

## Overview

The data source implementation is free to handle this responsibility in any way that is appropriate for your application. In many cases, it should look at the view controller passed to it, determine what content to display, and create the view controllers as they are needed. You may find it helpful to include information such as the page number in the view controller, to simplify the task of determining what content to display.

If both of the methods in Supporting a Page Indicator are implemented and the page view controller’s transition style is [UIPageViewControllerTransitionStyleScroll](uipageviewcontroller/transitionstyle-swift.enum/scroll.md), a page indicator is visible. Both of these methods are called after the [- setViewControllers:direction:animated:completion:](<uipageviewcontroller/setviewcontrollers(__direction_animated_completion_).md>) method is called. After gesture-driven navigation, these methods are not called. The index is updated automatically and the number of view controllers is expected to remain constant.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Providing View Controllers

- [- pageViewController:viewControllerBeforeViewController:](<uipageviewcontrollerdatasource/pageviewcontroller(__viewcontrollerbefore_).md>) — Returns the view controller before the given view controller.
- [- pageViewController:viewControllerAfterViewController:](<uipageviewcontrollerdatasource/pageviewcontroller(__viewcontrollerafter_).md>) — Returns the view controller after the given view controller.

### Supporting a Page Indicator

- [- presentationCountForPageViewController:](<uipageviewcontrollerdatasource/presentationcount(for_).md>) — Returns the number of items to be reflected in the page indicator.
- [- presentationIndexForPageViewController:](<uipageviewcontrollerdatasource/presentationindex(for_).md>) — Returns the index of the selected item to be reflected in the page indicator.

## See Also

### Providing the Page Content

- [dataSource](uipageviewcontroller/datasource.md) — The object that provides view controllers.

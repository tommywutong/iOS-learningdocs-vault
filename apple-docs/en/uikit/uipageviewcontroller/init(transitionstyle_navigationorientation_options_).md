---
title: 'init(transitionStyle:navigationOrientation:options:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontroller/init(transitionstyle:navigationorientation:options:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/init(transitionstyle:navigationorientation:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/init%28transitionstyle%3Anavigationorientation%3Aoptions%3A%29.json'
content_hash: 'sha256:7412607fe83e903b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# init(transitionStyle:navigationOrientation:options:)

<sub>Initializer</sub>

Initializes a newly created page view controller.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
init(transitionStyle style: UIPageViewController.TransitionStyle, navigationOrientation: UIPageViewController.NavigationOrientation, options: [UIPageViewController.OptionsKey : Any]? = nil)
```

## Parameters

- `style` — The style for transitions between pages.

- `navigationOrientation` — The orientation of the page-by-page navigation.

- `options` — A dictionary of options. For keys, see [OptionsKey](optionskey.md).

## Return Value

The initialized page view controller.

## Discussion

After initialization, use the [- setViewControllers:direction:animated:completion:](<setviewcontrollers(__direction_animated_completion_).md>) method to set the initial view controllers.

## See Also

### Creating a page view controller

- [- initWithCoder:](<init(coder_).md>) — Creates a page view controller from data in an unarchiver.
- [OptionsKey](optionskey.md) — Keys for creating the page view controller.

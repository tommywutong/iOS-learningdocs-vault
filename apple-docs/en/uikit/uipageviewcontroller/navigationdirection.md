---
title: UIPageViewController.NavigationDirection
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/navigationdirection
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/navigationdirection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/navigationdirection.json'
content_hash: 'sha256:3b9a94cc4673fba3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# UIPageViewController.NavigationDirection

<sub>Enumeration</sub>

Directions for page-turn transitions.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum NavigationDirection
```

## Overview

For horizontal navigation, pages turn from the right side of the screen to the left as you navigate forward.

For vertical navigation, pages turn from the bottom of the screen to the top as you navigate forward.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPageViewControllerNavigationDirectionForward](navigationdirection/forward.md) — Navigation to the next page.
- [UIPageViewControllerNavigationDirectionReverse](navigationdirection/reverse.md) — Navigation to the previous page.

### Initializers

- [init(rawValue:)](<navigationdirection/init(rawvalue_).md>)

## See Also

### Providing Content

- [- setViewControllers:direction:animated:completion:](<setviewcontrollers(__direction_animated_completion_).md>) — Sets the view controllers to be displayed.
- [viewControllers](viewcontrollers.md) — The view controllers displayed by the page view controller.
- [gestureRecognizers](gesturerecognizers.md) — An array of [UIGestureRecognizer](../uigesturerecognizer.md) objects that are configured to handle user interaction.

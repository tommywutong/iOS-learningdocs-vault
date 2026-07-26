---
title: UIPageViewController.SpineLocation
framework: UIKit
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/spinelocation-swift.enum
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/spinelocation-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/spinelocation-swift.enum.json'
content_hash: 'sha256:5c7b96fab92f2950'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# UIPageViewController.SpineLocation

<sub>Enumeration</sub>

Locations for the spine.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
enum SpineLocation
```

## Overview

To set the spine location, wrap one of these constants in an [NSNumber](../../foundation/nsnumber.md) object and set it as the value for the [UIPageViewControllerOptionSpineLocationKey](optionskey/spinelocation.md) key in the options dictionary passed to the [- initWithTransitionStyle:navigationOrientation:options:](<init(transitionstyle_navigationorientation_options_).md>) method.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Constants

- [UIPageViewControllerSpineLocationNone](spinelocation-swift.enum/none.md) — No spine.
- [UIPageViewControllerSpineLocationMin](spinelocation-swift.enum/min.md) — Spine at the left or top edge of the screen.
- [UIPageViewControllerSpineLocationMid](spinelocation-swift.enum/mid.md) — Spine in the middle or the screen.
- [UIPageViewControllerSpineLocationMax](spinelocation-swift.enum/max.md) — Spine at the right or bottom edge of the screen.

### Initializers

- [init(rawValue:)](<spinelocation-swift.enum/init(rawvalue_).md>)

## See Also

### Display Options

- [navigationOrientation](navigationorientation-swift.property.md) — The direction along which navigation occurs.
- [NavigationOrientation](navigationorientation-swift.enum.md) — Orientations for page-turn transitions.
- [spineLocation](spinelocation-swift.property.md) — The location of the spine.
- [transitionStyle](transitionstyle-swift.property.md) — The style used to transition between view controllers.
- [TransitionStyle](transitionstyle-swift.enum.md) — Styles for the page-turn transition.
- [doubleSided](isdoublesided.md) — A Boolean value that indicates whether content appears on the back of pages.

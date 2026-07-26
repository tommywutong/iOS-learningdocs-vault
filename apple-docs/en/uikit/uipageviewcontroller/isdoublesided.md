---
title: isDoubleSided
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/isdoublesided
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/isdoublesided'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/isdoublesided.json'
content_hash: 'sha256:c64723b7898d9049'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# isDoubleSided

<sub>Instance Property</sub>

A Boolean value that indicates whether content appears on the back of pages.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var isDoubleSided: Bool { get set }
```

## Discussion

The default value for this property is [false](../../swift/false.md).

If the back of pages has no content (the value is [false](../../swift/false.md)), then the content on the front of the page will partially show through to the back when turning pages.

If the spine is located in the middle, the value must be [true](../../swift/true.md). Setting it to [false](../../swift/false.md) with the spine located in the middle raises an exception.

## See Also

### Display Options

- [navigationOrientation](navigationorientation-swift.property.md) — The direction along which navigation occurs.
- [NavigationOrientation](navigationorientation-swift.enum.md) — Orientations for page-turn transitions.
- [spineLocation](spinelocation-swift.property.md) — The location of the spine.
- [SpineLocation](spinelocation-swift.enum.md) — Locations for the spine.
- [transitionStyle](transitionstyle-swift.property.md) — The style used to transition between view controllers.
- [TransitionStyle](transitionstyle-swift.enum.md) — Styles for the page-turn transition.

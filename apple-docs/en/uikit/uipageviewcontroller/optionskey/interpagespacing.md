---
title: interPageSpacing
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/optionskey/interpagespacing
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/interpagespacing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/optionskey/interpagespacing.json'
content_hash: 'sha256:cd99b3b860bf361f'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPageViewController](../../uipageviewcontroller.md) · [OptionsKey](../optionskey.md)

# interPageSpacing

<sub>Type Property</sub>

Space between pages, in points.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let interPageSpacing: UIPageViewController.OptionsKey
```

## Discussion

The value should be a [CGFloat](../../../corefoundation/cgfloat-swift.struct.md) wrapped in an instance of [NSNumber](../../../foundation/nsnumber.md). The default value is zero. An inter-page spacing is only valid if the transition style is [UIPageViewControllerTransitionStyleScroll](../transitionstyle-swift.enum/scroll.md).

## See Also

### Page options

- [UIPageViewControllerOptionSpineLocationKey](spinelocation.md) — Location of the spine.

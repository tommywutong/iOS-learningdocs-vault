---
title: spineLocation
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS, iPadOS, Mac Catalyst, tvOS, visionOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/optionskey/spinelocation
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/optionskey/spinelocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/optionskey/spinelocation.json'
content_hash: 'sha256:e427667da56eebfd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [UIKit](../../../uikit.md) · [UIPageViewController](../../uipageviewcontroller.md) · [OptionsKey](../optionskey.md)

# spineLocation

<sub>Type Property</sub>

Location of the spine.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let spineLocation: UIPageViewController.OptionsKey
```

## Discussion

For possible values, see [SpineLocation](../spinelocation-swift.enum.md). A spine location is only valid if the transition style is [UIPageViewControllerTransitionStylePageCurl](../transitionstyle-swift.enum/pagecurl.md).

If the transition style is [UIPageViewControllerTransitionStylePageCurl](../transitionstyle-swift.enum/pagecurl.md), the default value for this property is [UIPageViewControllerSpineLocationMin](../spinelocation-swift.enum/min.md); otherwise, the default is [UIPageViewControllerSpineLocationNone](../spinelocation-swift.enum/none.md).

## See Also

### Page options

- [UIPageViewControllerOptionInterPageSpacingKey](interpagespacing.md) — Space between pages, in points.

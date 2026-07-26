---
title: pageIndicatorTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/pageindicatortintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/pageindicatortintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/pageindicatortintcolor.json'
content_hash: 'sha256:2d6000c73d5e501b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# pageIndicatorTintColor

<sub>Instance Property</sub>

The tint color to apply to the page indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var pageIndicatorTintColor: UIColor? { get set }
```

## Discussion

The default color is a translucent white for the page indicator dot. The page indicator dot is used for all of the pages not visible on the screen. Assigning a new value to this property does not automatically change the color in the [currentPageIndicatorTintColor](currentpageindicatortintcolor.md) property because the value for these two properties is not automatically derived from the other. Both properties must be specified independently. Similarly, no alpha is applied to this property for you. It is recommended (but not required) that the color you specify for this parameter contains some transparency–i.e. the alpha value should be less than 1.0.

## See Also

### Coloring the page indicator

- [currentPageIndicatorTintColor](currentpageindicatortintcolor.md) — The tint color to apply to the current page indicator.

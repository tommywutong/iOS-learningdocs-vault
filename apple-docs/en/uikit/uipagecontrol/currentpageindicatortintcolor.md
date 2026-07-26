---
title: currentPageIndicatorTintColor
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/currentpageindicatortintcolor
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/currentpageindicatortintcolor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/currentpageindicatortintcolor.json'
content_hash: 'sha256:139af3ecc228acbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# currentPageIndicatorTintColor

<sub>Instance Property</sub>

The tint color to apply to the current page indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentPageIndicatorTintColor: UIColor? { get set }
```

## Discussion

The default color is an opaque white for the current page indicator dot. The current page indicator dot is used to indicate the currently visible page. Assigning a new value to this property does not automatically change the color in the [pageIndicatorTintColor](pageindicatortintcolor.md) property because the value for these two properties is not automatically derived from the other. Both properties must be specified independently.

## See Also

### Coloring the page indicator

- [pageIndicatorTintColor](pageindicatortintcolor.md) — The tint color to apply to the page indicator.

---
title: preferredCurrentPageIndicatorImage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/preferredcurrentpageindicatorimage
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/preferredcurrentpageindicatorimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/preferredcurrentpageindicatorimage.json'
content_hash: 'sha256:e8a87731ff94d0e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# preferredCurrentPageIndicatorImage

<sub>Instance Property</sub>

The preferred image for the current page indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var preferredCurrentPageIndicatorImage: UIImage? { get set }
```

## Discussion

When `nil`, the page control uses [preferredIndicatorImage](preferredindicatorimage.md) as its current page indicator.

The default value of this property is `nil`.

## See Also

### Managing the indicator images

- [preferredIndicatorImage](preferredindicatorimage.md) — The preferred image for indicators.
- [- indicatorImageForPage:](<indicatorimage(forpage_).md>) — Returns the override image for the indicator of the specified page.
- [- setIndicatorImage:forPage:](<setindicatorimage(__forpage_).md>) — Registers an override image for the indicator of the specified page.
- [- currentPageIndicatorImageForPage:](<currentpageindicatorimage(forpage_).md>) — Returns the override image for the current page indicator of the specified page.
- [- setCurrentPageIndicatorImage:forPage:](<setcurrentpageindicatorimage(__forpage_).md>) — Registers an override image for the current page indicator of the specified page.

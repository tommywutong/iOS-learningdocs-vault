---
title: 'setCurrentPageIndicatorImage(_:forPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrol/setcurrentpageindicatorimage(_:forpage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/setcurrentpageindicatorimage(_:forpage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/setcurrentpageindicatorimage%28_%3Aforpage%3A%29.json'
content_hash: 'sha256:f2fbaf33878bf3d9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# setCurrentPageIndicatorImage(_:forPage:)

<sub>Instance Method</sub>

Registers an override image for the current page indicator of the specified page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setCurrentPageIndicatorImage(_ image: UIImage?, forPage page: Int)
```

## Parameters

- `image` — The image to use instead of the preferred image. Use `nil` to reset the image to [preferredCurrentPageIndicatorImage](preferredcurrentpageindicatorimage.md).

- `page` — The index of the page. A value that’s greater than or equal to `0` and less than [numberOfPages](numberofpages.md).

## See Also

### Managing the indicator images

- [preferredIndicatorImage](preferredindicatorimage.md) — The preferred image for indicators.
- [- indicatorImageForPage:](<indicatorimage(forpage_).md>) — Returns the override image for the indicator of the specified page.
- [- setIndicatorImage:forPage:](<setindicatorimage(__forpage_).md>) — Registers an override image for the indicator of the specified page.
- [preferredCurrentPageIndicatorImage](preferredcurrentpageindicatorimage.md) — The preferred image for the current page indicator.
- [- currentPageIndicatorImageForPage:](<currentpageindicatorimage(forpage_).md>) — Returns the override image for the current page indicator of the specified page.

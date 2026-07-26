---
title: 'setIndicatorImage(_:forPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrol/setindicatorimage(_:forpage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/setindicatorimage(_:forpage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/setindicatorimage%28_%3Aforpage%3A%29.json'
content_hash: 'sha256:c2908bbb043ca970'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# setIndicatorImage(_:forPage:)

<sub>Instance Method</sub>

Registers an override image for the indicator of the specified page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func setIndicatorImage(_ image: UIImage?, forPage page: Int)
```

## Parameters

- `image` — The image to use instead of the preferred image. Use `nil` to reset the image to [preferredIndicatorImage](preferredindicatorimage.md).

- `page` — The index of the page. A value that’s greater than or equal to `0` and less than [numberOfPages](numberofpages.md).

## See Also

### Managing the indicator images

- [preferredIndicatorImage](preferredindicatorimage.md) — The preferred image for indicators.
- [- indicatorImageForPage:](<indicatorimage(forpage_).md>) — Returns the override image for the indicator of the specified page.
- [preferredCurrentPageIndicatorImage](preferredcurrentpageindicatorimage.md) — The preferred image for the current page indicator.
- [- currentPageIndicatorImageForPage:](<currentpageindicatorimage(forpage_).md>) — Returns the override image for the current page indicator of the specified page.
- [- setCurrentPageIndicatorImage:forPage:](<setcurrentpageindicatorimage(__forpage_).md>) — Registers an override image for the current page indicator of the specified page.

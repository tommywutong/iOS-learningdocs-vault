---
title: 'indicatorImage(forPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrol/indicatorimage(forpage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/indicatorimage(forpage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/indicatorimage%28forpage%3A%29.json'
content_hash: 'sha256:8e7c11aece4c2190'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# indicatorImage(forPage:)

<sub>Instance Method</sub>

Returns the override image for the indicator of the specified page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func indicatorImage(forPage page: Int) -> UIImage?
```

## Parameters

- `page` — The index of the page. A value that’s greater than or equal to `0` and less than [numberOfPages](numberofpages.md).

## Return Value

The override image, or `nil` if you haven’t overidden the image for the specified page number.

## See Also

### Managing the indicator images

- [preferredIndicatorImage](preferredindicatorimage.md) — The preferred image for indicators.
- [- setIndicatorImage:forPage:](<setindicatorimage(__forpage_).md>) — Registers an override image for the indicator of the specified page.
- [preferredCurrentPageIndicatorImage](preferredcurrentpageindicatorimage.md) — The preferred image for the current page indicator.
- [- currentPageIndicatorImageForPage:](<currentpageindicatorimage(forpage_).md>) — Returns the override image for the current page indicator of the specified page.
- [- setCurrentPageIndicatorImage:forPage:](<setcurrentpageindicatorimage(__forpage_).md>) — Registers an override image for the current page indicator of the specified page.

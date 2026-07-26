---
title: 'currentPageIndicatorImage(forPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, tvOS 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrol/currentpageindicatorimage(forpage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/currentpageindicatorimage(forpage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/currentpageindicatorimage%28forpage%3A%29.json'
content_hash: 'sha256:9e0beeb980b670fe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# currentPageIndicatorImage(forPage:)

<sub>Instance Method</sub>

Returns the override image for the current page indicator of the specified page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func currentPageIndicatorImage(forPage page: Int) -> UIImage?
```

## Parameters

- `page` — The index of the page. A value that’s greater than or equal to `0` and less than [numberOfPages](numberofpages.md).

## Return Value

The override image, or `nil` if you haven’t overidden the image for the specified page number.

## See Also

### Managing the indicator images

- [preferredIndicatorImage](preferredindicatorimage.md) — The preferred image for indicators.
- [- indicatorImageForPage:](<indicatorimage(forpage_).md>) — Returns the override image for the indicator of the specified page.
- [- setIndicatorImage:forPage:](<setindicatorimage(__forpage_).md>) — Registers an override image for the indicator of the specified page.
- [preferredCurrentPageIndicatorImage](preferredcurrentpageindicatorimage.md) — The preferred image for the current page indicator.
- [- setCurrentPageIndicatorImage:forPage:](<setcurrentpageindicatorimage(__forpage_).md>) — Registers an override image for the current page indicator of the specified page.

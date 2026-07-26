---
title: currentPage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/currentpage
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/currentpage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/currentpage.json'
content_hash: 'sha256:e6935409e4ffad70'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# currentPage

<sub>Instance Property</sub>

The current page, shown by the page control as a white dot.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var currentPage: Int { get set }
```

## Discussion

The property value is an integer specifying the current page shown minus one; thus a value of zero (the default) indicates the first page. A page control shows the current page as a white dot. Values outside the possible range are pinned to either 0 or [numberOfPages](numberofpages.md) minus 1.

## See Also

### Managing pages

- [numberOfPages](numberofpages.md) — The number of pages the receiver shows (as dots).
- [hidesForSinglePage](hidesforsinglepage.md) — A Boolean value that controls whether the page control is hidden when there is only one page.
- [defersCurrentPageDisplay](deferscurrentpagedisplay.md) — A Boolean value that controls when the current page is displayed. _(deprecated)_
- [- updateCurrentPageDisplay](<updatecurrentpagedisplay().md>) — Updates the page indicator to the current page. _(deprecated)_

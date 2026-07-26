---
title: numberOfPages
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/numberofpages
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/numberofpages'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/numberofpages.json'
content_hash: 'sha256:5848165eddce78d8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# numberOfPages

<sub>Instance Property</sub>

The number of pages the receiver shows (as dots).

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var numberOfPages: Int { get set }
```

## Discussion

The value of the property is the number of pages for the page control to show as dots. The default value is 0.

## See Also

### Managing pages

- [currentPage](currentpage.md) — The current page, shown by the page control as a white dot.
- [hidesForSinglePage](hidesforsinglepage.md) — A Boolean value that controls whether the page control is hidden when there is only one page.
- [defersCurrentPageDisplay](deferscurrentpagedisplay.md) — A Boolean value that controls when the current page is displayed. _(deprecated)_
- [- updateCurrentPageDisplay](<updatecurrentpagedisplay().md>) — Updates the page indicator to the current page. _(deprecated)_

---
title: hidesForSinglePage
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipagecontrol/hidesforsinglepage
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/hidesforsinglepage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/hidesforsinglepage.json'
content_hash: 'sha256:a80c6c74096a9d18'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# hidesForSinglePage

<sub>Instance Property</sub>

A Boolean value that controls whether the page control is hidden when there is only one page.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var hidesForSinglePage: Bool { get set }
```

## Discussion

Assign a value of [true](../../swift/true.md) to hide the page control when there is only one page; assign [false](../../swift/false.md) (the default) to show the page control if there is only one page.

## See Also

### Managing pages

- [currentPage](currentpage.md) — The current page, shown by the page control as a white dot.
- [numberOfPages](numberofpages.md) — The number of pages the receiver shows (as dots).
- [defersCurrentPageDisplay](deferscurrentpagedisplay.md) — A Boolean value that controls when the current page is displayed. _(deprecated)_
- [- updateCurrentPageDisplay](<updatecurrentpagedisplay().md>) — Updates the page indicator to the current page. _(deprecated)_

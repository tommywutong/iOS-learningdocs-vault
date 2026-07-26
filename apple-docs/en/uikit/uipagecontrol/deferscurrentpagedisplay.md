---
title: defersCurrentPageDisplay
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+（14.0 起废弃）, iPadOS 2.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, tvOS（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipagecontrol/deferscurrentpagedisplay
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/deferscurrentpagedisplay'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/deferscurrentpagedisplay.json'
content_hash: 'sha256:a8d4c90ab08582e6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# defersCurrentPageDisplay

<sub>Instance Property</sub>

A Boolean value that controls when the current page is displayed.

> [!warning] Deprecated
> The system no longer supports this property.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var defersCurrentPageDisplay: Bool { get set }
```

## Discussion

Set the value of this property to [true](../../swift/true.md) so that, when the user taps the control to go to a new page, the class defers updating the page control until it calls [- updateCurrentPageDisplay](<updatecurrentpagedisplay().md>). Set the value to [false](../../swift/false.md) (the default) to have the page control updated immediately.

## See Also

### Managing pages

- [currentPage](currentpage.md) — The current page, shown by the page control as a white dot.
- [numberOfPages](numberofpages.md) — The number of pages the receiver shows (as dots).
- [hidesForSinglePage](hidesforsinglepage.md) — A Boolean value that controls whether the page control is hidden when there is only one page.
- [- updateCurrentPageDisplay](<updatecurrentpagedisplay().md>) — Updates the page indicator to the current page. _(deprecated)_

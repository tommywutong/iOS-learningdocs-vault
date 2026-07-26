---
title: updateCurrentPageDisplay()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+（14.0 起废弃）, iPadOS 2.0+（14.0 起废弃）, Mac Catalyst 13.1+（14.0 起废弃）, tvOS（14.0 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/uikit/uipagecontrol/updatecurrentpagedisplay()
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrol/updatecurrentpagedisplay()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrol/updatecurrentpagedisplay%28%29.json'
content_hash: 'sha256:173c56ffa4d566e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControl](../uipagecontrol.md)

# updateCurrentPageDisplay()

<sub>Instance Method</sub>

Updates the page indicator to the current page.

> [!warning] Deprecated
> The system no longer supports this method.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
func updateCurrentPageDisplay()
```

## Discussion

This method updates the page indicator so that the current page (the white dot) matches the value returned from [currentPage](currentpage.md). The class ignores this method if the value of [defersCurrentPageDisplay](deferscurrentpagedisplay.md) is [false](../../swift/false.md). Setting the [currentPage](currentpage.md) value directly updates the indicator immediately.

## See Also

### Managing pages

- [currentPage](currentpage.md) — The current page, shown by the page control as a white dot.
- [numberOfPages](numberofpages.md) — The number of pages the receiver shows (as dots).
- [hidesForSinglePage](hidesforsinglepage.md) — A Boolean value that controls whether the page control is hidden when there is only one page.
- [defersCurrentPageDisplay](deferscurrentpagedisplay.md) — A Boolean value that controls when the current page is displayed. _(deprecated)_

---
title: 'presentationIndex(for:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipageviewcontrollerdatasource/presentationindex(for:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontrollerdatasource/presentationindex(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontrollerdatasource/presentationindex%28for%3A%29.json'
content_hash: 'sha256:7cac4bb20a635e59'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewControllerDataSource](../uipageviewcontrollerdatasource.md)

# presentationIndex(for:)

<sub>Instance Method</sub>

Returns the index of the selected item to be reflected in the page indicator.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func presentationIndex(for pageViewController: UIPageViewController) -> Int
```

## Parameters

- `pageViewController` — The page view controller.

## Return Value

The index of the selected item to be reflected in the page indicator.

## See Also

### Supporting a Page Indicator

- [- presentationCountForPageViewController:](<presentationcount(for_).md>) — Returns the number of items to be reflected in the page indicator.

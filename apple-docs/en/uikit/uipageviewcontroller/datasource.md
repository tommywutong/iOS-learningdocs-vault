---
title: dataSource
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uipageviewcontroller/datasource
source_url: 'https://developer.apple.com/documentation/uikit/uipageviewcontroller/datasource'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipageviewcontroller/datasource.json'
content_hash: 'sha256:00f1232668dd5732'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageViewController](../uipageviewcontroller.md)

# dataSource

<sub>Instance Property</sub>

The object that provides view controllers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
weak var dataSource: (any UIPageViewControllerDataSource)? { get set }
```

## Discussion

Methods of the data source are called in response to gesture-based navigation. If the value of this property is `nil`, then gesture-based navigation is disabled.

## See Also

### Providing the Page Content

- [UIPageViewControllerDataSource](../uipageviewcontrollerdatasource.md) — The [UIPageViewControllerDataSource](../uipageviewcontrollerdatasource.md) protocol is adopted by an object that provides view controllers to the page view controller on an as-needed basis, in response to navigation gestures.

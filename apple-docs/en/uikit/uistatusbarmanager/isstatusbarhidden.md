---
title: isStatusBarHidden
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistatusbarmanager/isstatusbarhidden
source_url: 'https://developer.apple.com/documentation/uikit/uistatusbarmanager/isstatusbarhidden'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistatusbarmanager/isstatusbarhidden.json'
content_hash: 'sha256:e75f1985db2781c6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStatusBarManager](../uistatusbarmanager.md)

# isStatusBarHidden

<sub>Instance Property</sub>

A Boolean value that indicates whether the status bar is currently hidden.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var isStatusBarHidden: Bool { get }
```

## Discussion

To customize the status bar’s visibility for each of your view controllers, override your view controller’s [prefersStatusBarHidden](../uiviewcontroller/prefersstatusbarhidden.md) property.

## See Also

### Getting the status bar configuration

- [statusBarStyle](statusbarstyle.md) — The current appearance of the status bar.

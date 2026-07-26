---
title: 'pageControlTimerProgress(_:shouldAdvanceToPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontroltimerprogressdelegate/pagecontroltimerprogress(_:shouldadvancetopage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontroltimerprogressdelegate/pagecontroltimerprogress(_:shouldadvancetopage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontroltimerprogressdelegate/pagecontroltimerprogress%28_%3Ashouldadvancetopage%3A%29.json'
content_hash: 'sha256:70186572a176675e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControlTimerProgressDelegate](../uipagecontroltimerprogressdelegate.md)

# pageControlTimerProgress(_:shouldAdvanceToPage:)

<sub>Instance Method</sub>

Determines if the time interval progress should advance to the next page upon progress completion of the current page’s duration. Default is YES.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pageControlTimerProgress(_ progress: UIPageControlTimerProgress, shouldAdvanceToPage page: Int) -> Bool
```

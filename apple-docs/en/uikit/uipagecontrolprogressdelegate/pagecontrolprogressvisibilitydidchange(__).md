---
title: 'pageControlProgressVisibilityDidChange(_:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange(_:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogressvisibilitydidchange%28_%3A%29.json'
content_hash: 'sha256:8dfd5505fb642d63'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControlProgressDelegate](../uipagecontrolprogressdelegate.md)

# pageControlProgressVisibilityDidChange(_:)

<sub>Instance Method</sub>

Called when the page control progress visibility has changed, which could occur when the page control is being interacted with. The page control progress becomes hidden when the user begins to interact with the page control (when it begins continuous interaction), and is visible again when the user stops interacting with the control. Observe the page control progress visibility to pause or resume the paging content.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pageControlProgressVisibilityDidChange(_ progress: UIPageControlProgress)
```

## Discussion

Example:

- (void)pageControlProgressVisibilityDidChange:(UIPageControlProgress *)progress { BOOL isProgressVisible = progress.isProgressVisible; if (isProgressVisible) { [self _resumeContentFromInteractionChanges]; } else { [self _pauseContentFromInteractionChanges]; } }

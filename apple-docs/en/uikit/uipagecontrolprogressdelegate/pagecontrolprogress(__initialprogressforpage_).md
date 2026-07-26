---
title: 'pageControlProgress(_:initialProgressForPage:)'
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogress(_:initialprogressforpage:)'
source_url: 'https://developer.apple.com/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogress(_:initialprogressforpage:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uipagecontrolprogressdelegate/pagecontrolprogress%28_%3Ainitialprogressforpage%3A%29.json'
content_hash: 'sha256:fe593ef2777022b8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIPageControlProgressDelegate](../uipagecontrolprogressdelegate.md)

# pageControlProgress(_:initialProgressForPage:)

<sub>Instance Method</sub>

Returns the initial progress (between 0…1) for the specified page. By default, `currentProgress` is set to 0 when the page changes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
optional func pageControlProgress(_ progress: UIPageControlProgress, initialProgressForPage page: Int) -> Float
```

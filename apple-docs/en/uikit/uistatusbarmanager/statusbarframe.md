---
title: statusBarFrame
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, swift, swift, swift, occ, occ, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uistatusbarmanager/statusbarframe
source_url: 'https://developer.apple.com/documentation/uikit/uistatusbarmanager/statusbarframe'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uistatusbarmanager/statusbarframe.json'
content_hash: 'sha256:be1f1abfcf84eafd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIStatusBarManager](../uistatusbarmanager.md)

# statusBarFrame

<sub>Instance Property</sub>

The frame rectangle of the status bar.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var statusBarFrame: CGRect { get }
```

## Discussion

The frame rectangle is in the coordinate space of the associated [UIWindowScene](../uiwindowscene.md) object. If the status bar is hidden, the value of this property is [CGRectZero](../../coregraphics/cgrectzero.md).

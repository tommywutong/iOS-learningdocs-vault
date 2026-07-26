---
title: sourceView
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uisheetpresentationcontroller/sourceview
source_url: 'https://developer.apple.com/documentation/uikit/uisheetpresentationcontroller/sourceview'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uisheetpresentationcontroller/sourceview.json'
content_hash: 'sha256:a6ecf6f8abfabd20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UISheetPresentationController](../uisheetpresentationcontroller.md)

# sourceView

<sub>Instance Property</sub>

The view that the sheet centers itself over.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var sourceView: UIView? { get set }
```

## Discussion

The default value is `nil`, which means the system centers edge-attached sheets on the edge they attach to, and centers floating sheets vertically and horizontally in the window.

To customize the sheet’s position, set a view within the view hierarchy of the presenting view controller as the [sourceView](sourceview.md) of the sheet. The sheet attempts to visually center itself over this view. The system only positions the sheet within system-defined margins.

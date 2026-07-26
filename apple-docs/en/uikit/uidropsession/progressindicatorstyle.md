---
title: progressIndicatorStyle
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uidropsession/progressindicatorstyle
source_url: 'https://developer.apple.com/documentation/uikit/uidropsession/progressindicatorstyle'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uidropsession/progressindicatorstyle.json'
content_hash: 'sha256:4af83e7286e5f187'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UIDropSession](../uidropsession.md)

# progressIndicatorStyle

<sub>Instance Property</sub>

The drop-progress indicator style associated with the drop session.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
var progressIndicatorStyle: UIDropSessionProgressIndicatorStyle { get set }
```

## Discussion

This property determines the type of progress indicator displayed when the drop operation takes a significant amount of time. The [UIDropSessionProgressIndicatorStyleDefault](../uidropsessionprogressindicatorstyle/default.md) style indicates that a progress indicator is shown by the system. If you prefer to show your own progress indicator, set this property to [UIDropSessionProgressIndicatorStyleNone](../uidropsessionprogressindicatorstyle/none.md).

---
title: removeAllTrackedConstraints()
framework: UIKit
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitrackinglayoutguide/removealltrackedconstraints()
source_url: 'https://developer.apple.com/documentation/uikit/uitrackinglayoutguide/removealltrackedconstraints()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitrackinglayoutguide/removealltrackedconstraints%28%29.json'
content_hash: 'sha256:34e2bef2e0dc2466'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITrackingLayoutGuide](../uitrackinglayoutguide.md)

# removeAllTrackedConstraints()

<sub>Instance Method</sub>

Stops the layout guide from tracking any constraints.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
func removeAllTrackedConstraints()
```

## Discussion

This method stops only the tracking of constraints. It doesn’t remove constraints from the layout, and it doesn’t activate or deactivate any constraints.

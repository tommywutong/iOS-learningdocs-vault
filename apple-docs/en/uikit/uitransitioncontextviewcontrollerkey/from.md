---
title: from
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewcontrollerkey/from
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey/from'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewcontrollerkey/from.json'
content_hash: 'sha256:f9aad7a349c85da8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITransitionContextViewControllerKey](../uitransitioncontextviewcontrollerkey.md)

# from

<sub>Type Property</sub>

A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let from: UITransitionContextViewControllerKey
```

## Discussion

This view controller is typically the one presenting the “to” view controller or is the one being replaced by the “to” view controller.

## See Also

### Keys

- [UITransitionContextToViewControllerKey](to.md) — A key that identifies the view controller that’s visible at the end of a completed transition.

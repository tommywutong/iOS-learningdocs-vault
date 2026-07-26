---
title: to
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewcontrollerkey/to
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewcontrollerkey/to'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewcontrollerkey/to.json'
content_hash: 'sha256:88f41f3e3c8c943c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITransitionContextViewControllerKey](../uitransitioncontextviewcontrollerkey.md)

# to

<sub>Type Property</sub>

A key that identifies the view controller that’s visible at the end of a completed transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let to: UITransitionContextViewControllerKey
```

## Discussion

This view controller is the one being presented.

## See Also

### Keys

- [UITransitionContextFromViewControllerKey](from.md) — A key that identifies the view controller that’s visible at the beginning of the transition, or at the end of a canceled transition.

---
title: to
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewkey/to
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey/to'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewkey/to.json'
content_hash: 'sha256:d80b68bb262800b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITransitionContextViewKey](../uitransitioncontextviewkey.md)

# to

<sub>Type Property</sub>

A key that identifies the view shown at the end of a completed transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let to: UITransitionContextViewKey
```

## Discussion

This view is typically the presented view controller’s view but may also be an ancestor of that view.

## See Also

### Keys

- [UITransitionContextFromViewKey](from.md) — A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.

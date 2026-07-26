---
title: from
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, tvOS, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitransitioncontextviewkey/from
source_url: 'https://developer.apple.com/documentation/uikit/uitransitioncontextviewkey/from'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitransitioncontextviewkey/from.json'
content_hash: 'sha256:151b9de89bb2bbb1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITransitionContextViewKey](../uitransitioncontextviewkey.md)

# from

<sub>Type Property</sub>

A key that identifies the view shown at the beginning of the transition, or at the end of a canceled transition.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let from: UITransitionContextViewKey
```

## Discussion

This view is typically the presenting view controller’s view.

## See Also

### Keys

- [UITransitionContextToViewKey](to.md) — A key that identifies the view shown at the end of a completed transition.

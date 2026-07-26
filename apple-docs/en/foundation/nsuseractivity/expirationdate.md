---
title: expirationDate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/expirationdate
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/expirationdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/expirationdate.json'
content_hash: 'sha256:0311a22b599aec49'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# expirationDate

<sub>Instance Property</sub>

The date after which the activity is no longer eligible for Handoff or indexing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var expirationDate: Date? { get set }
```

## Discussion

If you don’t set the value of this property, the system automatically expires the activity after a period of time.

## See Also

### Enabling system behaviors

- [eligibleForHandoff](iseligibleforhandoff.md) — A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [eligibleForSearch](iseligibleforsearch.md) — A Boolean value that indicates whether to add the activity to the on-device index.
- [eligibleForPublicIndexing](iseligibleforpublicindexing.md) — A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [eligibleForPrediction](iseligibleforprediction.md) — A Boolean value that determines whether Siri can suggest the activity as a shortcut.

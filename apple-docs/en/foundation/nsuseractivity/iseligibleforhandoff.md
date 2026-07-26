---
title: isEligibleForHandoff
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/iseligibleforhandoff
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforhandoff'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/iseligibleforhandoff.json'
content_hash: 'sha256:6afba3fa70c4ce84'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# isEligibleForHandoff

<sub>Instance Property</sub>

A Boolean value that indicates whether the activity can continue on another device using Handoff.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEligibleForHandoff: Bool { get set }
```

## Discussion

Set the value of this property to `true` for activities you can continue on a person’s other devices; otherwise, set it to `false`. The default value of this property is `true`.

For information about how to support Handoff in your app, see [Implementing Handoff in Your App](../implementing-handoff-in-your-app.md).

## See Also

### Enabling system behaviors

- [eligibleForSearch](iseligibleforsearch.md) — A Boolean value that indicates whether to add the activity to the on-device index.
- [eligibleForPublicIndexing](iseligibleforpublicindexing.md) — A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [eligibleForPrediction](iseligibleforprediction.md) — A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [expirationDate](expirationdate.md) — The date after which the activity is no longer eligible for Handoff or indexing.

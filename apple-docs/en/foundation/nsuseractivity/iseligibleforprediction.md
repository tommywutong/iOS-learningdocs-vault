---
title: isEligibleForPrediction
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, visionOS 1.0+, watchOS 5.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/iseligibleforprediction
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforprediction'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/iseligibleforprediction.json'
content_hash: 'sha256:b4e55d8e66327342'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# isEligibleForPrediction

<sub>Instance Property</sub>

A Boolean value that determines whether Siri can suggest the activity as a shortcut.

<sub>iOS, iPadOS, Mac Catalyst, visionOS, watchOS</sub>

```swift
var isEligibleForPrediction: Bool { get set }
```

## Discussion

If you aren’t yet using App Intents, set the value of this property to `true` if you want the system to suggest the activity as a shortcut. When the activity object is current, or associated with a view or responder in your app’s interface, the system includes the shortcut in places like Spotlight search and the Lock Screen. Set this property to `false` if you’re already donating App Intents to the system or want to prevent the generation of shortcuts for the activity. The default value of this property is `false`.

For information on how to generate shortcuts using SiriKit and activity objects, see [Donating Shortcuts](../../sirikit/donating-shortcuts.md).

## See Also

### Enabling system behaviors

- [eligibleForHandoff](iseligibleforhandoff.md) — A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [eligibleForSearch](iseligibleforsearch.md) — A Boolean value that indicates whether to add the activity to the on-device index.
- [eligibleForPublicIndexing](iseligibleforpublicindexing.md) — A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [expirationDate](expirationdate.md) — The date after which the activity is no longer eligible for Handoff or indexing.

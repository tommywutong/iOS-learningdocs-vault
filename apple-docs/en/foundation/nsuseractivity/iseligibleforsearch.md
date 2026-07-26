---
title: isEligibleForSearch
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/iseligibleforsearch
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforsearch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/iseligibleforsearch.json'
content_hash: 'sha256:9efb61522bd0ceca'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# isEligibleForSearch

<sub>Instance Property</sub>

A Boolean value that indicates whether to add the activity to the on-device index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEligibleForSearch: Bool { get set }
```

## Discussion

If you aren’t yet using App Intents and want to add your user activity objects to the Spotlight indexes, set the value in this property to `true`. When this property is `true` and the user activity object is current, Spotlight indexes the activity so it can appear in search results. Set this property to `false` if you are already indexing [AppEntity](../../appintents/appentity.md) types or don’t want Spotlight to include someone’s activity-related information in search results. The default value of this property is `false`.

Add an activity object to the search index if it contains information a person might reasonably search for later. For example, a restaurant finder app might index activity objects for each restaurant the person views. Subsequent searches for restaurants using Spotlight can then include the restaurants from your activity objects in the results. Index activity objects only to reflect the content that people touch in your app, not as a substitute for indexing your app’s content using Spotlight.

> [!important] Important
> Your app must maintain a strong reference to any activity objects you make eligible for search.

## See Also

### Enabling system behaviors

- [eligibleForHandoff](iseligibleforhandoff.md) — A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [eligibleForPublicIndexing](iseligibleforpublicindexing.md) — A Boolean value that indicates whether the activity is publicly accessible by all iOS users.
- [eligibleForPrediction](iseligibleforprediction.md) — A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [expirationDate](expirationdate.md) — The date after which the activity is no longer eligible for Handoff or indexing.

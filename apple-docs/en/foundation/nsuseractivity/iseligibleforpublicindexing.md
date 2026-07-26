---
title: isEligibleForPublicIndexing
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsuseractivity/iseligibleforpublicindexing
source_url: 'https://developer.apple.com/documentation/foundation/nsuseractivity/iseligibleforpublicindexing'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsuseractivity/iseligibleforpublicindexing.json'
content_hash: 'sha256:24d6c210525ce500'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSUserActivity](../nsuseractivity.md)

# isEligibleForPublicIndexing

<sub>Instance Property</sub>

A Boolean value that indicates whether the activity is publicly accessible by all iOS users.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var isEligibleForPublicIndexing: Bool { get set }
```

## Discussion

Set the value of this property to `true` to add the activity object to the global Spotlight search indexes. Set the value of this property to `false` if the activity object contains private or sensitive information or if the activity isn’t useful outside your app. The default value of this property is `false`.

If you set this property to `true`, the system indexes the values in the [webpageURL](webpageurl.md) and [requiredUserInfoKeys](requireduserinfokeys.md) properties, and you must provide a value for one of those properties. If you provide a URL, make sure it reflects the same content in both your app and your company’s website. When someone chooses one of your app’s public activities from search results, it tells Apple that your website’s public information is popular, which can increase the ranking of that content in future searches.

> [!important] Important
> Your app must maintain a strong reference to any activity objects you make eligible for search.

## See Also

### Enabling system behaviors

- [eligibleForHandoff](iseligibleforhandoff.md) — A Boolean value that indicates whether the activity can continue on another device using Handoff.
- [eligibleForSearch](iseligibleforsearch.md) — A Boolean value that indicates whether to add the activity to the on-device index.
- [eligibleForPrediction](iseligibleforprediction.md) — A Boolean value that determines whether Siri can suggest the activity as a shortcut.
- [expirationDate](expirationdate.md) — The date after which the activity is no longer eligible for Handoff or indexing.

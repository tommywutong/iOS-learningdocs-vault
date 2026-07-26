---
title: NSMetadataQueryResultContentRelevanceAttribute
framework: Foundation
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsmetadataqueryresultcontentrelevanceattribute
source_url: 'https://developer.apple.com/documentation/foundation/nsmetadataqueryresultcontentrelevanceattribute'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmetadataqueryresultcontentrelevanceattribute.json'
content_hash: 'sha256:59e1d423ad171292'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md)

# NSMetadataQueryResultContentRelevanceAttribute

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSMetadataQueryResultContentRelevanceAttribute: String
```

## Discussion

The key used to retrieve an `NSNumber` object with a floating point value between 0.0 and 1.0 inclusive. The relevance value indicates the relevance of the content of a result object. The relevance is computed based on the value of the result itself, not on its relevance to the other results returned by the query. If the value is not computed, it is treated as an attribute on the item that does not exist.

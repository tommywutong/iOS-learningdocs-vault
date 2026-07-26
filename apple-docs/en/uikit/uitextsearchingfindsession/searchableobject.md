---
title: searchableObject
framework: UIKit
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/uikit/uitextsearchingfindsession/searchableobject
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchingfindsession/searchableobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchingfindsession/searchableobject.json'
content_hash: 'sha256:a2fc0225bbc60bbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchingFindSession](../uitextsearchingfindsession.md)

# searchableObject

<sub>Instance Property</sub>

The object to search, responsible for performing the search operation and decorating the results.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
weak var searchableObject: (any __UITextSearching)? { get }
```

## Discussion

Use the methods this object implements from the [UITextSearching](../uitextsearching-53wjq.md) protocol to search text in your app and decorate the found results.

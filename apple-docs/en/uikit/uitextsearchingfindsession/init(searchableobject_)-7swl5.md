---
title: 'init(searchableObject:)'
framework: UIKit
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, visionOS]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/uikit/uitextsearchingfindsession/init(searchableobject:)-7swl5'
source_url: 'https://developer.apple.com/documentation/uikit/uitextsearchingfindsession/init(searchableobject:)-7swl5'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/uikit/uitextsearchingfindsession/init%28searchableobject%3A%29-7swl5.json'
content_hash: 'sha256:3c7265a7698376d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [UIKit](../../uikit.md) · [UITextSearchingFindSession](../uitextsearchingfindsession.md)

# init(searchableObject:)

<sub>Initializer</sub>

Initializes an object to manage the search for the searchable object you specify.

<sub>iOS, iPadOS, Mac Catalyst, visionOS</sub>

```swift
@MainActor @preconcurrency convenience init<SearchableObject>(searchableObject: SearchableObject) where SearchableObject : UITextSearching
```

## Parameters

- `searchableObject` — An object that conforms to the [UITextSearching](../uitextsearching-53wjq.md) protocol that the session uses to search the text of your app and decorate the found results.

## See Also

### Creating a text searching find session

- [- initWithSearchableObject:](<init(searchableobject_)-9zc4e.md>) — Initializes an object to manage the search for the searchable object you specify.

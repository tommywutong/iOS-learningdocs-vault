---
title: Keys for Use with a Notification Info Dictionary
framework: Foundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/keys-for-use-with-a-notification-info-dictionary
source_url: 'https://developer.apple.com/documentation/foundation/keys-for-use-with-a-notification-info-dictionary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/keys-for-use-with-a-notification-info-dictionary.json'
content_hash: 'sha256:74bf92a76b65748b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Foundation](../foundation.md) · [iCloud](icloud.md) · [NSMetadataQuery](nsmetadataquery.md)

# Keys for Use with a Notification Info Dictionary

<sub>API Collection</sub>

Constants for keys to retrieve the collection of changed items from a notification’s user info dictionary.

## Overview

When querying the ubiquitous scope, these keys get added to the user info dictionary only in OS X v10.10 and iOS 8.0 or later, and only when iCloud Drive is enabled for the user’s iCloud account. To track changes in earlier versions of the SDK, use KVO on the query’s `results` property instead.

## Topics

### Constants

- [NSMetadataQueryUpdateAddedItemsKey](nsmetadataqueryupdateaddeditemskey.md) — The key for retrieving an array of items added to the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [NSMetadataQueryUpdateChangedItemsKey](nsmetadataqueryupdatechangeditemskey.md) — The key for retrieving an array of items that have changed in the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.
- [NSMetadataQueryUpdateRemovedItemsKey](nsmetadataqueryupdateremoveditemskey.md) — The key for retrieving an array of items removed from the query result. By default, this array contains [NSMetadataItem](nsmetadataitem.md) objects, representing the query’s results; however, the query’s delegate can substitute these objects with instances of a different class.

## See Also

### Constants

- [Metadata Query Search Scopes](metadata-query-search-scopes.md) — Constants for the predefined search scopes used by [searchScopes](nsmetadataquery/searchscopes.md).
- [Content Relevance](content-relevance.md) — In addition to including the requested metadata attributes, a query result also includes content relevance, accessed with the following key.

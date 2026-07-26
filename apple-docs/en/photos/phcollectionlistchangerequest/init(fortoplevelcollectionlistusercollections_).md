---
title: 'init(forTopLevelCollectionListUserCollections:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 14.2+, iPadOS 14.2+, Mac Catalyst 14.2+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/init(fortoplevelcollectionlistusercollections:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(fortoplevelcollectionlistusercollections:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/init%28fortoplevelcollectionlistusercollections%3A%29.json'
content_hash: 'sha256:4a5f8b18e2b65c20'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# init(forTopLevelCollectionListUserCollections:)

<sub>Initializer</sub>

Creates a request to add, remove, or rearrange child collections in the top-level collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(forTopLevelCollectionListUserCollections childCollections: PHFetchResult<PHCollection>)
```

## Parameters

- `childCollections` — The child collections to modify.

## See Also

### Creating a Change Request

- [+ changeRequestForCollectionList:](<init(for_).md>) — Creates a request for modifying the specified collection list.
- [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) — Creates a request for modifying the specified collection list, with a fetch result for tracking changes.

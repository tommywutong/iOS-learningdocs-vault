---
title: NSAsynchronousFetchRequest
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsasynchronousfetchrequest
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchrequest'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchrequest.json'
content_hash: 'sha256:151ec1ba619c17fc'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSAsynchronousFetchRequest

<sub>Class</sub>

A fetch request that retrieves results asynchronously and supports progress notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSAsynchronousFetchRequest<ResultType> where ResultType : NSFetchRequestResult
```

## Relationships

- **Inherits From**: [NSPersistentStoreRequest](nspersistentstorerequest.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Initializing a Request

- [- initWithFetchRequest:completionBlock:](<nsasynchronousfetchrequest/init(fetchrequest_completionblock_).md>) — Initializes a new asynchronous fetch request configured with the provided fetch request and completion block.

### Preparing a Request

- [completionBlock](nsasynchronousfetchrequest/completionblock.md) — The block that is executed when the fetch request has completed.
- [estimatedResultCount](nsasynchronousfetchrequest/estimatedresultcount.md) — A configuration parameter that assists Core Data with scheduling the asynchronous fetch request.
- [fetchRequest](nsasynchronousfetchrequest/fetchrequest.md) — The underlying fetch request that is executed asynchronously.

## See Also

### Fetch requests

- [NSFetchRequest](nsfetchrequest.md) — A description of search criteria used to retrieve data from a persistent store.
- [NSAsynchronousFetchResult](nsasynchronousfetchresult.md) — A fetch result object that encompasses the response from an executed asynchronous fetch request.
- [NSFetchedResultsController](nsfetchedresultscontroller.md) — A controller that you use to manage the results of a Core Data fetch request and to display data to the user.

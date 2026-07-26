---
title: NSAsynchronousFetchResult
framework: Core Data
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsasynchronousfetchresult
source_url: 'https://developer.apple.com/documentation/coredata/nsasynchronousfetchresult'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsasynchronousfetchresult.json'
content_hash: 'sha256:e02de25a77ff07f0'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSAsynchronousFetchResult

<sub>Class</sub>

A fetch result object that encompasses the response from an executed asynchronous fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NSAsynchronousFetchResult<ResultType> where ResultType : NSFetchRequestResult
```

## Relationships

- **Inherits From**: [NSPersistentStoreAsynchronousResult](nspersistentstoreasynchronousresult.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Getting Information About a Result

- [fetchRequest](nsasynchronousfetchresult/fetchrequest.md) — The underlying fetch request that was executed.
- [finalResult](nsasynchronousfetchresult/finalresult.md) — The results that were received from the fetch request.

## See Also

### Fetch requests

- [NSFetchRequest](nsfetchrequest.md) — A description of search criteria used to retrieve data from a persistent store.
- [NSAsynchronousFetchRequest](nsasynchronousfetchrequest.md) — A fetch request that retrieves results asynchronously and supports progress notification.
- [NSFetchedResultsController](nsfetchedresultscontroller.md) — A controller that you use to manage the results of a Core Data fetch request and to display data to the user.
